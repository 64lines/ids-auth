from flask import Flask, jsonify, session, request
from flask_cors import CORS
from service.auth_service import AuthService

app = Flask(__name__)
app.secret_key = "supersecretkey"
cors = CORS(app)

auth_service = AuthService()
auth_service.create_table()

@app.route('/api/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    auth_service.create_user(username, password)
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    if auth_service.authenticate(username, password):
        session['username'] = username 
        return jsonify({'message': 'Login succeeded'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401
    
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('username', None) # Remove the username from the session
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    app.run()