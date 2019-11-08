##Scan Qr and open image file

import cv2

import pyzbar.pyzbar as pyzbar



qrData=""
font=cv2.FONT_HERSHEY_COMPLEX_SMALL


cap =cv2.VideoCapture(0)
i=0
flag=True

strs = ["" for x in range(4)]
while True:
    _,frame=cap.read()

    decodedObject = pyzbar.decode(frame)
    for obj in decodedObject:
         qrData=obj.data
         flag=False


    cv2.putText(frame,str(qrData),(100,100),font,1,(255,200,0),2)
    #print (qrData)


    cv2.imshow("frame",frame)

    key=cv2.waitKey(1)
    ##turn of the scanner when press to 0
    if key==48 or flag==False:
        break

print(qrData)
data = qrData.split()
print("---------------------------------------------------")

##parse the path of the image and open
img=(data[4][5:])

print(img)
from PIL import Image


im = Image.open(img)


im.show()
