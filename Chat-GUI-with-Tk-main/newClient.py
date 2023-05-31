# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:48:56 2019

@author: CSE
"""

from socket import *                             # for networking  
from _thread import *                            #to use threads for every client
from tkinter import *

window=Tk()
window.title("Welcome to The World chat")
window.geometry("860x420")
#gui set up 
#first frames
Frame1 = Frame(window)
Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 1,sticky = S+E+W)

Frame2 = Frame(window)
Frame2.grid(row = 0, column = 1, rowspan = 5, columnspan = 3,sticky = S+E+W)

Frame3 = Frame(window)
Frame3.grid(row = 5, column = 1, rowspan = 1, columnspan = 3,sticky = S+E+W)

#------------------------------------------------------------------------------
# set up connection part
s_label=Label(Frame1, text="Server_IP")
p_label=Label(Frame1, text=" Server_Port")
u_label=Label(Frame1, text="Username")
server = Entry(Frame1)
server.insert(0,'127.0.0.1')
portt = Entry(Frame1)
portt.insert(0,'12221')
user = Entry(Frame1)
user.insert(0,'CSE')
#------------------------------------------------------------------------------
s_label.grid(row=0,column=0)
p_label.grid(row=1,column=0)
u_label.grid(row=2,column=0)
server.grid(row=0,column=1,columnspan=2)
portt.grid(row=1,column=1,columnspan=2)
user.grid(row=2,column=1,columnspan=2)
#----------------------------------------------------------------------------
sock = socket((AF_INET), SOCK_STREAM)            #create socket object with socket diagram type using tcp
username =""
def connect():                                   #define connect method
    global username
    host = server.get()
    temp = portt.get()
    username = user.get()
    port = int(temp)
    sock.connect((host, port))
    start_new_thread(recievingMSG, (sock,))
connect = Button(Frame1,text="Connect",command=connect )#connect)
connect.grid(row=3,column=1)
#------------------------------------------------------------------------------

# set up chat area
chat = Text(Frame2)
chat.pack(side="left")

#------------------------------------------------------------------------------
# set up message area
msg = Entry(Frame3)
msg.pack(side="left",expand=1,fill="both")

#------------------------------------------------------------------------------
#send button function
def sendButton():
     global username 
     message = msg.get()
     finMessage =username + "-> " + message
     sock.send(message.encode())
     chat.insert(END,finMessage)
     chat.insert(END,"\n")
     msg.delete(0, END)
send = Button(Frame3,text="send",bg="Aqua", fg="Black",width=2,height=1,font=('courier','12'),command=sendButton )#connect)
send.pack(side="left",expand=1,fill="x")

#------------------------------------------------------------------------------
def recievingMSG(sock):
    while True:
        recievedMsg = sock.recv(1024).decode()
        finrecievedMsg = recievedMsg + "\n"
        chat.insert(END,finrecievedMsg)
#------------------------------------------------------------------------------
     
     
window.mainloop()