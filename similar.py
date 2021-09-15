import cv2
import numpy as np
from PIL import Image
import os


def classify_hist_with_split(image1, image2, size=(256, 256)):
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree
   

def findSimilarity(orjinal_img_path, referans_img_path):
    img1 = cv2.imread('./imageList/'+orjinal_img_path)
    img2 = cv2.imread('./'+referans_img_path)
    threeHist = classify_hist_with_split(img1, img2) 
    try:
    
        compareResult = int(round(threeHist[0]*100,1))
    except:
        compareResult = 100
    os.remove("./"+referans_img_path)
    return compareResult