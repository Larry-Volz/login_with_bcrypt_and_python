from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired 


class RegisterForm(FlaskForm):
    """Form for registering a user.""" 

    email = StringField("email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class LoginForm(FlaskForm):
    """Form for registering a user."""

    email = StringField("email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
