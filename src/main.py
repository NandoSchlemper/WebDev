from flask import Flask, request, jsonify, redirect
import sqlite3 as sql
import os

app = Flask(__name__)

DATABASE_PATH = "form-db.db"

@app.route("/")
def home():
    hello_word = "hello world bitches"
    return jsonify(hello_word)

@app.route("/get/all-tickets", methods=['GET'])
def get_all_users():
    con = sql.connect(DATABASE_PATH)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM tickets")
    rows = cur.fetchall()
    tickets = [dict(row) for row in rows]
    con.close()
    return jsonify(tickets)

@app.route("/create_ticket", methods=['POST'])
def create_user():
    if request.is_json:
        data = request.get_json()
        nf = data.get("NF")
        date = data.get("DATA")
        peso = data.get("PESO")

        if not date or not peso:
            return jsonify({"error": "Invalid input"}), 400

        con = sql.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.execute("INSERT INTO tickets (NF, DATA, PESO) VALUES (?, ?, ?)", (nf, date, peso))
        con.commit()
        con.close()
        return jsonify({"message": f"Ticket {nf} added successfully!"}), 201
    return jsonify({"error": "Request must be JSON"}), 400


@app.route("/edit_ticket/<nfe>", methods=["POST", "GET"])
def edit_ticket(nfe):
    if request.method == "POST":
        data = request.get_json()
        nf = data.get("NF")
        date = data.get("DATA")
        peso = data.get("PESO")
        con = sql.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.execute("update tickets set NF=?, DATA=?, PESO=? where NF=?", (nf, date, peso, nfe))
        ticket_alterado = f"{nf, date, peso}"
        con.commit()
        con.close()
        return jsonify({"message": f"Ticket {nf} foi alterado! Novo ticket: {ticket_alterado}"}), 201
    return jsonify({"error": "Request must be JSON"})


@app.route("/delete_ticket/<nfe>", methods=["DELETE"])
def delete_ticket(nfe):
    if request.method == "DELETE":
        con = sql.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.execute("delete from tickets where NF=?", (nfe,))
        jsonify({"message": "Ticket {nfe} deletado com sucesso!"})
        con.commit()
        con.close()
        return redirect("/get/all-tickets")
    return jsonify({"error": "Method must be DELETE"})

if __name__ == "__main__":
    app.run(debug=True)
