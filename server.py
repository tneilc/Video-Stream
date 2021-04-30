import cv2
import socket
import pickle
import base64

HOST = '192.168.1.27' 
PORT = 9999 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen()
conn,addr = socket.accept()
print(conn)


while True:
    try:
        datas = conn.recv(1000000)   
        datas = base64.b64decode(datas)
        frame = pickle.loads(datas)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        cv2.imshow("deneme", frame)
        cv2.waitKey(1)
    except:
        continue
