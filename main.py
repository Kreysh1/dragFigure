import cv2 as cv
import time
import mediapipe as mp

###### Capture Resolution ######
wCam, hCam = 1280, 720
################################

###### FPS Configuration ######
xPos, yPos = 10,40
font = cv.FONT_HERSHEY_COMPLEX
fontScale = 1.5
fontColor = [255, 0, 255]
fontThickness = 2
################################

cam = cv.VideoCapture(0)
cam.set(3, wCam)
cam.set(4,hCam)
previousTime = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands()


while True:
    success, img = cam.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    #Hand Detection
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    #Frames Per Second
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    cv.putText(img, f'FPS: {int(fps)}', (xPos,yPos), font, fontScale, fontColor, fontThickness)

    cv.imshow("Image", img)
    cv.waitKey(1)