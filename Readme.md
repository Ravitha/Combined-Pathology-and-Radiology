# COMBINED RADIOLOGY AND PATHOLOGY BASED CLASSIFICATION OF TUMOR TYPES
Pathology images provide clinical information about the tissues where as the radiology images can be used for locating the lesions <br/>

:pencil2:This work aims at proposing a classification model which categorizes the tumor as oligodendroglioma (benign tumors) (or) astrocytoma (Malignant tumors) <br/> The architecture uses dedicated workflows for processing pathology and radiology images. 

# WORKFLOW FOR TUMOR CLASSIFICATION
![](image.png)   







# Files 

*tissue_percent.py*

  Eliminates the unuseful tiles using the features of the histogram
  Threshold value are computed directly from the histogram against which the intensity values are compared
  
  Performs color deconvolution to extract H image using Reinhard algorithm
  
  Segments the nuclei using Fuzzy means clustering provided in histomicstk package
  Features are extracted using ResNet50
  
 *SVM_Train.py*
 
  Creates an SVM model using Scikit-learn package


# Classification model:
The feature vectors from radiology and pathology images are concatenated and are given to the SVM (Support Vector Machine) classification model. SVM is a statistical tool which can learn the non-linear boundaries to separate the data points. As the data points provide a sparse representation, SVM is preferred.

:dart: The work has been published as a chapter which provides an detailed explanation of each components in the model pipeline<br/>
Cite the work if you use the material in the link<br/>
>Ravitha Rajalakshmi N., Sangeetha B., Vidhyapriya R., Ramesh N. (2021) Combined Radiology and Pathology Based Classification of Tumor Types. In: Kose U., Alzubi J. (eds) Deep Learning for Cancer Diagnosis. Studies in Computational Intelligence, vol 908. Springer, Singapore. https://doi.org/10.1007/978-981-15-6321-8_6
