# Pathology Image Processing Pipeline:

<ul>
 <li>VIPS utility is used to convert the baseline WSI image into (256,256) tiles</li>
 <li>Reinhard's color deconvolution algorithm is applied for the separation of H & E stains from the Image</li>
 <li>H-stained portion of the image is subjected to local maximum clustering for segmentation of nuclei region</li>
 <li>The resulting segmentation mask is then applied to the original image for the extraction of the texture details</li>
</ul>

# Files
excelwithkera.py - Converting the images into feature vectors using ResNet50 model (Keras)
