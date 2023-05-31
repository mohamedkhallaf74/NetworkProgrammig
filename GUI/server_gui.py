# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:43:41 2019

@author: CSE
"""
from tkinter import *
from tkinter import messagebox
from socket import *
import _thread
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host="127.0.0.1"
port=9000
s.bind((host,port))
s.listen(5)
wind = Tk()
wind.title('server')
wind.geometry('1000x500')
wind.configure(background='#2e59d1')
entryText =StringVar()
en=Entry(wind,width=100,textvariable=entryText)
en.grid(column=1,row=1)
btn=Button(wind,width=3,height=1,text="send")
btn.grid(column=1,row=2)
r=3
c,a=s.accept()
def rec():
    global r,s,lab
    while True:
        w=c.recv(2048)
        Button(wind,text=w.decode('utf-8'),bd=5,relief=FLAT,bg='#d12e44',padx=5,pady=5,wraplength=100).grid(column=2,row=r) 
        r=r+1
_thread.start_new_thread(rec,())
def clicked():
    global r,c,lab,entryText
    c.send((en.get()).encode('utf-8'))
    x=en.get()
    Button(wind,text=x,bd=5,relief=FLAT,bg='#d1c62e',padx=5,pady=5,wraplength=100).grid(column=0,row=r)
    entryText.set("")
    r=r+1
btn["command"]=clicked 
wind.mainloop()

   
    
    
