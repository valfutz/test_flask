from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class UserForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(),
                    Length(min=2, max=50, message='first_name should be between 4 and 50 characters')])
    last_name = StringField('last_name', validators=[DataRequired(),
                    Length(min=2, max=50, message='last_name should be between 4 and 50 characters')])
    username = StringField('Username', validators=[DataRequired(),
                    Length(min=2, max=50, message='username should be between 4 and 50 characters')])
    psw = PasswordField('Password', validators=[DataRequired(),
                    Length(min=4, max=50, message='username should be between 4 and 50 characters')])
    psw2 = PasswordField('Confirm Password', validators=[DataRequired(),
                     EqualTo('psw', message='Passwords must match')])
    submit = SubmitField('Sign Up')

