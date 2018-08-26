from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from sklearn.svm import SVC 

####################Training Dataset#########################

Train_Rad = pd.read_csv("Training_rad.csv",header=None)
Train_Path= pd.read_csv("Training_path.csv",header=None)

Train_Path_Array=np.array(Train_Path)
Train_Rad_Array=np.array(Train_Rad)
Train_Label= Train_Rad_Array[:,2048]
#Train =np.concatenate((Train_Rad_Array[:,0:2047],Train_Path_Array),axis=1)
Train=Train_Rad_Array[:,0:2047]
pca=PCA(n_components=50)
pca.fit(Train)
Train_PCA=pca.transform(Train)



####SVM Model Building

clf = SVC(kernel='linear')
clf.fit(Train_PCA, Train_Label)


def percentage(input,output):
	count=0
	for i in range(32):
		if clf.predict([input[i]])==output[i]:
			count=count+1

	print("Percentage:")
	print(count)


##################Test Dataset##############################
Test_Rad=pd.read_csv("Test_rad.csv",header=None)
Test_Rad_Array=np.array(Test_Rad)
Test_Path= pd.read_csv("Test_path.csv",header=None)
Test_Path_Array=np.array(Test_Path)

#Test=np.concatenate((Test_Rad_Array[:,0:2047],Test_Path_Array),axis=1)
Test=Test_Rad_Array[:,0:2047]
Test_PCA=pca.transform(Test)
for i in range(20):
	y_predict=clf.predict([Test_PCA[i]])
	if y_predict==1 :
		print("i"+":"+"O")
	else:
		print("i"+":"+"A")
