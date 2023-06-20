# from IPython.display import Image as show_image
# show_image(filename="runs/segment/train9/val_batch0_labels.jpg")
import cv2

imgTrain = cv2.imread('runs/segment/train10/val_batch0_labels.jpg')
imgTest = cv2.imread('runs/segment/train10/val_batch0_pred.jpg')
imgResults = cv2.imread('runs/segment/train10/results.png')

cv2.imshow('Train_result',imgTrain)
cv2.imshow('Test_result',imgTest)
cv2.imshow('graph_result',imgResults)

cv2.waitKey(0)
