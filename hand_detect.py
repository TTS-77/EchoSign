import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    gesture_text = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            # Finger states
            index_up = landmarks[8].y < landmarks[6].y
            middle_up = landmarks[12].y < landmarks[10].y
            ring_up = landmarks[16].y < landmarks[14].y
            pinky_up = landmarks[20].y < landmarks[18].y
            thumb_up = landmarks[4].y < landmarks[3].y

            thumb_index_dist = distance(landmarks[4], landmarks[8])
            thumb_middle_dist = distance(landmarks[4], landmarks[12])
            index_middle_dist = distance(landmarks[8], landmarks[12])

            # ---------- OK ----------
            if thumb_index_dist < 0.05 and not middle_up:
                gesture_text = "OK"

            # ---------- F ----------
            elif thumb_index_dist < 0.05 and middle_up and ring_up and pinky_up:
                gesture_text = "F"

            # ---------- YES ----------
            elif thumb_up and not index_up and not middle_up and not ring_up and not pinky_up:
                gesture_text = "YES"

            # ---------- NO ----------
            elif not index_up and not middle_up and not ring_up and not pinky_up:
                gesture_text = "NO"

            # ---------- STOP ----------
            elif index_up and middle_up and ring_up and pinky_up and thumb_up:
                gesture_text = "STOP"

            # ---------- I ----------
            elif pinky_up and not index_up and not middle_up and not ring_up:
                gesture_text = "I"

            # ---------- U ----------
            elif index_up and middle_up and not ring_up and not pinky_up and index_middle_dist < 0.06:
                gesture_text = "U"

            # ---------- LOVE ----------
            elif thumb_up and index_up and pinky_up and not middle_up and not ring_up:
                gesture_text = "LOVE"

            # ---------- L ----------
            elif index_up and thumb_up and not middle_up and not ring_up and not pinky_up:
                gesture_text = "L"
                
    if gesture_text != "":
        cv2.putText(frame, gesture_text, (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5, (0, 255, 0), 3)

    cv2.imshow("Sign Language Translator", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()