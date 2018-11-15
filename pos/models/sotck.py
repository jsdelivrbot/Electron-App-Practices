class Stock:
    TABLE_NAME = 'stock'

    def __init__(self, id, barcode, unit_price, selling_price, sold_status, purchase_inventory, status, updated_at):
        self.id = id
        self.barcode = barcode
        self.unit_price = unit_price
        self.selling_price = selling_price
        self.sold_status = sold_status
        self.purchase_inventory = purchase_inventory
        self.status = status
        self.updated_at = updated_at
