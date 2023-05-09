from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil


def close_program():
    answer = messagebox.askokcancel(title='Выход', message='Закрыть программу?')
    if answer:
        root.destroy()

# ============================================================
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    file_label.config(text="Выбранный файл: "+os.path.basename(filename))

def save_file():
    global filename
    if filename:
        file_name, file_ext = os.path.splitext(os.path.basename(filename))
        first_letter = file_name[0].upper()
        # os.mkdir("files")
        # os.chdir("files")
        folder_name = f"{first_letter}_files"
        if not os.path.exists(folder_name):

            os.mkdir(folder_name)
        new_file_path = os.path.join(folder_name, file_name + file_ext)
        try:
            shutil.copy(filename, new_file_path)
            print(f"File saved in {new_file_path}")
        except shutil.Error:
            shutil.copy(filename, new_file_path)
            os.remove(filename)
            print(f"File saved in {new_file_path}")
        save_label.config(text="Файл сохранен в папку: " + folder_name)

# ==============================================================================

root = Tk()

style = ttk.Style()
style.configure('TNotebook.Tab', font=('TkDefaultFont', 12))

root.protocol("WM_DELETE_WINDOW", close_program)

root.title('Картотека')
# Иконка
icon = PhotoImage(file="library.png")
root.iconphoto(False, icon)
# Размеры окна
root.geometry('300x300+500+500')
root.resizable(False, False)

main_menu = Menu(root)
root.config(menu=main_menu)
# File menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Выход', command=close_program)
main_menu.add_cascade(label='Файл', menu=file_menu)
# Help menu
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label='Помощь')
help_menu.add_command(label='О программе')
main_menu.add_cascade(label='Справка', menu=help_menu)

# создаем набор вкладок
notebook = ttk.Notebook(padding=(3, 3, 3, 3))
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Добавить")
notebook.add(frame2, text="Найти")
# ===========================================================================
file_label = Label(frame1, text="Выберите файл")
file_label.pack()

browse_button = ttk.Button(frame1, text="Обзор", command=browse_file)
browse_button.pack()

save_button = ttk.Button(frame1, text="Сохранить", command=save_file)
save_button.pack()

save_label = Label(frame1, text="")
save_label.pack()
# =======================================================================
root.mainloop()
