import numpy as np
import cv2 

def nothing(x):
    pass
a=cv2.VideoCapture(0)
cv2.namedWindow('tracking')

cv2.createTrackbar('LH','tracking',0,255,nothing)
cv2.createTrackbar("LS","tracking",0,255,nothing)
cv2.createTrackbar("LV","tracking",0,255,nothing)
cv2.createTrackbar("UH","tracking",255,255,nothing)
cv2.createTrackbar("US","tracking",255,255,nothing)
cv2.createTrackbar("UV","tracking",255,255,nothing)


while True:
    _,frame=a.read()
    #frame=cv2.imread('image.jpg')
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_H=cv2.getTrackbarPos("LH","tracking")
    l_S=cv2.getTrackbarPos("LS","tracking")
    l_V=cv2.getTrackbarPos("LV","tracking")
    u_h=cv2.getTrackbarPos("UH","tracking")
    u_s=cv2.getTrackbarPos("US","tracking")
    u_v=cv2.getTrackbarPos("UV","tracking")

    l_b=np.array([l_H,l_S,l_V])
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,l_b,u_b)
    frame=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('hsv',hsv)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    
    key=cv2.waitKey(1)

    if key==27:
        break

a.release()
cv2.destroyAllWindows()