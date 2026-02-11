from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": "db",   
    "user": "root",
    "password": "rootpassword",
    "database": "demo"
}

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(**db_config)
        return "Connected to MySQL successfully!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
