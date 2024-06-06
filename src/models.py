from src import db

class Tickets(db.Model):
    nfe        = db.Column(db.Integer, primary_key=True, nullable=False)
    placa      = db.Column(db.String(7), nullable=False)
    tara       = db.Column(db.Float, nullable=False)
    peso_total = db.Column(db.Float, nullable=False)
    excesso    = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'< Ticket: {self.nfe}, Placa: {self.placa}'
    
