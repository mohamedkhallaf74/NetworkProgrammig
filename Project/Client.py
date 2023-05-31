#client
from tkinter import*
from tkinter import messagebox 
import nltk
from nltk.corpus import words

from time import gmtime, strftime
import time
from collections import Counter 
from socket import*
from _thread import start_new_thread

x= ""

def receiveThread(s):
    global x
    while True:
        x =s.recv(500).decode("UTF-8")
        x=int(x)
        label['text'] = "Your score is: " + str(score1) + "\nYour opponent's score is: "+str(x);
       

def sendFunction(score1):
    s.send(str(score1).encode('UTF-8'))

    
nltk.download('words')
word_list=words.words()
Matrix_list=['a','r','b','z','t','n','d','h','m','v','s','x','l','u','g','y','p','k','c','o']
score1=0;

window=Tk()
window.title("Player 2 Words")
window.geometry("600x500")

def checkspells():
    global score1
    word = word_check.get();
    if word in word_list:
        dict=Counter (word)
        flag=1
        for key in dict.keys():
            if key not in Matrix_list:
                flag = 0
        if flag==1 and len(word) > 3:
            score1=score1+len(word)
            label['text']="Your score is: "+str(score1)+"in Your opponent's is: "+str(x) 
            print(word)
        else:
            messagebox.showinfo("check", "No matchine with above character OR word length should be greater than 3") 
    else:   
        print("No word")
    sendFunction(score1)
    word_check.delete(0, 'end')

def tick(time1=''):
    time2 = time.strftime("%M:%S")
    if time2 != time1:
        time1 = time2
        timer.config(text="After 1 minute it will close automatically " + time2)
    timer.after(200, tick)

def quit_pro():
    global x
    if x > score1:
        messagebox.showinfo("Player 2: You lost", "You lost. Your opponent scored: " + str(x) + "\nYour score is: " + str(score1))
    elif x == score1:
        messagebox.showinfo("Player 2: Game is Drawn", "Game is Drawn. Your score is: " + str(score1) + "\nYour opponent's score is: " + str(x))
    else:
        messagebox.showinfo("Player 2: You won", "You won. Your score is: " + str(score1) + "\nYour opponent's score is: " + str(x))
    window.destroy()

btn1 = Button(window, text="A", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="R", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="B", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="Z", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="T", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=1)

btn1 = Button(window, text="N", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn1.grid(column=1, row=2)
btn2 = Button(window, text="D", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=2)
btn3 = Button(window, text="H", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=2)
btn4 = Button(window, text="M", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=2)
btn5 = Button(window, text="V", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=2)

btn1 = Button(window, text="S", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn1.grid(column=1, row=3)
btn2 = Button(window, text="X", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=3)
btn3 = Button(window, text="L", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=3)
btn4 = Button(window, text="U", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=3)
btn5 = Button(window, text="G", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=3)

btn1 = Button(window, text="Y", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn1.grid(column=1, row=4)
btn2 = Button(window, text="P", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=4)
btn3 = Button(window, text="K", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=4)
btn4 = Button(window, text="C", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=4)
btn5 = Button(window, text="O", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=4)

word_check = Entry(window, width=50)
word_check.grid(row=5, column=0, columnspan=6)
btncheck = Button(window, text="OK", bg="black", fg="white", width=5, height=2, font=("Helvetica", "10"), command=checkspells)
btncheck.grid(column=10, row=5)
label = Label(window, text="Score = 0")
label.grid(column=11, row=5)
timer = Label(window, text="You have 1 minute")
timer.grid(column=0, row=6, columnspan=6)
tick()
window.after(60000, quit_pro)

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",7000))
start_new_thread(receiveThread, (s,))


window.mainloop()