from PIL import Image
import numpy as np
import cv2
from skimage import data, color, exposure
from skimage.feature import hog
def crop_test():
    k=1
    img = Image.open('C:/Python27/svm/door/003.jpg')
    for a in range(42):
        for b in range(42):
            box=(0 + b * 30, 30 + a * 30, 30 + b * 30, 60 + a * 30)
            resize = img.crop(box)
            resize.save("C:/Python27/svm/door/test/" + np.str(k) + '.jpg')
            k = k + 1
crop_test()
def crop_test2():
    k=1
    img = Image.open('C:/Python27/svm/door/004.jpg')
    for a in range(10):
        for b in range(10):
            box=(0 + b * 30, 30 + a * 30, 30 + b * 30, 60 + a * 30)
            resize = img.crop(box)
            resize.save("C:/Python27/svm/door/test2/" + np.str(k) + '.jpg')
            k = k + 1
crop_test2()
def crop_pos():
    k=1
    img = Image.open('C:/Python27/svm/door/pos_sample/001.jpg')
    for a in range(11):
        for b in range(12):
            box=(0 + b * 30, 30 + a * 30, 30 + b * 30, 60 + a * 30)
            resize = img.crop(box)
            resize.save("C:/Python27/svm/door/pos/" + np.str(k) + '.jpg')
            k = k + 1
crop_pos()
def crop_pos2():
    k=1
    img = Image.open('C:/Python27/svm/door/pos_sample/002.jpg')
    for a in range(14):
        for b in range(15):
            box=(0 + b * 30, 30 + a * 30, 30 + b * 30, 60 + a * 30)
            resize = img.crop(box)
            resize.save("C:/Python27/svm/door/pos/" + np.str(k) + '.jpg')
            k = k + 1
crop_pos2()

def crop_neg():
    k=1
    img = Image.open('C:/Python27/svm/door/neg_sample/001.jpg')
    for a in range(6):
        for b in range(25): #x
            box=(0 + b * 20, 0 + a * 20, 20 + b * 20, 20 + a * 20)
            resize = img.crop(box)
            resize.save("C:/Python27/svm/door/neg/" + np.str(k) + '.jpg')
            k = k + 1
crop_neg()
def crop_neg2():
    k=151
    img = Image.open('C:/Python27/svm/door/neg_sample/005.jpg')
    for a in range(2):
        for b in range(26): #x
            box=(0 + b * 20, 0 + a * 20, 20 + b * 20, 20 + a * 20)
            resize = img.crop(box)
            resize.save("C:/Python27/svm/door/neg/" + np.str(k) + '.jpg')
            k = k + 1
crop_neg2()



crop_test()
crop_neg()


