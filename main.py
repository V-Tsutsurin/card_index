from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def close_program():
    answer = messagebox.askokcancel(title='Выход', message='Закрыть программу?')
    if answer:
        root.destroy()


root = Tk()
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


root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',True)

root.mainloop()
