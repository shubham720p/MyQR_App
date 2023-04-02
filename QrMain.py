import qrcode
import tkinter
from tkinter import *
from tkinter import Tk , ttk
from urllib.parse import urlparse


def makeQr():
    img = qrcode.make(url.get())
    img.save(f'./{url}.png')
    img.show()

def clear():
    url.delete(0, END)
   

col1 = "white"
col2 = "red"
col3 = "violet"
f1 = "blue"
root = Tk()
root.title("Personal Speaker")
root.geometry("300x150")
root.resizable(height = False , width = False)
# upper frame
frame_up = Frame(root , width = 720 , height = 70 , bg =col3)
frame_up.grid(row = 0 , column = 0)
heading = Label (frame_up , text = "Enter Link for QR-Code", bg = col3 , fg ="black",font =("ivy 20 italic") )
heading.place(x = 0, y = 10)
line = Label(frame_up,  width =380,text = "" , height = 1 , bg = col2 ,  anchor = "nw")
line.place(x = 0 , y = 65)
# framedown
frame_down = Frame(root , width = 720 , height = 480, bg =col1 )
url = Entry(frame_down,width = 38 , justify = "center" , font=("arial  10") , highlightthickness=2)
url.place(x = 10 , y = 10)
frame_down.grid(row = 1, column = 0)
# Attendence Button
btn_speak = Button(frame_down , text ="Get_QR", width = 15  , fg = "black", command = makeQr)
btn_speak.place(x = 15, y =50)
btn_clear = Button(frame_down , text ="Clear", width = 15  , fg = "black", command = clear)
btn_clear.place(x = 175, y =50)
text = Label(frame_down,text="THANKS!✌️" , bg = col1)
text.place(x=350,y=50)
root.mainloop()