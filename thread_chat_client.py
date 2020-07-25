# 라이브러리 불러오기
from socket import *
import threading
import time

# 보내기, 받기 함수
def send(socket):
    while True:
        send_data = input('>>>')
        # encoding : 문자를 0과 1로
        socket.send(send_data.encode('utf-8'))

def receive(socket):
    while True:
        recv_data = socket.recv(1024)
        # decoding : 0과 1을 문자로
        print('\n상대방 :', recv_data.decode('utf-8'),'\n>>>', end='')

# 소켓 연결
ip = '127.0.0.1'
port = 8080

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((ip, port))

print('****접속 완료****')

# 쓰레드로 보내기와 받기
sender = threading.Thread(target=send, args=(client_socket, ))
receiver = threading.Thread(target=receive, args=(client_socket, ))

sender.start()
receiver.start()

# 프로그램이 종료되지 않도록 반복
while True:
    time.sleep(1)
    pass





                      
