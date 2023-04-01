from repository.auth_repository import AuthRepository

class AuthService:
    def __init__(self):
        self.repository = AuthRepository('auth_db.sqlite')

    def create_user(self, username, password):
        self.repository.create_user(username, password)

    def authenticate(self, username, password):
        return self.repository.authenticate(username, password)
        
    def create_table(self):
        self.repository.create_table()