import psycopg2
from flask import Flask, jsonify
import os

app = Flask(__name__)

def get_db_connection():
    # Connexion au service postgres-service défini dans le YAML
    conn = psycopg2.connect(
        host="postgres-service",
        database="postgres",
        user="postgres",
        password="password123"
    )
    return conn

@app.route('/api/hello')
def hello():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({
            "status": "success",
            "message": f"Hello from the Python backend! (Connected to {db_version[0]})",
            "version": "1.0"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)