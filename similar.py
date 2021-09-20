import cv2
import numpy as np
from PIL import Image
import os

def aHash(img,shape=(10,10)):
    img = cv2.resize(img, shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    s = 0
    hash_str = ''
    for i in range(shape[0]):
        for j in range(shape[1]):
            s = s + gray[i, j]
    avg = s / 100
    for i in range(shape[0]):
        for j in range(shape[1]):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str

def cmpHash(hash1, hash2,shape=(10,10)):
    n = 0
    if len(hash1)!=len(hash2):
        return -1
    for i in range(len(hash1)):
        if hash1[i] == hash2[i]:
            n = n + 1
    return n/(shape[0]*shape[1])
   

def findSimilarity(orjinal_img_path, referans_img_path):
    img1 = cv2.imread('./imageList/'+orjinal_img_path)
    img2 = cv2.imread('./'+referans_img_path)
    hash1 = aHash(img1)
    hash2 = aHash(img2)
    n = cmpHash(hash1, hash2)
    n = n*100
    os.remove("./"+referans_img_path)
    return n