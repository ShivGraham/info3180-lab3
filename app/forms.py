from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextField, TextAreaField 
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	email = TextField('Email', validators=[DataRequired(), Email()]) 
	subject = TextField('Subject', validators=[DataRequired()])
	message = TextAreaField('Message', validators=[DataRequired()])