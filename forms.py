from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired])
    ##username = StringField('Username' , [DataRequired(), Length(min=5,message = ('Your username is too short')))])
    password = PasswordField('Password', validators=[DataRequired])
    ##password = PasswordField('Password',[DataRequired(), Length(min=5,message = ('Your username is too short')))])
    submit = SubmitField('Sign in')
