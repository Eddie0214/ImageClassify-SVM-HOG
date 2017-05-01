# -*- coding: UTF-8 -*-
from glob import glob
from PIL import Image
import numpy as np
from sklearn.decomposition import PCA
from sklearn import svm
from skimage import data, color, exposure
from skimage.feature import hog
import cv2
all_data_set = [] #原始总数据集，二维矩阵n*m，n个样例，m个属性
all_data_label = [] #总数据对应的类标签
PICTURE_neg =  "C:/Python27/coin_svm/neg/"
def get_neg():
    label = 1
    #读取所有图片并一维化
    if (label <= 3): #
        for name in glob(PICTURE_neg + "\\*.jpg"):
            img = Image.open(name)
            img= img.convert('L')
            img = list(img.getdata())  # 转换为一个一维数组，按照行排列
            all_data_set.append(img)  # getdata 一維化
            all_data_label.append(0)
            label += 1
get_neg()
PICTURE_pos =  "C:/Python27/coin_svm/pos/"
def get_pos():
    label = 1
    #读取所有图片并一维化
    if (label <= 6): #
        for name in glob(PICTURE_pos + "\\*.jpg"):
            img = Image.open(name)
            img= img.convert('L')
            img = list(img.getdata())  # 转换为一个一维数组，按照行排列
            all_data_set.append(img)  # getdata 一維化
            all_data_label.append(1)
            label += 1
get_pos()


X = np.array(all_data_set)
Y = np.array(all_data_label)
clf = svm.SVC()
clf.fit(X, Y)
test=[]
PICTURE_test=  "C:/Python27/coin_svm/test/"
def get_test():
    label = 1
    #读取所有图片并一维化
    if (label <= 9): #
        for name in glob(PICTURE_test + "\\*.jpg"):
            img = Image.open(name)
            img= img.convert('L')
            img = list(img.getdata())  # 转换为一个一维数组，按照行排列
            test.append(img)  # getdata 一維化
            label += 1
get_test()
test_array = np.array(test)
