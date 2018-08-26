
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

workbook = xlsxwriter.Workbook('feature.xlsx')
worksheet = workbook.add_worksheet()
row=0
col=0

base_model = ResNet50(weights='imagenet')
model=Model(input=base_model.input, outputs=base_model.get_layer('flatten_1').output)
max_pre=np.zeros((1,2048))


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

print(label_list)
for i in range(1,2): 
	INPUT='/root/Pathology/process_'+str(i)+'_labelled/' 
	images=os.listdir(INPUT)
	col=0
	for x in images:
		img_path=INPUT+'/'+x
		img = image.load_img(img_path,target_size=(224,224))
		x1 = image.img_to_array(img)
		x1 = np.expand_dims(x1,axis=0)
		x1 = preprocess_input(x1)
		pre = model.predict(x1)
		#print(x)
		#print(preds)
		#print(np.shape(preds))
		for j in range(0,2048):
			if pre[0][j] > max_pre[0][j]:
				max_pre[0][j]=pre[0][j]

	#max_fin=np.transpose(max_pre)
	max_fin=max_pre
	#print(np.shape(max_fin))
	label_np_data=np.array([[label_list[i-1]]])
	np.append(max_fin,label_np_data,axis=1)
	max_fin=np.transpose(max_fin)
	for Value in (max_fin):
		worksheet.write(row,col,Value)
		col=col+1
	row=row+1
	
workbook.close()
