from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for handling cross-origin requests
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MySQL database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'example'),
        database=os.getenv('DB_NAME', 'clickops')
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the backend service!"}), 200

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')
    course = data.get('course')
    gender = data.get('gender')

    if not all([name, age, course, gender]):
        return jsonify({"message": "All fields are required!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age, course, gender) VALUES (%s, %s, %s, %s)",
                   (name, age, course, gender))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Thank you for choosing us!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

