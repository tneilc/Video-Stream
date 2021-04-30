import cv2
import pyautogui
import numpy as np
import socket
import pickle
import base64

HOST = '192.168.1.27' 
PORT = 9999  


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))



def getframeandsend():
    screen = pyautogui.screenshot()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (1024, 576), interpolation=cv2.INTER_AREA)
    return frame

while True:
    
    frame = getframeandsend()
    istrue , tosend = cv2.imencode(".jpg",frame,[int(cv2.IMWRITE_JPEG_QUALITY), 90])
    data = pickle.dumps(tosend)
    tosend = base64.b64encode(data)
    size = len(data)
    socket.send(tosend)

    