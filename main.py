import cv2 as cv
import time
import mediapipe as mp
import handTrackingModule as htm
from PIL import ImageColor

###### Capture Resolution ######
wCam, hCam = 1280, 720
################################

###### FPS Configuration ######
xPos, yPos = 10,40
font = cv.FONT_HERSHEY_COMPLEX
fontScale = 1.5
fontColor = ImageColor.getcolor("#9400D3", "RGB")
fontThickness = 2
previousTime = 0
################################

cam = cv.VideoCapture(0)
cam.set(3, wCam)
cam.set(4,hCam)

detector = htm.HandDetector()

while True:
    success, img = cam.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    #Frames Per Second
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    cv.putText(img, f'FPS: {int(fps)}', (xPos,yPos), font, fontScale, fontColor, fontThickness)

    cv.imshow("Image", img)
    cv.waitKey(1)