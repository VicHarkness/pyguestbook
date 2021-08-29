#!/usr/bin/env python3

import socket
import codecs

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            received=codecs.decode(data,'UTF-8')
            splitData=received.split()
            messageType=int(splitData[0])
            nickname=splitData[1]
            if messageType==1:
                f=open('logs.txt','r')
                logs=f.read()
                logs=codecs.encode(logs,'UTF-8')
                conn.sendall(logs)
            elif messageType==2:
                f=open('logs.txt','a')
                f.write(nickname+'\n')
            else:
                print("Plz no bully protocol :(")
         #   print("received from "+nickname)
         #   if not data:
          #      break
           # conn.sendall(data)
            #conn.close()
