from tkinter import *
# splashscreen start
splash_win = Tk()
splash_win.title("Start Screen FPS Trainer")
splash_win.geometry("400x400")
splash_win.config(bg=("#b8d9e0"))
splash_win.overrideredirect(True)  # gets rid of borders
splash_label = Label(splash_win,
                    text="Welcome to FPS TrainerV1",
                    bg="#b8d9e0",
                    fg="#0049b8",
                    font=("helevtica",20))
splash_label.pack()                                
# splashscreen ending  