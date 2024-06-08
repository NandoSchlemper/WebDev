from src import db

class LocalCarregamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local = db.Column(db.String(20), unique=True, nullable=False)
    gps = db.Column(db.String(122))


class Motoristas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(55), unique=True, nullable=False)


class Placas(db.Model):
    id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    motorista = db.Column(db.String, db.ForeignKey(Motoristas.nome), unique=True, nullable=False)
    placa = db.Column(db.String(7), unique=True, nullable=False)



class Tickets(db.Model):
    id         = db.Column(db.Integer, primary_key=True,autoincrement=True)
    carregamento = db.Column(db.String, db.ForeignKey(LocalCarregamento.local), nullable=False)
    nfe        = db.Column(db.Integer, unique=True, nullable=False)
    placa   = db.Column(db.String, db.ForeignKey(Placas.placa), nullable=False) 
    tara       = db.Column(db.Float, nullable=False)
    peso_total = db.Column(db.Float, nullable=False)
    excesso    = db.Column(db.Float, nullable=False)

