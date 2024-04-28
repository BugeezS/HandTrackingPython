import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)
while webcam.isOpened():
    success, image = webcam.read()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hands.Hands().process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks,connections=mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Webcam Hands', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
