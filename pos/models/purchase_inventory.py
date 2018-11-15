from database import Database
import datetime


class Purchase_inventory:
    TABLE_NAME = 'purchase_inventory'

    def __init__(self, id=None, purchase_date=None, product_id=None,
                 supplier_id=None, quantity=None, cost=None, status=0,
                 updated_at=datetime.datetime.now()):
        self.id = id
        self.purchase_date = purchase_date
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.quantity = quantity
        self.cost = cost
        self.status = status
        self.updated_at = updated_at

    def json(self):
        return self.__dict__

    def getParams(self):
        data = self.json()
        params = {k: v for k, v in data.items() if v !=
                  None and k != "id"}
        return params

    @classmethod
    def find_purchase_inventory_by_id(cls, database, params):
        tempDB = Database(database)
        row = tempDB.get_rows(cls.TABLE_NAME, params)
        del tempDB
        if row:
            row = row[0]
            resPur = Purchase_inventory(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            return resPur
        else:
            return {}

    @classmethod
    def update_from_database(cls, database, key, params):
        tempDB = Database(database)
        row = tempDB.update_row(cls.TABLE_NAME, params, key)
        del tempDB
        return row

    @classmethod
    def delete_from_database(cls, database, key):
        tempDB = Database(database)
        row = tempDB.delete_row(cls.TABLE_NAME, key)
        del tempDB
        return row

    @classmethod
    def insert_into_database(cls, database, params):
        tempDB = Database(database)
        row = tempDB.insert_row(cls.TABLE_NAME, params)
        del tempDB
        return row

    @classmethod
    def get_all_rows(cls, database):
        tempDB = Database(database)
        rows = tempDB.get_rows(cls.TABLE_NAME)

        rows = [Purchase_inventory(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]).json()
                for x in rows]

        del tempDB
        if rows:
            return rows
        return False
