from flask_wtf import FlaskForm,RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField,validators, ValidationError
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = TextField("Name",validators=[DataRequired()])
    email = TextField("Email",validators=[DataRequired(),validators.Email()])
    subject = TextField("Subject",validators=[DataRequired()])
    message = TextField("Message",validators=[DataRequired()])
    submit = SubmitField("Submit")