import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('coordinate',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=[y,x,0]
        green=[y,x,1]
        red=[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        strbgr=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strbgr,(x,y),font,.5,(255,0,0),2)
        cv2.imshow('coordinate',img)


img=cv2.imread('image.jpg')
cv2.imshow('coordinate',img)
cv2.setMouseCallback('coordinate',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()