from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from app.models import User



class EditProfileForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField('Отправить')
    
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Пожалуйста используйте другое имя.\nЭто имя уже занято.')


class PostForm(FlaskForm):
    post = TextAreaField('Скажите что-нибудь', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Отправить')

