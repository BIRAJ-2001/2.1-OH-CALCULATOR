import cv2
import mediapipe as mp
import time
import protobuf_to_dict as ptd

class HandDetect():
    def __init__(self, mode= False, maxhands=2, complexity=1, detectioncon=0.5, trackingcon=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.complexity = complexity
        self.detectioncon = detectioncon
        self.trackingcon = trackingcon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxhands, self.complexity, self.detectioncon, self.trackingcon)
        self.mpdraw = mp.solutions.drawing_utils


    def findhands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS, self.mpdraw.DrawingSpec((255, 0, 0)),
                                      self.mpdraw.DrawingSpec((255, 255, 0)))
        return img


    def findpos(self, img, handno=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(hand.landmark):
                   h, w, c = img.shape
                   cx, cy = int(lm.x * w), int(lm.y * h)
                   lmlist.append([id, cx, cy])
                   if draw:
                       cv2.circle(img, (cx,cy), 10,(255,255,255), -1)
                       #cv2.putText(img, str(lmlistL[id][0]), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                       self.mpdraw.draw_landmarks(img, hand, self.mpHands.HAND_CONNECTIONS,
                                                   self.mpdraw.DrawingSpec((255, 0, 0)),
                                                   self.mpdraw.DrawingSpec((255, 255, 0)))
        return lmlist


def main():
    cam = cv2.VideoCapture(1)
    pt = 0
    detector = HandDetect()
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (960, 540))
        img = detector.findhands(img)
        lmlist= detector.findpos(img)
        print (len(lmlist))
        ct = time.time()
        fps = 1 / (ct - pt)
        pt = ct
        cv2.putText(img, str(int(fps)), (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 155, 0), 2)
        cv2.imshow("image", img)
        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()