import cv2
import datetime


a=cv2.VideoCapture(0)
a.set(3,1280)
a.set(4,720)
print(a.isOpened())
while (a.isOpened()):
    ret,frame=a.read()
    b=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    date='WIDTH='+str(a.get(3))+'HEIGHT='+str(a.get(4))
    font=cv2.FONT_HERSHEY_SIMPLEX
    frame=cv2.putText(frame,date,(10,50),font,1,(0,0,255),1,cv2.LINE_AA)
    cv2.imshow('frame',b)
    if cv2.waitKey(1) & 0xFF==ord('q' or 'Q'):
        break

a.release()
cv2.destroyAllWindows()
