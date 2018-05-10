from flask import Flask , render_template,  flash, redirect, url_for, session, request, logging
from data import Meals
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

Meals = Meals()

#check if user logout in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorised, Please login', 'danger')
			return redirect(url_for('login'))
	return wrap
#========================INDEX / HOME PAGE========================#
@app.route('/')
def index():
	return render_template('home.html')


 #=======================LOGIN PAGE================================================#

@app.route('/login')
def login():
	return redirect(url_for('login_page'))
@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login_page():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin'  or  request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

#============================LOGIN PAGE==================================================#

@app.route('/home')
def home():
	return render_template('home.html') 

#=================WELCOME PAGE==========================#
	
@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

#====================ABOUTPAGE======================#

@app.route('/about')
def about():
	return render_template('about.html')


#=======================MEAL PAGE=========================#
@app.route('/meals')
def meals():
	return render_template('meals.html', meals = Meals)


	if result > 0:
		return render_template('meals.html', meals=meals)
	else:
		msg = 'No Meals Found'
		return render_template('meals.html', msg=msg)



#============MEAL DATA=========================#
@app.route('/meal/<string:title>/')
def meal(title):

	return render_template('meal.html', meal=meal)

# =============REGISTER PAG=================#

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
		])
	confirm = PasswordField('Confirm Password')


#=================REGISTER PAGE=========================#
@app.route('/register')
def register():
	return redirect(url_for('register_page'))
@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def register_page():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.d

		return redirect(url_for('login'))
        return render_template('register.html', form=form)




if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(debug=True)
