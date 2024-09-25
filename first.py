import cv2
import mediapipe as mp
import pyfirmata2
import math
import time

board = pyfirmata2.Arduino('COM5')
ledpin = board.get_pin("d:9:p")
cap=cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)

# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands
hand=mp_hands.Hands(max_num_hands=1)

while True:
 sucess,frame=cap.read()
 if sucess:
    RGB_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hand.process(RGB_frame)
    if result.multi_hand_landmarks:
       handLandmarks = result.multi_hand_landmarks[0]
       thumbTip=handLandmarks.landmark[4]
       indexTip=handLandmarks.landmark[8]
       distance = math.sqrt((thumbTip.x-indexTip.x)**2+(thumbTip.y-indexTip.y)**2)
       print(distance)
       ledpin.write(distance)
       #cv2.line(frame,(thumbTip.x,thumbTip.y),(indexTip.x,indexTip.y),(255,0,0),3)
       for hand_landmarks in result.multi_hand_landmarks:
        mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
   # 
    cv2.imshow("capture",frame)
    if cv2.waitKey(1)==ord('q'):
      break

cv2.destroyAllWindows()

ledpin.write(0)
board.exit()