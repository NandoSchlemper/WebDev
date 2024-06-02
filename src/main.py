from flask import Flask, request, jsonify
import sqlite3 as sql
import os

app = Flask(__name__)

DATABASE_PATH = "database/form-db.db"

@app.route("/get/all-users", methods=['GET'])
def get_all_users():
    con = sql.connect(DATABASE_PATH)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    users = [dict(row) for row in rows]
    con.close()
    return jsonify(users)

@app.route("/create_user", methods=['POST'])
def create_user():
    if request.is_json:
        data = request.get_json()
        username = data.get("USERNAME")
        age = data.get("AGE")

        if not username or not age:
            return jsonify({"error": "Invalid input"}), 400

        con = sql.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.execute("INSERT INTO users (USERNAME, AGE) VALUES (?, ?)", (username, age))
        con.commit()
        con.close()
        return jsonify({"message": f"User {username} added successfully!"}), 201
    return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True)
