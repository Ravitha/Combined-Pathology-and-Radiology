# COMBINED RADIOLOGY AND PATHOLOGY BASED CLASSIFICATION OF TUMOR TYPES
Computer Aided Detection plays a crucial role in the early detection of deadly diseases such as cancer (or) tumor. Pathology and radiology images form the core of tumor diagnosis. Pathology images provide clinical information about the tissues where as the radiology images can be used for locating the lesions.  This work aims at proposing a classification model which categorizes the tumor as oligodendroglioma (benign tumors) (or) astrocytoma (Malignant tumors). The architecture uses dedicated workflows for processing pathology and radiology images. 
Pathology Image Processing Pipeline:
 A whole slide tissue image in SVS format is provided for each case in the dataset. Whole slide images comprises of a pyramid structure holding multiple images at different resolution. VIPS utility is used to tile the baseline image into (256,256) tiles. It's been recorded in the literature that nuclei appears to have a rough texture in malignant tumors as opposed to smooth regular texture in benign tumors. As the morphology of the nuclei acts as an important attribute in the classification, nuclei is segmented and been used for feature extraction. The pathology images are Hematoxylin and Eosin (H&E) stained whole slide tissue images. Hematoxylin stain enhances the nuclei in the image. So, Reinhard's color deconvolution algorithm is applied for the separation of H & E stains from the Image. The H-stained portion of the image is subjected to local maximum clustering for segmentation of nuclei region. The resulting segmentation mask is then applied to the original image for the extraction of the texture details.
 








# Files 
tissue_percent.py  

  Eliminates the unuseful tiles using the features of the histogram
  Threshold value are computed directly from the histogram against which the intensity values are compared
  
  Performs color deconvolution to extract H image using Reinhard algorithm
  
  Segments the nuclei using Fuzzy means clustering provided in histomicstk package
  Features are extracted using ResNet50
  
 SVM_Train.py
 
  Creates an SVM model using Scikit-learn package
