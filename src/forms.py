from flask_wtf import FlaskForm
import wtforms as wt
import wtforms.validators as val

class InserirTicket(FlaskForm):
    ticket = wt.IntegerField('Insira o valor do ticket', validators=[val.DataRequired(), val.Length(1, 25)])
    data = wt.StringField('Insira a data da descarga', validators=[val.DataRequired(), val.Length(8, 12)])
    peso = wt.FloatField('Insira o peso da NF', validators=[val.DataRequired()])
    submit = wt.SubmitField('Subimit')
