from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields.html5 import SearchField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SearchReplit(FlaskForm):
	searchType = SelectField('What are you looking for?',
							choices=[
								(1, ' '),
								(2, 'Users'),
								(3, 'Posts')
							],
							validators=[DataRequired()])
	searchData = SearchField('Search Here', validators=[DataRequired()])
	submit = SubmitField('Get Results')

class SearchPost(FlaskForm):
	search_data = SearchField('Post Title', validators=[DataRequired()])
	submit = SubmitField('Search')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
