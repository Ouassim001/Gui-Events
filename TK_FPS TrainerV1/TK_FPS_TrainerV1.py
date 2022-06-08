from operator import mod, truediv
from tkinter import * 
import time
from unittest import mock

window = Tk()
window.title("FPS TrainerV1")
window.geometry("500x500")

windowlabel= Label(window,
text="FPS TrainerV1",
font=("helvetica",20),
fg="#0049b8")
windowlabel.pack


# hieronder defs
def pressW(event):
    if ButtonW == True:
        ButtonW.config(text="Clicked!")
    scoreLabel.config(text="score " + str(10))
    ButtonW.destroy()


def pressA(event):
    if ButtonA == True:
        ButtonA.config(text="Clicked!")
    scoreLabel.config(text="score " + str(20))
    ButtonA.destroy()


def pressS(event):
    if ButtonS == True:
        ButtonS.config(text="Clicked!")
    scoreLabel.config(text="score " + str(30))
    ButtonS.destroy()


def pressD(event):
    if ButtonD == True:
        ButtonS.config(text="Clicked!")
    scoreLabel.config(text="score " + str(40))
    ButtonD.destroy()


def pressSPACE(event):
    if ButtonSpace == True:
        ButtonS.config(text="Clicked!")
    scoreLabel.config(text="score " + str(50))
    ButtonSpace.destroy()




def Timer():
    buttonTime.destroy()

    ButtonW.place(x=20, y=40)
    ButtonA.pack(side=TOP, padx=50, pady=20)
    ButtonS.pack(side=BOTTOM, padx=50, pady=20)
    ButtonD.pack(side=BOTTOM, padx=50, pady=50)
    ButtonSpace.pack(side=RIGHT, padx=50, pady=20)


    window.bind("<d>", pressD)

    for x in range(19,-1, -1):
        countdownLabel["text"] = "nog", x , "seconds"
        window.update()
        time.sleep(1)





# hieronder Buttons
window.bind("<w>", pressW)
ButtonW = Button(window,
               text=("PRESS W"),
               font=("helvetica", 15),
               bg="#0041ab",
               command=pressW)


window.bind("<a>", pressA)
ButtonA = Button(window,
               text=("PRESS A"),
               font=("helvetica", 15),
               bg="#2968cf",
               command=pressA)
    

window.bind("<s>", pressS)
ButtonS = Button(window,
               text=("PRESS S"),
               font=("helvetica", 15),
               bg="#2968cf",
               command=pressS)
    

window.bind("<d>", pressD)       
ButtonD = Button(window,
               text=("PRESS D"),
               font=("helvetica", 15),
               bg="#2ba3ff",
               command=pressD)


window.bind("<space>", pressSPACE)
ButtonSpace = Button(window,
               text=("PRESS space"),
               font=("helvetica", 15),
               bg="#2ba6ff",
               command=pressSPACE)






# hieronder timer button
buttonTime = Button(window,
                    text="Start",
                    bg="#21b6db",
                    command=Timer)
buttonTime.pack(side=TOP, padx=50, pady=50)


# hieronder countdownlabel
countdownLabel = Label(window, text="Nog 20 seconden",
                       bg="powder blue")
countdownLabel.place(x=400, y=10)


# hieronder score label 
scoreLabel = Label(window,
                   text="score: " + str(0),
                   bg="powder blue")
scoreLabel.place(x=10, y=10)








window.mainloop()