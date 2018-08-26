
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import Model
import numpy as np
import xlsxwriter
import os
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_Features(INPUT,x):
        image_path=INPUT+'/'+x
        img = image.load_img(image_path,target_size=(224,224))
        x1 = image.img_to_array(img)
        x1 = np.expand_dims(x1,axis=0)
        x1 = preprocess_input(x1)
        pre = model.predict(x1)
        return pre


def Max_Feature(max_pre,pre):
        max_pre=np.maximum(max_pre,pre)
        return max_pre


workbook = xlsxwriter.Workbook('feature_rad.xlsx')
worksheet = workbook.add_worksheet()
row=0
col=0

base_model = ResNet50(weights='imagenet')
model=Model(input=base_model.input, outputs=base_model.get_layer('flatten_1').output)
max_pre=np.zeros((1,2048))


file_name_list=[]
label_list=[]

with open('/root/Pathology/label_data.txt') as f:
	for line in f.readlines():
		file_name,label=line.split(" ")
		a,b,c=file_name.split("_")
		##label_list.append(similar(label,"A"))
		if (similar(label,"A")>=0.5):
			label_list.append(1)
		else:
			label_list.append(0)
		file_name_list.append(c)
##print(label_list)
##print(file_name_list)
"""
	 #Read the folder in the TestFast folder
	 #Read the images in the folder
	 #Generate features in the image
"""

INPUT_FOLDER='/root/Radiology/Fast/'
INPUT_SUB_FOLDERS=os.listdir(INPUT_FOLDER)
row=0
col=0

for folder in INPUT_SUB_FOLDERS:
	SUB_FOLDER=INPUT_FOLDER+folder
	#print(SUB_FOLDER)
	file_name=folder.split("-")
	if (len(file_name)==2):
		row=file_name[1]
		print("row")
		print(row)
		INPUT=SUB_FOLDER
		#print(INPUT)
		print("INPUT")
		print(INPUT)
		if os.path.exists(INPUT):
			images=os.listdir(INPUT)
			max_pre=np.zeros((1,2048))
			for x in images:
				print(x)
				pre=find_Features(INPUT,x)
				max_pre=Max_Feature(max_pre,pre)
			max_fin=max_pre
			#z=file_name_list.index(file_name[1])
       		 	#label_np_data=np.array([[float(label_list[z])]])
        		#print("label")
			#print(label_np_data)
			#np.append(max_fin,label_np_data,axis=1)
                	max_fin=np.transpose(max_fin)
                	print(np.shape(max_fin))
			col=0
			for Value in (max_fin):
				worksheet.write(int(row)-1,col,Value)
                		col=col+1
			max_fin=[]
workbook.close()

