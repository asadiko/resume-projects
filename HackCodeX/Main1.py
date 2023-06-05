import numpy as np
import mediapipe as mp
from Function import *
from flask import Flask, render_template, request, session, Response
import json

app = Flask(__name__)
holy_hands = mp.solutions.hands

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(process_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

def process_video():
    cap = cv.VideoCapture(0)
    with holy_hands.Hands(max_num_hands=2) as hands:
        index_cord = []
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            image.flags.writeable = False
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = hands.process(image)
            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            imgH, imgW = image.shape[:2]
            string = ""
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    hand_cordinate = []
                    for index, landmark in enumerate(hand_landmarks.landmark):
                        x_cordinate, y_cordinate = int(landmark.x * imgW), int(landmark.y * imgH)
                        hand_cordinate.append([index, x_cordinate, y_cordinate])
                    hand_cordinate = np.array(hand_cordinate)
                    string = persons_input(hand_cordinate)
                    image = get_fram(image, hand_cordinate, string)
            if string == " D":
                index_cord.append([15, hand_cordinate[8][1], hand_cordinate[8][2]])
            if string == " I" or string == " J":
                index_cord.append([15, hand_cordinate[20][1], hand_cordinate[20][2]])
            for val in index_cord:
                image = cv.circle(image, (val[1], val[2]), val[0], (255, 255, 255), 1)
                val[0] = val[0] - 1
                if val[0] <= 0:
                    index_cord.remove(val)
            ret, frame = cv.imencode('.jpg', cv.flip(image, 1))
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
            

            

if __name__ == '__main__':
    app.run(debug=True)
