from flask_wtf import FlaskForm
import wtforms as w

class TicketForm(FlaskForm):
    nfe = w.IntegerField('Nota Fiscal', validators=[w.validators.DataRequired()])
    placa = w.StringField('Placa', validators=[w.validators.DataRequired(), w.validators.Length(min=7, max=7)])
    tara = w.FloatField('Peso Tara', validators=[w.validators.DataRequired()])
    peso_total = w.FloatField('Peso Total Carregado', validators=[w.validators.DataRequired()])
    excesso = w.FloatField('Excesso Calculado', validators=[w.validators.DataRequired()])

    submit = w.SubmitField('Submit')


class PlacasForm(FlaskForm):
    placa = w.StringField('Placa', validators=[w.validators.DataRequired(), w.validators.Length(min=7, max=7)])
    motorista = w.StringField('Motorista', validators=[w.validators.DataRequired()])

    submit = w.SubmitField('Submit')


class MotoristasForm(FlaskForm):
    nome = w.StringField('Motorista', validators=[w.validators.DataRequired(), w.validators.Length(max=55)])

    submit = w.SubmitField('Submit')
