import tkinter as tk
from tkinter import ttk, filedialog
from db_funk import DB as DB
import os
import shutil
import subprocess
import datetime


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='white', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.img_add = tk.PhotoImage(file="New Add32.png")
        btn_add_new = ttk.Button(toolbar, text="Добавить", command=self.open_dialog,
                                 compound=tk.TOP, image=self.img_add)
        btn_add_new.pack(side=tk.LEFT)

        self.img_upd = tk.PhotoImage(file="New Edit32.png")
        btn_edit_dialog = ttk.Button(toolbar, text="Редактировать", command=self.open_update_dialog,
                                 compound=tk.TOP, image=self.img_upd)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.img_del = tk.PhotoImage(file="New Remove32.png")
        btn_delete = ttk.Button(toolbar, text="Удалить позицию", command=self.delete_records,
                                     compound=tk.TOP, image=self.img_del)
        btn_delete.pack(side=tk.LEFT)

        self.img_search = tk.PhotoImage(file="Find32.png")
        btn_search = ttk.Button(toolbar, text="Поиск", command=self.open_search_dialog,
                                compound=tk.TOP, image=self.img_search)
        btn_search.pack(side=tk.LEFT)

        self.img_refresh = tk.PhotoImage(file="Refresh Green32.png")
        btn_refresh = ttk.Button(toolbar, text="Обновить", command=self.view_records,
                                compound=tk.TOP, image=self.img_refresh)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'title', 'date_create', 'doc_type',
                                                'creator', 'location', 'description',
                                                'file_path'), height=15, show='headings')

        self.tree.column('ID', width=10, minwidth=10, anchor=tk.CENTER)
        self.tree.column('title', width=110, minwidth=30, anchor=tk.CENTER)
        self.tree.column('date_create', width=100, minwidth=30, anchor=tk.CENTER)
        self.tree.column('doc_type', width=75, minwidth=30, anchor=tk.CENTER)
        self.tree.column('creator', width=20, minwidth=10, anchor=tk.CENTER)
        self.tree.column('location', width=70, minwidth=30, anchor=tk.CENTER)
        self.tree.column('description', width=80, minwidth=30, anchor=tk.CENTER)
        self.tree.column('file_path', width=100, minwidth=30, anchor=tk.CENTER)

        self.tree.heading('ID', text='№')
        self.tree.heading('title', text='Название документа')
        self.tree.heading('date_create', text='Дата на документе')
        self.tree.heading('doc_type', text='Тип документа')
        self.tree.heading('creator', text='Автор')
        self.tree.heading('location', text='Место хранения')
        self.tree.heading('description', text='Краткое описание')
        self.tree.heading('file_path', text='Путь к документу')

        self.tree.pack(fill="both", expand=1, pady=10, padx=10, side=tk.LEFT)

        scroll = tk.Scrollbar(self, bg='white', command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, title, date_create, doc_type, creator, location, description, file_path):
        db.write_data(title, date_create, doc_type, creator, location, description, file_path)
        self.view_records()

    def update_record(self, title, date_create, doc_type, creator, location, description, file_path):
        self.db.c.execute('''UPDATE card_index SET
        title=?, date_create=?, doc_type=?, creator=?, location=?, description=?, file_path=? WHERE ID=?''',
                          (title, date_create, doc_type, creator, location, description, file_path,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM card_index''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM card_index WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, description):
        description = ('%' + description + '%',)
        self.db.c.execute('''SELECT * FROM card_index WHERE description LIKE ?''', description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

    def open_file(self, event):
        # получаем адрес файла из ячейки
        item = self.tree.selection()[0]
        file_path = self.tree.item(item)["values"][0]
        # открываем файл с помощью модуля subprocess
        subprocess.Popen(["open", file_path])


# Окно кнопки добавить
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

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

        label_date_create = ttk.Label(self, text='Дата на документе')
        label_date_create.place(x=50, y=80)
        self.entry_date_create = ttk.Entry(self)
        self.entry_date_create.place(x=200, y=80)

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

        self.label_file_path = ttk.Label(self, text='Выберите файл')
        self.label_file_path.place(x=50, y=230)

        def browse_file():
            global filename
            filename = filedialog.askopenfilename()
            return filename
            # file_label.config(text="Выбранный файл: "+os.path.basename(filename))

        self.entry_file_path = ttk.Button(self, text="Обзор", command=browse_file)
        self.entry_file_path.place(x=200, y=230)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=270)

        def data():
            date = datetime.datetime.now()
            unic_data = str(date)[9:25:3]
            return unic_data

        def save_file():
            global filename
            global new_file_path
            if filename:
                file_name, file_ext = os.path.splitext(os.path.basename(filename))
                first_letter = file_name[0].upper()
                # os.mkdir("files")
                # os.chdir("files")
                global folder_name
                folder_name = f"{first_letter}_files"
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)

                unic = data()

                global new_file_path
                new_file_path = os.path.join(folder_name, unic + file_name + file_ext)
                try:
                    shutil.copy(filename, new_file_path)
                    print(f"File saved in {new_file_path}")
                    return new_file_path
                except shutil.Error:
                    shutil.copy(filename, new_file_path)
                    os.remove(filename)
                    print(f"File saved in {new_file_path}")
                    return new_file_path
            return new_file_path

        self.btn_ok = ttk.Button(self, text='Дабавить')
        self.btn_ok.place(x=220, y=270)

        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(
            self.entry_title.get(),
            self.entry_date_create.get(),
            self.entry_doc_type.get(),
            self.entry_creator.get(),
            self.entry_location.get(),
            self.entry_description.get(),
            save_file(),
        ))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()
        # self.save_file = ''

    def init_edit(self):
        self.title('Редактировать позицию')

        self.label_file_path.destroy()
        self.entry_file_path.destroy()
        label_file = ttk.Label(self, text='Файл:')
        label_file.place(x=50, y=230)
        self.file_path = ttk.Entry(self)
        self.file_path.place(x=200, y=230)

        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=270)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(
            self.entry_title.get(),
            self.entry_date_create.get(),
            self.entry_doc_type.get(),
            self.entry_creator.get(),
            self.entry_location.get(),
            self.entry_description.get(),
            self.file_path.get(),
        ))
        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM card_index WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchone()
        self.entry_title.insert(0, row[1])
        self.entry_date_create.insert(0, row[2])
        self.entry_doc_type.insert(0, row[3])
        self.entry_creator.insert(0, row[4])
        self.entry_location.insert(0, row[5])
        self.entry_description.insert(0, row[6])
        self.file_path.insert(0, row[7])
        print(self.file_path)


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        icon = tk.PhotoImage(file="Folder (Adorner in front) Database16.png")
        self.iconphoto(False, icon)
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


if __name__ == '__main__':
    root = tk.Tk()
    db = DB('title', 'date_create', 'doc_type', 'creator', 'location', 'description', 'file_path')
    app = Main(root)
    app.pack(fill="both", expand=1, pady=10, padx=10, side=tk.LEFT)
    # Название
    root.title("Электронная картотека")
    # Иконка
    icon = tk.PhotoImage(file="Folder (Adorner in front) Database16.png")
    root.iconphoto(False, icon)
    # Размеры окна
    root.geometry("865x650+300+200")
    root.resizable(True, True)
    # Запуск
    root.mainloop()
