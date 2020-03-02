import os
import numpy as np
from PIL import Image
import cv2

def train_classifier(data_dir):
    allImagePaths = [os.path.join(data_dir, f) for f in os.listdir(data_dir)] #this is used to create the relative of all image that are stored in dara_dir all these paths are stored in python list 'allImagePaths'
    
    faces = [] #this list will store the images in the form of numpy array
    ids = []   #this list will store the userID of the numpy image coressponding to faces list

    for image in allImagePaths:
        img = Image.open(image).convert('L') #'L' is used to convert the image to gray scale
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])

        faces.append(imageNp)
        ids.append(id)

    ids = np.array(ids) #now convert the whole python list to numpy array as for training purpose we have to use numpy array rather than python list 
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.yml")
    print(*allImagePaths, sep="\n")
    print("The above mentioned images are used for training purpose")

# MAIN
train_classifier("dataset") #Passing directory name as args.


