import numpy as np
import cv2
from PIL import Image
from glob import glob
from sklearn.decomposition import PCA
from sklearn import svm
from skimage import data, color, exposure
#=================Sobel================#
def sobel(image,k):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image=cv2.resize(image,(1260,1260))
    sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    cv2.imwrite('C:/Python27/coin_svm/sobel/' + np.str(k) + '.jpg'  , sobelCombined)
    cv2.resizeWindow('coin', 1260, 1260)
    cv2.imshow('coin1', sobelCombined)
    cv2.waitKey(0)

#=================Crop===============#
def crop_test():
    k=1
    img = Image.open('C:/Python27/coin_svm/sobel/2.jpg')
    for a in range(3):
        for b in range(3):
            box=(0 + b * 420, 0 + a * 420, 420 + b * 420, 420 + a * 420)
            resize = img.crop(box)
            resize.save('C:/Python27/coin_svm/crop/ '+np.str(k)+'.jpg')
            k = k + 1
crop_test()

all_data_set = []
all_data_label = []
PICTURE_pos =  "C:/Python27/coin_svm/pos"
def get_pos():
        for name in glob(PICTURE_pos + "\\*.jpg"):
            img = Image.open(name)
            img= img.convert('L')
            img = list(img.getdata())
            all_data_set.append(img)
            all_data_label.append(1)
get_pos()
PICTURE_neg =  "C:/Python27/coin_svm/neg"
def get_neg():
    label = 1
    if (label <= 6): #
        for name in glob(PICTURE_neg + "\\*.jpg"):
            img = Image.open(name)
            img= img.convert('L')
            img = list(img.getdata())
            all_data_set.append(img)
            all_data_label.append(0)
            label += 1
get_neg()
PICTURE_test =  "C:/Python27/coin_svm/test"
test=[]
def get_test():
        for name in glob(PICTURE_test + "\\*.jpg"):
            img = Image.open(name)
            img= img.convert('L')
            img = list(img.getdata())
            test.append(img)
get_test()



X = np.array(all_data_set)
Y = np.array(all_data_label)
test=np.array(test)
#=================SVM================#
clf = svm.SVC()
clf.fit(X, Y)
clf.predict(test)