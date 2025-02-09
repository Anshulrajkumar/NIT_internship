import cv2
import numpy as np
from matplotlib import pyplot as pp

a=cv2.VideoCapture(0)
print(a.isOpened())
while (a.isOpened()):
    ret,img=a.read()
    _,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
    kernal=np.ones((5,5), np.uint8)
    dilation=cv2.dilate(img,kernal,iterations=2)
    erosion=cv2.erode(img,kernal,iterations=1)
    opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
    closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
    gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)
    tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernal)
    titles=['image','mask','dilation','erosion','opening','closing','gradient','tophat']
    images=[img,mask,dilation,erosion,opening,closing,gradient,tophat]
    for i in range(8):
        cv2.imshow(titles[i],images[i])
    if cv2.waitKey(1) & 0xFF==ord('q' or 'Q'):
        break



for i in range(8):
        pp.subplot(2,4,i+1),pp.imshow(images[i],'gray')
        pp.title(titles[i])
        pp.xticks([]),pp.yticks([])



pp.show()

