import tkinter as tk
from tkinter import ttk
from main_funk import *


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='white', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.img_add = tk.PhotoImage(file="New Add32.png")
        btn_add_new = ttk.Button(toolbar, text="Добавить", command=self.open_dialog,
                                 compound=tk.TOP, image=self.img_add)

        btn_add_new.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'title', 'date', 'doc_type',
                                                'creator', 'location', 'description',
                                                'file_path'), height=15, show='headings')

        self.tree.column('ID', width=50, minwidth=30, anchor=tk.CENTER)
        self.tree.column('title', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('date', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('doc_type', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('creator', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('location', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('description', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('file_path', width=100, minwidth=30, anchor=tk.CENTER)

        self.tree.heading('ID', text='№')
        self.tree.heading('title', text='Название документа')
        self.tree.heading('date', text='Дата на документе')
        self.tree.heading('doc_type', text='Тип документа')
        self.tree.heading('creator', text='Автор')
        self.tree.heading('location', text='Место хранения')
        self.tree.heading('description', text='Краткое описание')
        self.tree.heading('file_path', text='Путь к документу')

        self.tree.pack()


    def open_dialog(self):
        Child()

# Окно кнопки добавить
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        icon = tk.PhotoImage(file="Folder (Adorner in front) Database16.png")
        self.iconphoto(False, icon)
        self.title('Добавление документа')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        label_title = ttk.Label(self, text='Название документа')
        label_title.place(x=50, y=50)
        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=200, y=50)

        label_date = ttk.Label(self, text='Дата на документе')
        label_date.place(x=50, y=80)
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=200, y=80)

        label_doc_type = ttk.Label(self, text='Тип документа')
        label_doc_type.place(x=50, y=110)
        self.entry_doc_type = ttk.Entry(self)
        self.entry_doc_type.place(x=200, y=110)

        label_creator = ttk.Label(self, text='Автор')
        label_creator.place(x=50, y=140)
        self.entry_creator = ttk.Entry(self)
        self.entry_creator.place(x=200, y=140)

        label_location = ttk.Label(self, text='Место хранения')
        label_location.place(x=50, y=170)
        self.entry_location = ttk.Entry(self)
        self.entry_location.place(x=200, y=170)

        label_description = ttk.Label(self, text='Краткое описание')
        label_description.place(x=50, y=200)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=200)

        label_file_path = ttk.Label(self, text='Выберите файл')
        label_file_path.place(x=50, y=230)
        self.entry_file_path = ttk.Button(self, text="Обзор", command=browse_file)
        self.entry_file_path.place(x=200, y=230)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=270)

        btn_ok = ttk.Button(self, text='Дабавить')
        btn_ok.place(x=220, y=270)

        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    # Название
    root.title("Электронная картотека")
    # Иконка
    icon = tk.PhotoImage(file="Folder (Adorner in front) Database16.png")
    root.iconphoto(False, icon)
    # Размеры окна
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    # Запуск
    root.mainloop()
