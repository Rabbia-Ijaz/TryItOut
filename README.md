## TextureMod
TextureMod is the feature where the user provides a Source image and a Pattern image and the model maps the pattern on the Source image.

### 6 classes
User, Data, PreProcessing, TextureMod, Result, Database

    #### User class is the dummy class right now and will be used when we will connect it with the front-end.
    #### Data class takes links of Source and Pattern images and returns the numpy arrays of colored and gray scale images of Source and Pattern
    #### PreProcessing class takes the grayscale image of Source and apply threshold on it and returns the results 
    #### Result is the class for saving the results
    #### Database is the dummy class for saving the all the results with user id and name
    #### TextureMod has multiple functions such as Blend(), Pattern(), KMeansAlgo(), FinalDetails(), secondMin() and firstMin()
       # Blend(self,img,pattern) takes img and patterns and then maps the pattern on the img and blends it.
       # Pattern(self,srcC,srcG,patternC,patternG,thresh,blend) takes the thresh and blend which are the outputs of Thresholding() and Blend() and use other parameters to map the blended image on the thresholded image to get the outlined image of dress with the pattern on it.
       # KMeansAlgo(self,img,K) is responsible to extract the details of the original Source image so that we can apply it on the mapped image
       # secondMin() and firstMin() are helping functions to extract the small details
       # FinalDetails(self,srcC,result,res,res2) is responsible to apply those small details that we extracted from KMeansAlgo(), secondMin() and firstMin() on the mapped image and then get the realistic output
#### Result files
    Texture_Mod has three folders, Source, Pattern and Result. Result folder has the final output after mapping
![alt_text](https://user-images.githubusercontent.com/63001234/115640203-d0fd8c80-a32f-11eb-947f-ac1ac74c3090.png)



## TailorMod
TailorMod is the feature where the user provides a Source image and a Target image and the model maps the collar of the Source image on the Target Image.

### 6 classes
User, Data, PreProcessing, TailorMod, Result, Database (in both files,classes are same but we will combine them when we will have a front-end)

    #### User class is the dummy class right now and will be used when we will connect it with the front-end.
    #### Data class takes links of Source and Pattern images and with the help of trained machine learning model, it extracts the bounding boxes of collars.
    #### PreProcessing class takes source and target images and applies blending on it with the help of Blending(), KMeansAlgo(), FinalDetails(), firstMin(), secondMin()
       # KMeansAlgo(self,img,K) is responsible to extract the details of the original Source image so that we can apply it on the target image
       # secondMin() and firstMin() are helping functions to extract the small details
       # FinalDetails(self,srcC,result,res,res2) is responsible to apply those small details that we extracted from KMeansAlgo(), secondMin() and firstMin() on the target image and to get the realistic output
    #### Result is the class for saving the results
    #### Database is the dummy class for saving the all the results with user id and name
    #### TextueMod has multiple functions such as rotate(), checkOutliars(), getDifference() and Mapping()

       # rotate() applies rotation on source image to map it seamlessly on the area of target bounding box.
       # checkOutliars(), getDifference() are the helping functions
       # Mapping() is the main function which is applying the source part on the collar part with the help of rotation and other helping functions.


## Boxgen
This file contains the code for generating a bounding box for sleeves and collars
![alt_text](https://user-images.githubusercontent.com/63001234/115639071-208e8900-a32d-11eb-9279-5213a0479fab.png)

## GarmentTransfer
GarmentTransfer is the feature where the user provides a Source image and a Target image and the model replicates the shirt of the Source image on the Target Image Body

![alt_text](https://user-images.githubusercontent.com/63001234/115639164-5d5a8000-a32d-11eb-9130-aea1d5095261.png)

## MotionTransfer
MotionTransfer is the feature where the user provides a Source image and a Target video and the model replicates the shirt of the Source image on the Target Body in the video





