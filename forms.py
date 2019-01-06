from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, BooleanField,PasswordField
from wtforms.validators import Required

class LoginForm(Form):
	name = StringField('username', validators=[Required()]) 
	password = StringField('username', validators=[Required()]) 
	submit = SubmitField('Submit')
	openid = TextField('openid', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)
