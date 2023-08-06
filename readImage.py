import cv2

image1 = cv2.imread('datasets/train/images/img_0.png',0)
image2 = cv2.imread('avc_dataset/train/images/img_1.png',0)

cv2.imshow('image1',image1)

cv2.imshow('image2',image2)

cv2.waitKey(0)