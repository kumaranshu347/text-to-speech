from tkinter import *
import pyttsx3
engine = pyttsx3.init()
win = Tk()
win.title("Suno Sirf Apne DIL Kii")
win.configure(bg="yellow")
win.geometry("420x200")
def speak():
    engine.say(text.get())
    engine.runAndWait()
    engine.stop()


#label frame
lf = LabelFrame(win,text="text to speech",font="30",bd=5,bg="skyblue")
lf.pack(fill="both",expand="yes",padx=10,pady=10)
Label(lf,text="Text",font="30",padx=15).pack(side=LEFT)
#entry---user enter his/her text
text = StringVar()
Entry(lf,width=25,bd=5,font=20,textvariable=text).pack(side=LEFT,padx=10)

#button
Button(lf,text="Speech",font=15,command=speak).pack(side=LEFT)
mainloop()
