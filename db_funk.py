import sqlite3

# from main import Child

class DB:
    def __init__(self, title, date_create, doc_type, creator, location, description, file_path):
        self.title = title
        self.date_create = date_create
        self.doc_type = doc_type
        self.creator = creator
        self.location = location
        self.description = description
        self.file_path = file_path
        self.conn = sqlite3.connect('card_index.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS card_index 
            (id integer primary key,
            title text,
            date_create text,
            doc_type text,
            creator text,
            location text,
            description text,
            file_path text
            )'''
        )
        self.conn.commit()

    def write_data(self, title, date_create, doc_type, creator, location, description, file_path):
        self.c.execute('''INSERT INTO card_index(
        title,
        date_create,
        doc_type,
        creator,
        location,
        description,
        file_path) VALUES (?, ?, ?, ?, ?, ?, ?)
         ''', (title, date_create, doc_type, creator, location, description, file_path))
        self.conn.commit()


