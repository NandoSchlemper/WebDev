from flask import Flask, request, jsonify, redirect
import sqlite3 as sql

# Vamos comecar a utilizar alguns forms do Flask para facilitar a aplicacao de rodar, segue exemplos:
from forms import InserirTicket

import secrets
app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key(foo)

DATABASE_PATH = "form-db.db"

# Homepage padrao ;)
@app.route("/")
def home():
    hello_word = "hello world bitches"
    return jsonify(hello_word)


# GET --> Mostrar Todos os Tickets em Formato de Tabela posteriormente
@app.route("/all-tickets", methods=['GET'])
def get_all_tickets():
    con = sql.connect(DATABASE_PATH)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM tickets")
    rows = cur.fetchall()
    tickets = [dict(row) for row in rows]
    con.close()
    return jsonify(tickets)


# POST --> Criando novo ticket
@app.route("/create_ticket", methods=['POST'])
def create_ticket():
    form = InserirTicket()
    if request.method == "POST":
        if form.validate_on_submit():
            form_data = form.data
            print(f"{form_data}")
            # Fazer a logica por tras do DB e do form_data
            con = sql.connect(DATABASE_PATH)
            cur = con.cursor()
            cur.execute("INSERT INTO tickets (NF, DATA, PESO) VALUES (?, ?, ?)", (nf, date, peso))
            con.commit()
            con.close()
            return jsonify({"message": f"Ticket {nf} added successfully!"}), 201
    return jsonify({"error": "Request must be JSON"}), 400


# POST --> Editando completamente um ticket, adicionar edicoes parciais depois
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


# DELETE --> Deletando um ticket, adicionar uma confirmacao dps
@app.route("/delete_ticket/<nfe>", methods=["DELETE"])
def delete_ticket(nfe):
    if request.method == "DELETE":
        con = sql.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.execute("delete from tickets where NF=?", (nfe))
        jsonify({"message": "Ticket {nfe} deletado com sucesso!"})
        con.commit()
        con.close()
        return redirect("/get/all-tickets")
    return jsonify({"error": "Method must be DELETE"})

if __name__ == "__main__":
    app.run(debug=True)
