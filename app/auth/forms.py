from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from app.models import User



class LoginForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')



class RegistrationForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
            'Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста используйте другое имя.\nЭто имя уже занято.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста используйте другой почтовый ящик.\nЭтот почтовый ящик уже занят.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Email()])
    submit = SubmitField('Запрос сброса пароля')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
            'Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Поменять пароль')
