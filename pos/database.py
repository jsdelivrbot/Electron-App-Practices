import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)

    def insert_row(self, table, row):
        values = '('+",".join([str(i) for i in row])+')'
        params = '('+",".join([':'+i for i in row])+')'
        query = "INSERT INTO {} {} VALUES{}".format(table, values, params)
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(query, row)
                self.conn.commit()
                return True
        except:
            return None

    def get_rows(self, table, params={}):
        values = ""
        # print(params)
        for key in params.items():

            values += "{} = {} and ".format(key[0], ':'+key[0])
        try:
            if len(values) > 0:
                values = values[:-4]
                query = "SELECT * FROM {} where {}".format(table, values)
                with self.conn:
                    cursor = self.conn.cursor()
                    cursor.execute(query, params)
                    return cursor.fetchall()
            else:
                query = "SELECT * FROM {}".format(table)
                with self.conn:
                    cursor = self.conn.cursor()
                    cursor.execute(query, params)
                    return cursor.fetchall()
        except:
            return None

    def update_row(self, table, params, keys):
        if len(keys) < 1 or len(params) < 1:
            return None

        key_values = ""
        update_values = ""
        for k in keys.items():
            key_values += "{} = {} and ".format(k[0], ':'+k[0])
        key_values = key_values[:-4]
        for k in params.items():
            update_values += "{} = {} ,".format(k[0], ':'+k[0])
        update_values = update_values[:-1]

        query = "UPDATE {} SET {} WHERE {}".format(
            table, update_values, key_values)
        all_params = {**keys, **params}
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(query, all_params)
                return True
        except:
            return None

    def delete_row(self, table, params):
        values = ""
        for k in params.items():
            values += "{} = {} and ".format(k[0], ':'+k[0])

        values = values[:-4]
        query = "DELETE FROM {} WHERE {}".format(table, values)
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                return True
        except:
            return None

    def execute_query(self, query, params=None):
        if params:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                return cursor.fetchall()
        else:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(query)
                return cursor.fetchall()

    def __del__(self):
        self.conn.close()
