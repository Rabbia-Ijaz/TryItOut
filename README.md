# FYP

TextureMod is the feature where the user provides a Source image and a Pattern image and the model maps the pattern on the Source image.

#### 5 classes
User
Data
PreProcessing
TextureMod
Database

*User class is the dummy class right now and will be used when we will connect it with the front-end.
*Data class takes links of Source and Pattern images and returns the numpy arrays of colored and gray scale images of Source and Pattern
*PreProcessing class takes the grayscale image of Source and apply threshold on it and returns the results 
*Database is the dummy class for saving the results
*TextureMod has multiple functions such as Blend(), Pattern(), KMeansAlgo(), FinalDetails(), secondMin() and firstMin()

Blend(self,img,pattern) takes img and patterns and then maps the pattern on the img and blends it

Pattern(self,srcC,srcG,patternC,patternG,thresh,blend) takes the thresh and blend which are the outputs of Thresholding() and Blend() and use other parameters to map the blended image on the thresholded image to get the outlined image of dress with the pattern on it.

KMeansAlgo(self,img,K) is responsible to extract the details of the original Source image so that we can apply it on the mapped image

secondMin() and firstMin() are helping functions to extract the small details

FinalDetails(self,srcC,result,res,res2) is responsible to apply those small details that we extracted from KMeansAlgo(), secondMin() and firstMin() on the mapped image and then get the realistic output
  
