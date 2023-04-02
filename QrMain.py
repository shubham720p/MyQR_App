import qrcode
import tkinter
from tkinter import *
from tkinter import Tk , ttk
from urllib.parse import urlparse


def makeQr():
    img = qrcode.make(url.get())
    img.save(f'{name.get()}.png')
    img.show()

def clear():
    url.delete(0, END)
    name.delete(0, END)
   

col1 = "white"
col2 = "red"
col3 = "violet"
f1 = "blue"
root = Tk()
root.title("QR_Code Maker")
root.geometry("310x260")
root.resizable(height = False , width = False)
# upper frame
frame_up = Frame(root , width = 720 , height = 70 , bg =col3)
frame_up.grid(row = 0 , column = 0)
heading = Label (frame_up , text = "QR-Code Maker", bg = col3 , fg ="black",font =("ivy 20 bold") )
heading.place(x = 55, y = 10)
line = Label(frame_up,  width =380,text = "" , height = 1 , bg = col2 ,  anchor = "nw")
line.place(x = 0 , y = 65)
# framedown
frame_down = Frame(root , width = 720 , height = 480, bg =col1 )
# labels
URL = Label(root, text="⭐ Website link",font=("arial 18 "), bg=col1)
URLName = Label(root, text="⭐ Name to be saved",font=("arial" ,'18'),bg=col1)
URLName.place(x =32 , y = 72)
URL.place(x = 56 , y = 135)
# __
name = Entry(frame_down, width = 38 , justify = "center" , font=("arial  10") , highlightthickness=2,border= 3)
name.place(x = 10 , y = 35)
url = Entry(frame_down,width = 38 , justify = "center" , font=("arial  10") , highlightthickness=2,border=3)
url.place(x = 10 , y = 100)
frame_down.grid(row = 1, column = 0)
btn_url = Button(frame_down , text ="Get_QR", width = 15  , fg = "black", command = makeQr)
btn_url.place(x = 10, y =140)
btn_clear = Button(frame_down , text ="Clear", width = 15  , fg = "black", command = clear)
btn_clear.place(x = 169, y =140)
text = Label(frame_down,text="THANKS!✌️" , bg = col1)
text.place(x=350,y=110)
root.mainloop()