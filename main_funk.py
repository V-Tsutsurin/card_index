from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    # file_label.config(text="Выбранный файл: "+os.path.basename(filename))