from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange

STATUS_TO_STR = ['На исполнении', 'Выполнено', 'Ждет проверки']


class RegistrationForm(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email('Некорректный адрес')])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    check_password = PasswordField('Повторите пароль:',
                                   validators=[
                                       EqualTo(fieldname='password', message='Пароли не соответствуют друг другу')])
    submit = SubmitField('Зарегистрироваться')


class SettingsForm(FlaskForm):
    name = StringField('Имя:')
    email = StringField('E-mail:', validators=[Email('Некорректный адрес')])
    password = PasswordField('Пароль:')
    check_password = PasswordField('Повторите пароль:',
                                   validators=[
                                       EqualTo(fieldname='password', message='Пароли не соответствуют друг другу')])
    submit = SubmitField('Применить')


class LoginForm(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired(), Email('Некорректный адрес')])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class CreateGroupForm(FlaskForm):
    name = StringField('Имя группы:', validators=[DataRequired()])
    max_members = IntegerField('Максимальное число учеников:',
                               validators=[DataRequired(), NumberRange(2, 100, 'Число должно быть от 2 до 100')])
    submit = SubmitField('Создать')


class JoinGroupForm(FlaskForm):
    id = StringField('ID группы:', validators=[DataRequired()])
    submit = SubmitField('Войти')


class CreateTaskForm(FlaskForm):
    name = StringField('Название:', validators=[DataRequired()])
    description = TextAreaField('Описание:', validators=[DataRequired()])
    status = SelectField('Статус:', choices=[(0, STATUS_TO_STR[0]), (1, STATUS_TO_STR[1]), (2, STATUS_TO_STR[2])],
                         coerce=int, default=0)
    submit = SubmitField('Применить')
