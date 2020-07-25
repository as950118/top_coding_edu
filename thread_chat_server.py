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

# 소켓 연결 대기
ip = ''
port = 8080

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(1)
print('****접속 대기중****')

# 소켓 연결
conn_socket, addr = server_socket.accept()

# 쓰레드로 보내기와 받기
sender = threading.Thread(target = send, args=(conn_socket, ))
receiver = threading.Thread(target = receive, args=(conn_socket, ))

sender.start()
receiver.start()

# 프로그램이 종료되지 않도록 반복
while True:
    time.sleep(1)
    pass





                      
