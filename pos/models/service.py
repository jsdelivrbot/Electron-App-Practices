class Service:
    TABLE_NAME = 'service'

    def __init__(self, id, name, status, updated_at):
        self.id = id
        self.name = name
        self.status = status
        self.updated_at = updated_at
