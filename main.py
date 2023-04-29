from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Картотека')
root.iconbitmap('library.ico')
root.geometry('300x300+500+500')

btn1 = Button(text="Кнопка")
btn1.pack()

btn = ttk.Button(text="Кнопка")
btn.pack()


root.mainloop()
