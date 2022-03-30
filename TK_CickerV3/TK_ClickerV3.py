from tkinter import *
from turtle import bgcolor

window = Tk()
window.title("ClickerV3")
window.geometry("400x400")


window.count = 0
def clickUp():
    window.count+=1
    counter.config(text=window.count)
    if window.count >0:
        window.config(bg="#00e832")
    if window.count == 0:
        window.config(bg="#454545")
    

def clickDown():
    window.count-=1
    counter.config(text=window.count)
    if window.count <0:
        window.config(bg="#eb0000")
    if window.count == 0:
        window.config(bg="#454545")

def ChangeBgEnter(event):
    window.prevNum = window.cget("bg")
    window.config(bg="#b8eb00")

def ChangeBgLeave(event):
    window.config(bg=window.prevNum)

def Multiply3(event):
    window.count*=3
    counter.config(text=window.count)

def Substract3(event):
        window.count/=3
        counter.config(text=window.count)
    
    




button = Button(text="UP",
                bg="#001840",
                font=("helvetica"),
                state=ACTIVE,
                padx=100,
                pady=10,
                relief="solid",
                command="UP")
button.pack(side=TOP, padx=10, pady=10)

button2 = Button(text="DOWN",
                bg="#001840",
                state=ACTIVE,
                padx=100,
                pady=10,
                relief="solid",
                command="DOWN",)
button2.pack(side=BOTTOM, padx=10, pady=10)

button.config(command=clickUp)
button2.config(command=clickDown)

counter = Label(window,
                padx=100,
                pady=30,
                text=window.count)
counter.pack()

window.config(bg="#454545")


counter.bind("<Enter>",ChangeBgEnter)
counter.bind("<Leave>", ChangeBgLeave)

counter.bind("<Double-Button>", Multiply3)



window.mainloop()