class User:
    TABLE_NAME = 'user'

    def __init__(self, id, name, address, phone, email, password, username, type, status, updated_at):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.username = username
        self.type = type
        self.status = status
        self.updated_at = updated_at
