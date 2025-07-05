import os
import sys

# Ensure the current directory is in the module search path for CI environments
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.before_request
def log_request():
    print(f"==> {request.method} {request.path}")

@app.route('/')
def index():
    return jsonify({
        'message': 'Mock Server Running',
        'endpoints': [
            '/api/user/<user_id>',
            '/api/user [POST, PUT, DELETE]',
            '/api/products',
            '/api/order/<order_id>',
            '/api/order [POST]',
            '/api/login',
            '/api/logout',
            '/api/health',
            '/api/notifications',
            '/api/settings [GET, PUT]',
            '/api/profile [GET, PATCH]',
            '/api/reports',
            '/api/upload [POST]'
        ]
    })

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({'user_id': user_id, 'name': 'User'+str(user_id)})

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({'message': 'User created', 'user': data}), 201

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return jsonify({'message': 'User updated', 'user_id': user_id, 'updates': data})

@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({'message': f'User {user_id} deleted'})

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': ['Product A', 'Product B', 'Product C']})

@app.route('/api/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return jsonify({'order_id': order_id, 'status': 'processing'})

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.get_json()
    return jsonify({'message': 'Order placed', 'order': data}), 201

@app.route('/api/login', methods=['POST'])
def login():
    creds = request.get_json()
    return jsonify({'message': f"Welcome {creds.get('username')}", 'token': 'mock-token-123'})

@app.route('/api/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'User logged out'})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'uptime': '100h'})

@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    return jsonify({'notifications': ['Message 1', 'Alert 2', 'Reminder 3']})

@app.route('/api/settings', methods=['GET'])
def get_settings():
    return jsonify({'theme': 'dark', 'language': 'en', 'timezone': 'UTC'})

@app.route('/api/settings', methods=['PUT'])
def update_settings():
    data = request.get_json()
    return jsonify({'message': 'Settings updated', 'settings': data})

@app.route('/api/profile', methods=['GET'])
def get_profile():
    return jsonify({'name': 'John Doe', 'email': 'john@example.com', 'role': 'admin'})

@app.route('/api/profile', methods=['PATCH'])
def update_profile():
    data = request.get_json()
    return jsonify({'message': 'Profile updated', 'updates': data})

@app.route('/api/reports', methods=['GET'])
def get_reports():
    return jsonify({'reports': ['Report1.pdf', 'Report2.xlsx']})

@app.route('/api/upload', methods=['POST'])
def upload_file():
    return jsonify({'message': 'File uploaded successfully', 'file_id': '12345'})

if __name__ == '__main__':
    print("Starting Flask mock server on http://localhost:5000")
    app.run(debug=False, port=5000)