import cv2

a=cv2.imread('image.jpg',0)
cv2.imshow('image',a)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('new_image.jpg',a)
    cv2.destroyAllWindows()
