#!/usr/bin/python
#Author : Antonio Taboada
#Date: 08/08/2016
#Filename: citadeldia.py
#Purpose : Conecta por UDP puerto 17 a servidor QOTD y muestra la cita del dia

import sys
import socket  
import errno

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print "Usage: " , sys.argv[0] , " <hostname> "
    exit(0)
elif len(sys.argv) == 2:
    hostname = sys.argv[1]
    try:
        host=socket.gethostbyname(hostname)
    except:
        print "hostname no valido"
        exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 17
s.sendto(" ", (host, port))
d = s.recvfrom(1024)
reply = d[0]
addr = d[1]
print reply
