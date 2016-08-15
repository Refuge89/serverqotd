#!/usr/bin/python
#Author : Antonio Taboada
#Date: 08/08/2016
#Filename: serverqotd.py
#Purpose : Simple servidor de QUOTE OF THE DAY "Frase del dia" en UDP puerto 17;

import socket
import sys

#Variable HOST = IP por defecto localhost 127.0.0.1;  
HOST = 'localhost'  
PORT = 17
 
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Abierto puerto UDP:', PORT
except socket.error, msg :
    print 'Error al abrir el puerto. Codigo de error : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Servidor QOTD Activo!! IP:', HOST
 
while 1:

    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
#Aqui ponemos la frase del dia:     
    reply = 'Frase del dia... (c) 2016 hackingyseguridad.com ' + data
     
    s.sendto(reply , addr)
    print '[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
s.close()
