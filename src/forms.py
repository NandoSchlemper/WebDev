from flask_wtf import FlaskForm
import wtforms as w
from src.models import Placas, LocalCarregamento, Motoristas, Tickets

class TicketForm(FlaskForm):
    carregamento = w.SelectField('Local Carregamento', validators=[w.validators.DataRequired()])
    nfe = w.IntegerField('Nota Fiscal', validators=[w.validators.DataRequired()])
    placa = w.StringField('Placa', validators=[w.validators.DataRequired(), w.validators.Length(min=7, max=8)])
    tara = w.FloatField('Peso Tara', validators=[w.validators.DataRequired()])
    peso_total = w.FloatField('Peso Total Carregado', validators=[w.validators.DataRequired()])
    excesso = w.FloatField('Excesso Calculado', validators=[w.validators.DataRequired()])

    submit = w.SubmitField('Submit')

    def ValidarPlaca(self, field):
        if not Placas.query.filter_by(field.data).first():
            raise w.validators.ValidationError('Placa nao encontrada no banco de dados')


class LocalCarregamentoForm(FlaskForm):
    local = w.StringField('Local', validators=[w.validators.DataRequired(), w.validators.Length(max=20)])
    gps = w.StringField('GpsLink', validators=[w.validators.Length(max=122)])



class PlacasForm(FlaskForm):
    placa = w.StringField('Placa', validators=[w.validators.DataRequired(), w.validators.Length(min=7, max=8)])
    motorista = w.StringField('Motorista', validators=[w.validators.DataRequired()])

    submit = w.SubmitField('Submit')


class MotoristasForm(FlaskForm):
    nome = w.StringField('Motorista', validators=[w.validators.DataRequired(), w.validators.Length(max=55)])

    submit = w.SubmitField('Submit')
    
    def update(self, mot):
        mot.nome = self.nome.data

