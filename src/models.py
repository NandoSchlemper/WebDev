from src import db

class Tickets(db.Model):
    id         = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nfe        = db.Column(db.Integer, nullable=False)
    placa      = db.Column(db.String(7), nullable=False)
    tara       = db.Column(db.Float, nullable=False)
    peso_total = db.Column(db.Float, nullable=False)
    excesso    = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'< Ticket: {self.nfe}, Placa: {self.placa}'
    

class Placas(db.Model):
    id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    placa = db.Column(db.String(7), nullable=False)
    motorista = db.relationship('Motoristas', blackref='nome_motorista', lazy=True)


class Motoristas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), db.ForeignKey('nome'), nullable=False)