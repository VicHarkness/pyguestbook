#!/usr/bin/env python3

import socket
import codecs

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

nickname=input("What's your name?")
print("Hi "+nickname)
action=input("Do you want to read or sign?")
if action=="read":
    messageType=1
elif action=="sign":
    messageType=2
else:
    print("wat")
messageType=str(messageType)
print(messageType)


packet=messageType+" "+nickname
packetEnc=codecs.encode(packet,'UTF-8')



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packetEnc)
    data = s.recv(1024)

print('Received', repr(data))

