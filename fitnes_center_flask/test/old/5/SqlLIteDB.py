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


    def fetch_oll(self, table, colons = None, condition = None, join_table = None, join_condition = None):
        if colons is not None:
            if type(colons) == list:
                colons_str = ', '.join(colons)
                qvery = f'select {colons_str} from {table}'
            else:
                qvery = f'select {colons} from {table}'

        else:
            qvery = f'select * from {table}'
        conditions = []

        if join_table is not None:
            join_cond_list = []
            for key, val in join_condition.items():
                join_cond_list.append(f"{key}={val}")
            join_cond_str = " and ".join(join_cond_list)
            join_str = f" join {join_table} ON {join_cond_str} "
            qvery = qvery + join_str



        if condition is not None:
            for key, val in condition.items():
                conditions.append(f"{key}='{val}' ")
            str_conditions = " and ".join(conditions)
            str_conditions = " where " + str_conditions
            qvery = qvery + str_conditions
        cursor = self.connection.cursor()
        cursor.execute(qvery)
        res = cursor.fetchall()
        if res:
            return res
        return None


    def fetch_one(self, table, colons = None, condition = None, join_table = None, join_condition = None):

        if colons is not None:
            print(colons, len(colons))
            if type(colons) == list:
                colons_str = ', '.join(colons)
                print(colons_str)
                qvery = f'select {colons_str} from {table}'
            else:
                qvery = f'select {colons} from {table}'

        else:
            qvery = f'select * from {table}'
        conditions = []

        if join_table is not None:
            join_cond_list = []
            for key, val in join_condition.items():
                join_cond_list.append(f"{key}={val}")
            join_cond_str = " and ".join(join_cond_list)
            join_str = f" join {join_table} ON {join_cond_str} "
            qvery = qvery + join_str



        if condition is not None:
            for key, val in condition.items():
                conditions.append(f"{key}='{val}' ")
            str_conditions = " and ".join(conditions)
            str_conditions = " where " + str_conditions
            qvery = qvery + str_conditions
        cursor = self.connection.cursor()
        cursor.execute(qvery)
        res = cursor.fetchone()
        if res:
            return res
        return None



    def insert_to_db(self, table, data):
        keys = []
        vals = []
        for key, value in data.items():
            keys.append(key)
            vals.append("'"+str(value)+"'")
        str_keys = ', '.join(keys)
        str_vals = ', '.join(vals)
        qvery = f"INSERT INTO {table} ({str_keys}) VALUES ({str_vals})"

        cursor = self.connection.cursor()
        cursor.execute(qvery)
        self.connection.commit()


