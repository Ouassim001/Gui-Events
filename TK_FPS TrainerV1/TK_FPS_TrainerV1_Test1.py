from tkinter import *
import time
from turtle import up
# from tkinter import scrolledtext


window = Tk()
window.title("FPS TrainerV1")
window.geometry("800x500")

windowlabel= Label(window,
text="FPS TrainerV1",
font=("helvetica",20),
fg="#0049b8")
windowlabel.pack







countdownLabel = Label(window, text="Nog 20 seconden")
countdownLabel.pack()


def updateCountdown():
    global count 
    countdownLabel['text'] = text=("Nog 19 seconds")

window.after(1000,updateCountdown)

def updateCountdown2():
    global count 
    countdownLabel['text'] = text=("Nog 18 seconds")
window.after(2000,updateCountdown2)

def updateCountdown3():
    global count 
    countdownLabel['text'] = text=("Nog 17 seconds")
window.after(3000,updateCountdown3)

def updateCountdown4():
    global count 
    countdownLabel['text'] = text=("Nog 16 seconds")
window.after(4000,updateCountdown4)

def updateCountdown5():
    global count 
    countdownLabel['text'] = text=("Nog 15 seconds")
window.after(5000,updateCountdown5)

def updateCountdown6():
    global count 
    countdownLabel['text'] = text=("Nog 14 seconds")
window.after(6000,updateCountdown6)

def updateCountdown7():
    global count 
    countdownLabel['text'] = text=("Nog 13 seconds")
window.after(7000,updateCountdown7)

def updateCountdown8():
    global count 
    countdownLabel['text'] = text=("Nog 12 seconds")
window.after(8000,updateCountdown8)

def updateCountdown9():
    global count 
    countdownLabel['text'] = text=("Nog 11 seconds")
window.after(9000,updateCountdown9)

def updateCountdown10():
    global count 
    countdownLabel['text'] = text=("Nog 10 seconds")
window.after(10000,updateCountdown10)

def updateCountdown11():
    global count 
    countdownLabel['text'] = text=("Nog 9 seconds")
window.after(11000,updateCountdown11)

def updateCountdown12():
    global count 
    countdownLabel['text'] = text=("Nog 8 seconds")
window.after(12000,updateCountdown12)

def updateCountdown13():
    global count 
    countdownLabel['text'] = text=("Nog 7 seconds")
window.after(13000,updateCountdown13)

def updateCountdown14():
    global count 
    countdownLabel['text'] = text=("Nog 6 seconds")
window.after(14000,updateCountdown14)

def updateCountdown15():
    global count 
    countdownLabel['text'] = text=("Nog 5 seconds")
window.after(15000,updateCountdown15)

def updateCountdown16():
    global count 
    countdownLabel['text'] = text=("Nog 4 seconds")
window.after(16000,updateCountdown16)

def updateCountdown17():
    global count 
    countdownLabel['text'] = text=("Nog 3 seconds")
window.after(17000,updateCountdown17)

def updateCountdown18():
    global count 
    countdownLabel['text'] = text=("Nog 2 seconds")
window.after(18000,updateCountdown18)

def updateCountdown19():
    global count 
    countdownLabel['text'] = text=("Nog 1 seconds")
window.after(19000,updateCountdown19)

def updateCountdown20():
    global count 
    countdownLabel['text'] = text=("Time's Up")
window.after(20000,updateCountdown20)



# hieronder new label 
scoreLabel = Label(window, text="score: " + str(0), bg="powder blue")
scoreLabel.place(x=10, y=10)


def pressW(event):
    ButtonW.config(text="Clicked!")
    scoreLabel.config(text="score " + str(10))

window.bind("<w>", pressW)

ButtonW = Button(window,
               text=("PRESS W"),
               font=("helvetica", 15),
               bg="#0041ab")
ButtonW.pack(side=RIGHT, padx=20, pady=50)


def pressA(event):
    ButtonA.config(text="Clicked!")
    scoreLabel.config(text="score " + str(20))

window.bind("<a>", pressA)

ButtonA = Button(window,
               text=("PRESS A"),
               font=("helvetica", 15),
               bg="#2968cf")
ButtonA.pack(side=TOP, padx=50, pady=20)


def pressS(event):
    ButtonS.config(text="Clicked!")
    scoreLabel.config(text="score " + str(30))

window.bind("<s>", pressS)

ButtonS = Button(window,
               text=("PRESS S"),
               font=("helvetica", 15),
               bg="#2968cf")
ButtonS.pack(side=BOTTOM, padx=50, pady=20)


def pressD(event):
    ButtonS.config(text="Clicked!")
    scoreLabel.config(text="score " + str(40))

window.bind("<d>", pressD)

ButtonD = Button(window,
               text=("PRESS D"),
               font=("helvetica", 15),
               bg="#2ba3ff")
ButtonD.pack(side=BOTTOM, padx=50, pady=50)


def pressSPACE(event):
    ButtonS.config(text="Clicked!")
    scoreLabel.config(text="score " + str(50))

window.bind("<space>", pressSPACE)
ButtonSpace = Button(window,
               text=("PRESS space"),
               font=("helvetica", 15),
               bg="#2ba6ff",
               command= lambda:ButtonSpace.destroy())
ButtonSpace.pack(side=TOP, padx=50, pady=50)
ButtonSpace.place(x=100, y=20)



















window.mainloop()