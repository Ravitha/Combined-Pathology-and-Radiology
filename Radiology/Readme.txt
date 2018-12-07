MRI images play a vital role in clinical neuro-imaging in the detection of tumor. They are acquired with several different techniques (pulse sequences) and acquisition parameters (called e.g. echo time, TE, repetition time TR etc.) resulting in different image contrast. The dataset provided all the most common  most common MR acquisitions: T1, T1.c, T2 and FLAIR sequences. T1.c MRI is obtained after the administration of contrast media. Tumor regions show signal enhancement after administration of contrast agent and hence T1.c images are considered in the classification task. FSL library is used for analyzing the brain imaging data. The pipeline starts with application of BET command to remove the skull portions . FAST is then applied to categorize the brain regions as grey matter, white matter, CSF and tumor region. The segmented suspicious tissue slices are then fed to Inception V3 and feature vectors are generated independently (i.e) one after the another. med2image package is used in the  conversion of Nifti volumes to slices into jpg format. The feature vectors from all the slices are max pooled wherein the maximum of all vectors for each input value is considered. The resulting feature vector is then used for the representation of the radiology image. 


There is a python package called nipype which has inbuilt fsl functionalities. Using the inbuilt functions of nipype the following processes are carried out for segmentation of tumour/lesion part of the image.

Step-1:

All the three T1, T2 and FLAIR images are co-registered using T1C as reference image since T1C has better results compared to others(as suggested by doctors).FLIRT command of FSL is used for this purpose.

Step-2:

Next T1C is given as input for BET command of FSL. This adjusts the threshold for the extraction to assure that the skull is removed while cortical surface is left intact.

Step-3:

Then the output of BET command is fed to FAST command of FSL as input with input specifications such as number of classes=4 and number of iterations=8(for better performance). This generates four segmented images each image highlighting CSF, Grey matter, White matter and lesion parts. Out of four images pve_1 generated highlights lesions.

Step-4:

There is a package called med2image. This helps in converting Nifti volumes’ all the individual slices into jpg format. Then the pve_1 image is separated into slices and intermediary slices are taken for feature vector extraction.
