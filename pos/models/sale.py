class Sales:
    TABLE_NAME = 'sales'

    def __init__(self, id, stock_id, selling_date, discount, discount_reason, sold_price, status, updated_at):
        self.id = id
        self.stock_id = stock_id
        self.selling_date = selling_date
        self.discount = discount
        self.discount_reason = discount_reason
        self.sold_price = sold_price
        self.status = status
        self.updated_at = updated_at
