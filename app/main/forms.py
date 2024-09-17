from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length

disciplina_choices = [
    ('DSWA5', 'DSWA5'),
    ('GPSA5', 'GPSA5'),
    ('IHCA5', 'IHCA5'),
    ('SODA5', 'SODA5'),
    ('PJIA5', 'PJIA5'),
    ('TCOA5', 'TCOA5')]

class NameForm(FlaskForm):
    disciplina = SelectField('Disciplina associada:', choices=disciplina_choices, validators=[DataRequired()])
    data = DateTimeField('Data e Horário:', format='%d/%m/%Y %H:%M', validators=[DataRequired(message="Por favor, insira uma data e hora válidas.")])
    name = TextAreaField('Descrição da ocorrência (250 caracteres)', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Enviar')

