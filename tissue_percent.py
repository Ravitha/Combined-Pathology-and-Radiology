
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras import backend as K
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import Model
import xlsxwriter
import histomicstk as htk
import numpy as np
import scipy as sp
import scipy.misc
import skimage.io
import skimage.measure
import skimage.color
from scipy.misc import imresize
from PIL import Image
import cv2
import os
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#Initialize the ResNet Model
base_model = ResNet50(weights='imagenet')
model=Model(input=base_model.input, outputs=base_model.get_layer('flatten_1').output)
max_pre=np.zeros((1,2048))

# Find labels for the images
file_name_list=[]
label_list=[]

with open('label_data.txt') as f:
        for line in f.readlines():
                file_name,label=line.split(" ")
                a,b,c=file_name.split("_")
                if (similar(label,"A")>0.5):
                        label_list.append(1)
                else:
                        label_list.append(0)
                file_name_list.append(c)

stainColorMap = {
    'hematoxylin': [0.65, 0.70, 0.29],
    'eosin':       [0.07, 0.99, 0.11],
    'dab':         [0.27, 0.57, 0.78],
    'null':        [0.0, 0.0, 0.0]
}

stain_1 = 'hematoxylin'   # nuclei stain
stain_2 = 'eosin'         # cytoplasm stain
stain_3 = 'null'          # set to null of input contains only two stains


def Max_Feature(max_pre,pre):
        max_pre=np.maximum(max_pre,pre)
        return max_pre

def adjust_gamma(image, gamma=0.5):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

def tissue_percent(hist,pixels):
	"""
	Compute the tissue percentage based on the number of pixels in first three bins
	hist - histogram of the image
	pixels - count of pixels
	"""
	sum=0
	for i in range(3):
		sum=sum+hist[i]
	return sum/pixels

def total_pixels(img):
	"""
	img - Input Image (2-D numpy Array)
	It computes the number of pixels in an array
	"""
	size=img.shape
	row=size[0]
	column=size[1]
	total=row * column
	return total

def nuclei_Segment(INPUT_IMAGE,max_pre):
	#print(INPUT_IMAGE)
	img=cv2.imread(INPUT_FOLDER+'/'+INPUT_IMAGE)
	hist=cv2.calcHist([img],[0],None,[4],[0,256])
	W = np.array([stainColorMap[stain_1],stainColorMap[stain_2],stainColorMap[stain_3]]).T
	im_stains = htk.preprocessing.color_deconvolution.color_deconvolution(img, W).Stains
	im_nuclei_stain = im_stains[:, :, 0]
        #cv2.imwrite("H_Stained_Image.jpeg",im_nuclei_stain)
	hist1=cv2.calcHist([im_nuclei_stain],[0],None,[4],[0,256])
	pixel_count=total_pixels(im_nuclei_stain)
	percentile=tissue_percent(hist,pixel_count)
	percentile_H=tissue_percent(hist1,pixel_count)
	#print(percentile)
	if percentile_H>0.7:
		if percentile_H<0.9 and percentile<0.55:
			im_nuclei_stain=adjust_gamma(im_nuclei_stain,0.60)

		"""
		# Segment foreground
		foreground_threshold =30
		im_fgnd_mask = sp.ndimage.morphology.binary_fill_holes(im_nuclei_stain < foreground_threshold)

		# Run adaptive multi-scale LoG filter
		min_radius = 10
		max_radius = 15

		im_log_max, im_sigma_max = htk.filters.shape.cdog(
    			im_nuclei_stain, im_fgnd_mask,
    			sigma_min=min_radius * np.sqrt(2),
    			sigma_max=max_radius * np.sqrt(2)
		)

		# Detect and segment nuclei using local maximum clustering
		local_max_search_radius = 10
		im_nuclei_seg_mask, seeds, maxima = htk.segmentation.nuclear.max_clustering(
    			im_log_max, im_fgnd_mask, local_max_search_radius)

		# Filter out small objects
		min_nucleus_area =80 
		im_nuclei_seg_mask = htk.segmentation.label.area_open(im_nuclei_seg_mask, min_nucleus_area).astype(np.int)
		objProps = skimage.measure.regionprops(im_nuclei_seg_mask)
		#print 'Number of nuclei = ', len(objProps)
		if len(objProps)>=10:
			im_nuclei_1=im_nuclei_seg_mask[:,:]>0
			im_nuclei_1=np.dot(im_nuclei_1,1)
		#kernel = np.ones((5,5))
	        #print(type(im_nuclei_1))
                #im_nuclei_1 = cv2.erode(im_nuclei_1,kernel,iterations = 1)
			#print('YES')
			im_nuclei_1 = np.repeat(im_nuclei_1[:, :, np.newaxis], 3, axis=2)
			im_nuclei_1=im_nuclei_1*img
			#cv2.imwrite(OUTPUT_FOLDER+INPUT_IMAGE,im_nuclei_1)
			#print(type(im_nuclei_1))
			#print(im_nuclei_1.shape)
		"""	
		x1=np.resize(im_nuclei_stain,(224,224,3))
			#x1 = cv2.resize(im_nuclei_1, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
			#img = image.load_img(img_path,target_size=(224,224))
	                #x1 = image.img_to_array(im_nuclei_1)
		x1 = np.expand_dims(x1,axis=0)
                x1 = preprocess_input(x1)
                pre = model.predict(x1)
		max_pre=Max_Feature(max_pre,pre)
	return max_pre

for i in range(1,33):
	# Create Workbook
	workbook = xlsxwriter.Workbook('feature_nuclei_seg_'+str(i)+'.xlsx')
	worksheet = workbook.add_worksheet()
	print(i)
	row=0

	INPUT='/root/Pathology/process_'+str(i)+'\_files'
	files = os.listdir(INPUT)
	#OUTPUT_FOLDER='/root/Pathology/color_normalize/process_'+str(i)+'_colornormalize'
	number_of_files=len(files)-3
	INPUT_FOLDER=INPUT+'/'+str(number_of_files)
	#if not os.path.exists(OUTPUT_FOLDER):
	#	os.mkdir(OUTPUT_FOLDER)
	images=os.listdir(INPUT_FOLDER)
	max_pre=np.zeros((1,2048))
	for x in images:
		max_pre=nuclei_Segment(x,max_pre)
		max_fin=max_pre
                max_fin=np.transpose(max_fin)
                #print(np.shape(max_fin))
                col=0
                for Value in (max_fin):
			worksheet.write(row,col,Value)
                        col=col+1
		max_fin=[]

	workbook.close()

