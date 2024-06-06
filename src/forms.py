from flask_wtf import FlaskForm
import wtforms as w

class TicketForm(FlaskForm):
    nfe  = w.IntegerField('Nota Fiscal', validators=[w.validators.DataRequired()])
    placa   = w.StringField('Placa', validators=[w.validators.DataRequired()])
    tara    = w.FloatField('Peso tara', validators=[w.validators.DataRequired()])
    peso_total   = w.FloatField('Peso total carregado', validators=[w.validators.DataRequired()])
    excesso = w.FloatField('Excesso calculado', validators=[w.validators.DataRequired()])

    submit = w.SubmitField('Submit')

