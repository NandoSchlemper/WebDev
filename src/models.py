from src import db


class Tickets(db.Model):
    id         = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nfe        = db.Column(db.Integer, nullable=False)
    placa      = db.Column(db.String, db.ForeignKey('Placas.placa'), nullable=False)
    placa_relation      = db.relationship('Placas', blackref='tickets', lazy=True)
    tara       = db.Column(db.Float, nullable=False)
    peso_total = db.Column(db.Float, nullable=False)
    excesso    = db.Column(db.Float, nullable=False)

class Placas(db.Model):
    id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    placa = db.Column(db.String(7), nullable=False)
    motorista = db.Column(db.String, db.ForeignKey('Motoristas.nome'))# So pode ter 1 mot p/cada placa
    motorista_relation = db.relationship('Motoristas', backref=db.backref('placa', uselist=False))

class Motoristas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(55), nullable=False)
