#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Simon Matern
"""

import numpy as np
import cv2
import utils


def binarizeImage(img, thresh):
    """
    Given a coloured image and a threshold binarizes the image.
    Values below thresh are set to 0. All other values are set to 255
    """
    # TODO
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] < thresh and img[i][j][1] < thresh and img[i][j][2] < thresh:
                img[i][j] = [0, 0, 0]
            else:
                img[i][j] = [255, 255, 255] 
    
    return img

def smoothImage(img):    
    """
    Given a coloured image apply a blur on the image, e.g. Gaussian blur
    """
    # TODO
    gaussian_blur = [1/16, 1/8, 1/16, 1/8, 1/4, 1/8, 1/16, 1/8, 1/16]
    img = cv2.filter2D(img, -1, np.array(gaussian_blur))

    return img

def doSomething(img):
    """
    Given a coloured image apply any image manipulation. Be creative!
    """
    # TODO
    random_array = np.random.randint(100, 200, (3, 3))
    print(random_array)
    img = cv2.filter2D(img, -1, random_array)
    
    return img


def processImage(img):
    """
    Given an coloured image applies the implemented smoothing and binarization.
    """
    # TODO
    img = smoothImage(img)
    img = binarizeImage(img, 190)
    return img


if __name__=="__main__":
    img = cv2.imread("test.jpg")
    utils.show(img)
    
    # img1 = smoothImage(img)
    # utils.show(img1)
    # cv2.imwrite("result1.jpg", img1)
    
    # img2 = binarizeImage(img, 190)
    # utils.show(img2)
    # cv2.imwrite("result2.jpg", img2)
   
    # img3 = processImage(img)
    # utils.show(img3)
    # cv2.imwrite("result3.jpg", img3)
    
    # img4 = doSomething(img)
    # utils.show(img4)
    # cv2.imwrite("result4.jpg", img4)

    img5 = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.4)
    utils.show(img5)
