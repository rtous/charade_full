#requires dependencies from partial2D

import json
import cv2
import numpy as np
import math
import poseUtils
from os import listdir
from os.path import isfile, join, splitext
import pathlib


WIDTH = 64
HEIGHT = 64
SPINESIZE = WIDTH/4
THRESHOLD = 0.1
HAVETHRESHOLD = True
INPUTPATHIMAGES = "input/images"
INPUTPATHKEYPOINTS = "input/keypoints"
OUTPUTPATH = "result/2D/blank_images"

pathlib.Path(OUTPUTPATH).mkdir(parents=True, exist_ok=True) 

imageFiles = [f for f in listdir(INPUTPATHIMAGES) if isfile(join(INPUTPATHIMAGES, f))]
for filename_image in imageFiles:

    filename_noextension = splitext(filename_image)[0]
    filename_keypoints = filename_noextension+"_keypoints.json"

    keypoints = openPoseUtils.json2Keypoints(join(INPUTPATHKEYPOINTS, filename_keypoints))

    originalImagePath = join(INPUTPATHIMAGES, filename_keypoints)
    originalImage = cv2.imread(originalImagePath)
    originalImageWidht = originalImage.widht
    orighinalImageHeight = originalImage.height
    blackImage = np.zeros((originalImageWidht,orighinalImageHeight,3), dtype=np.uint8)

    poseUtils.draw_pose(blackImage, keypoints, THRESHOLD, openPoseUtils.POSE_BODY_25_PAIRS_RENDER_GP, openPoseUtils.POSE_BODY_25_COLORS_RENDER_GPU, HAVETHRESHOLD)
    
    try:
      target_path = join(OUTPUTPATH, filename_noextension+"_pose.jpg", blackImage)
      cv2.imwrite(target_path)
    except:
      print("WARNING: Cannot write to "+target_path)  






    



