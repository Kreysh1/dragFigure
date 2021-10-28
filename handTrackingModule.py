import cv2 as cv
import mediapipe as mp

class HandDetector():
    def __init__(self, mode=False, maxHands=2, modelComplex=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComplex,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    #•Detecta que hay manos en la imagen
    def findHands(self, img, draw = True):
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    #•Detecta la posicion de las manos en la imagen
    #•Guarda las LandMarks en un array
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape   
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw and id==4:
                    cv.circle(img, (cx, cy), 10, (255,0,255), cv.FILLED)

        return lmList

def main():
    cam = cv.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cam.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cv.imshow("Image", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()