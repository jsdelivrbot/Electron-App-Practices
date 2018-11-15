class Supplier:
    TABLE_NAME = 'supplier'

    def __init__(self, id, name, address, phone, company_name, balance, status, updated_at):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.company_name = company_name
        self.balance = balance
        self.status = status
        self.updated_at = updated_at
