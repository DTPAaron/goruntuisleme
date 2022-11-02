import cv2
import numpy as np

photo=cv2.imread("kelebek.jpg",0)
cv2.imshow("kelebekduz",photo)
cv2.waitKey()

max_photo=np.max(photo)

[h,w]=np.shape(photo)

for i in range (0,h):
    for j in range (0,w):
        photo[i,j]=max_photo-photo[i,j]

cv2.imshow("kelebekters",photo)
cv2.waitKey()