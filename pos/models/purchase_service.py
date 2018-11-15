class Purchase_service:
    TABLE_NAME = 'purchase_service'

    def __init__(self, id, purchase_date, service_id, cost, status, updated_at):
        self.id = id
        self.purchase_date = purchase_date
        self.service_id = service_id
        self.cost = cost
        self.status = status
        self.updated_at = updated_at
