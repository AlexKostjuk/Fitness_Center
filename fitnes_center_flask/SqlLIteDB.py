import sqlite3
def dict_factory(cursor, row):
    d={}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Dbsql:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = dict_factory
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


    def fetch_oll(self, qvery, *args, **kwargs):
        cursor = self.connection.cursor()
        cursor.execute(qvery, *args, **kwargs)
        res = cursor.fetchall()
        if res:
            return res
        return res

    def fetch_one(self, qvery, *args, **kwargs):
        cursor = self.connection.cursor()
        cursor.execute(qvery, *args, **kwargs)
        res = cursor.fetchone()
        if res:
            return res
        return None

    def insert_to_db(self, qvery, *args, **kwargs):
        cursor = self.connection.cursor()
        cursor.execute(qvery, *args, **kwargs)
        self.connection.commit()


