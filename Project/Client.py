from tkinter import *
from tkinter import messagebox
from time import strftime
import time
from socket import *
from _thread import start_new_thread

word_list = []
Matrix_list = ['a', 'r', 'b', 'z', 't', 'n', 'd', 'h', 'm', 'v', 's', 'x', 'l', 'u', 'g', 'y', 'p', 'k', 'c', 'o']
score = 0

window = Tk()
window.title("Player 2 Words")
window.geometry("600x500")
x = ""
c = None

def receiveThread():
    global x
    while True:
        try:
            x = int(c.recv(500).decode("UTF-8"))
            label['text'] = "Your score is: " + str(score) + "\nYour opponent's score is: " + str(x)
        except ValueError:
            pass

def sendFunction(score):
    c.send(str(score).encode("UTF-8"))

def checkspells():
    global score
    word = word_check.get()

    if word in word_list:
        word_counter = Counter(word)
        flag = all(key in Matrix_list for key in word_counter.keys())
        if flag and len(word) > 3:
            score += len(word)
            label['text'] = "Your score is: " + str(score) + "\nYour opponent's score is: " + str(x)
            print(word)
        else:
            messagebox.showinfo("Check", "No match with the given characters or word length should be greater than 3")
    else:
        print("No word")
    sendFunction(score)
    word_check.delete(0, 'end')

def tick(timel=''):
    time2 = time.strftime("%M:%S")
    if time2 != time1:
        timel = time2
        timer.config(text="After 1 minute it will close automatically " + time2)
    timer.after(200, tick)

def quit_pro():
    if x > score:
        messagebox.showinfo("Player 2: You lost", "You lost. Your opponent scored: " + str(x) + "\nYour score is: " + str(score))
    elif x == score:
        messagebox.showinfo("Player 2: Game is Drawn", "Game is Drawn. Your score is: " + str(score) + "\nYour opponent's score is: " + str(x))
    else:
        messagebox.showinfo("Player 2: You won", "You won. Your score is: " + str(score) + "\nYour opponent's score is: " + str(x))
    window.destroy()

btn1 = Button(window, text="A", bg="pink", fg="white", width=3, height=1, font=("Helvetica", 20))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="R", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="B", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="2", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="T", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=1)

btn1 = Button(window, text="N", bg="pink", fg="white", width=3, height=1, font=("Helvetica", 20))
btn1.grid(column=1, row=2)
btn2 = Button(window, text="D", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=2)
btn3 = Button(window, text="H", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=2)
btn4 = Button(window, text="M", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=2)
btn5 = Button(window, text="V", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=2)

btn1 = Button(window, text="S", bg="pink", fg="white", width=3, height=1, font=("Helvetica", 20))
btn1.grid(column=1, row=3)
btn2 = Button(window, text="X", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn2.grid(column=2, row=3)
btn3 = Button(window, text="L", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn3.grid(column=3, row=3)
btn4 = Button(window, text="U", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn4.grid(column=4, row=3)
btn5 = Button(window, text="G", bg="pink", fg="white", width=3, height=1, font=("Helvetica", "20"))
btn5.grid(column=5, row=3)

btn1 = Button(window, text="Y", bg="pink", fg="white", width=3, height=1, font=("Helvetica", 20))
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
btncheck = Button(window, text="OK", bg="black", fg="white", width=5, height=1, font=("Helvetica", "20"), command=checkspells)
btncheck.grid(column=10, row=5)
label = Label(window, text="Score 0")
label.grid(column=11, row=5)
timer = Label(window, text="You have 1 minute")
timer.grid(column=6, row=6, columnspan=6)
tick()
window.after(60000, quit_pro)

s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.connect((host, port))

start_new_thread(receiveThread, ())
window.mainloop()