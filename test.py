import os
import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
        except IOError:
            print('Error: file not found or cannot be read')
        else:
            folder_name = file_path.split('/')[-1][0]
            folder_path = os.path.join(os.getcwd(), folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            new_file_path = os.path.join(folder_path, os.path.basename(file_path))
            with open(new_file_path, 'wb') as f:
                f.write(data)
            print('File saved successfully')

root = tk.Tk()
root.withdraw()

save_button = tk.Button(text='Save File', command=save_file)
save_button.pack()

root.mainloop()
