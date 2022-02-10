import os.path
from os import path
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import cv2


class image_editor():
    def __init__(self, img_name):
        self.img = None
        self.height = None
        self.width = None
        self.median = None
        self.gaussian = None
        self.bilateral = None
        self.dilated = None
        self.erode = None
        self.sobelx = None
        self.sobely = None

        try:
            self.img = cv2.imread(img_name)

        except IOError:
            pass


    def median_filter(self, k, save_path= None):
        self.median = cv2.medianBlur(self.img, k)
        plt.subplot(1, 2, 1), plt.imshow(self.img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.median, cmap='gray')
        plt.title('Median Filter'), plt.xticks([]), plt.yticks([])
        if save_path:
            cv2.imwrite(save_path, self.median)
        plt.show()

    def gaussian_filter(self, k, save_path= None):
        self.gaussian = cv2.GaussianBlur(self.img, (k, k), 0)
        plt.subplot(1, 2, 1), plt.imshow(self.img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.gaussian, cmap='gray')
        plt.title('Gaussian Filter'), plt.xticks([]), plt.yticks([])
        if save_path:
            cv2.imwrite(save_path, self.median)
        plt.show()


    def bilateral_filter(self, k, save_path= None):
        self.bilateral = cv2.bilateralFilter(self.img, k, 80, 80)
        plt.subplot(1, 2, 1), plt.imshow(self.img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.bilateral, cmap='gray')
        plt.title('Bilateral Filter'), plt.xticks([]), plt.yticks([])
        if save_path:
            cv2.imwrite(save_path, self.median)
        plt.show()


    def dilation (self, k, save_path= None):
        self.dilated = cv2.dilate(self.img, (k,k))
        plt.subplot(1, 2, 1), plt.imshow(self.img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.dilated, cmap='gray')
        plt.title('Dilated'), plt.xticks([]), plt.yticks([])
        if save_path:
            cv2.imwrite(save_path, self.median)
        plt.show()


    def erosion (self, k, save_path= None):
        self.erode = cv2.dilate(self.img, (k,k))
        plt.subplot(1, 2, 1), plt.imshow(self.img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 2, 2), plt.imshow(self.erode, cmap='gray')
        plt.title('Eroded'), plt.xticks([]), plt.yticks([])
        if save_path:
            cv2.imwrite(save_path, self.median)
        plt.show()


    def sobel_filter(self, k , save_path = None):
        self.sobelx = cv2.Sobel(self.img, cv2.CV_64F, 1, 0, k)
        self.sobely = cv2.Sobel(self.img, cv2.CV_64F, 0, 1, k)

        plt.subplot(1, 3, 1), plt.imshow(self.img, cmap= 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 3, 2), plt.imshow(self.sobelx, cmap='gray')
        plt.title('Sobel Horizontal'), plt.xticks([]), plt.yticks([])
        plt.subplot(1, 3, 3), plt.imshow(self.sobely, cmap='gray')
        plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])

        if save_path:
            cv2.imwrite(save_path, self.sobel)
        plt.show()


