# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:43:20 2019

@author: CSE
"""

from socket import *                             # for networking  
from _thread import *                            #to use threads for every client


host = '127.0.0.1'                               #loop back address
port = 12221                                     #pick any free port on the computer 
clients = []

sock = socket((AF_INET), SOCK_STREAM)            #create socket object with socket diagram type using udp
sock.bind((host, port))                          #bind to host and port
sock.listen(20)                                  #listen for connections
print("server is running...")
print("server ip is " + host)
print("server port is "+ str(port))

                                                #define of recieving behavior
def recieving(conn , addr):
    while True:
        msg = str(addr[1]) + "-> " + conn.recv(2048).decode()
        
        for client in clients:
            if client != conn:
                client.send(msg.encode())

while True:
    conn, addr = sock.accept()
    print(str(addr[1]) + " joined the room " )
    msg = "connection from "+ str(addr[1]) + " established \n"
    for client in clients:
            client.send(msg.encode())
    clients.append(conn)
    start_new_thread(recieving, (conn, addr))
    



