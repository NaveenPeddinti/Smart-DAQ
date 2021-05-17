#!/usr/bin/env python3

import socket
import errno
from socket import error as socket_error

def checkDAQinNetwork(HOST = '127.0.0.1', PORT = 23):
    data =""
    isConnected = False
    print("HOST =", HOST)
    print("PORT =", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            #s.sendall(b'$ADC#')
            isConnected = True
            s.settimeout(1.0)
            #data = s.recv(1024)
            #s.settimeout(None)
        except socket_error as serr:
            print ("socket error: {}".format(serr))
            isConnected = False
    s.close()
    print('Received', repr(data))
    return isConnected


def getDAQReadings(HOST = '127.0.0.1', PORT = 23):
    data =""
    print("HOST =", HOST)
    print("PORT =", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.sendall(b'$ADC#')
            s.settimeout(1.0)
            data = s.recv(1024)
            s.settimeout(None)
        except socket_error as serr:
            print ("socket error: {}".format(serr))
            data = "Error"
    print('Received', repr(data))
    s.close()
    return data
