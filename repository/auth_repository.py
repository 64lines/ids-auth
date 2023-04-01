import sqlite3
import hashlib

class AuthRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_user(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()

        # Close the database connection
        conn.close()

    def authenticate(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Hash the password to compare with the stored hash
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the user exists and the password is correct
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        result = cursor.fetchone()

        # Close the database connection
        conn.close()

        # Return True if the user exists and the password is correct, False otherwise
        if result is not None:
            return True
        else:
            return False
        
    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)')
        conn.commit()
        conn.close()