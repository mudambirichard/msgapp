from flask import Flask , render_template,  flash, redirect, url_for, session, request, logging
from data import Meals
from functools import wraps
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

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return render_template('home.html') 

#=================WELCOME PAGE==========================#
	
@app.route('/welcome')
def welcome():
	return render_template("welcome.html")


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
			#if sha256_crypt.verify(password_candidate, password):
			   #passed
			session['logged_in'] = True
			#session['username'] = username
			
			return redirect(url_for('dashboard'))
        return render_template('login.html', error=error)
#############################################
#########        LOGOUT          ############
#############################################
@app.route('/logout')
@is_logged_in
def logout():
	return redirect(url_for('logout_page'))
@app.route('/api/v1/logout', methods=['GET', 'POST'])
def logout_page():
	session.pop('logged_in', None)
        return redirect(url_for('home'))
   
#====================================dashboard=====================#

@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html', meals = Meals)


#============================edit==========================#

@app.route('/edit_meal', methods=['POST', 'GET'])
def edit_meal():
	
    return render_template('edit_meal.html')
#==========================add page========================#

@app.route('/add_meal', methods=['GET', 'POST'])
@is_logged_in
def add_meal():
	return render_template('add_meal.html')

#==============deletepage=======================#

@app.route('/delete_meal/<string:id>', methods=['POST'])
def delete_meal(id):
    return redirect(url_for('dashboard'))

@app.route('/order_meal')
def order_meal():
	return render_template('order_meal.html')
    #return redirect(url_for('order_meal.html'))
#============================LOGIN PAGE=================================================

@app.route('/view orders')
def vieworders():
	return render_template('view orders.html') 

#====================ABOUTPAGE======================#
@app.route('/post_meals')
@is_logged_in
def post():
	return redirect(url_for('post_meals'))
@app.route('/api/v1/post_meals')
def post_meals():
	return render_template('post_meals.html')


#=======================MEAL PAGE=========================#
@app.route('/meals')
def meals():
	return render_template('meals.html', meals = Meals)

#============MEAL DATA=========================#
@app.route('/meal/<string:id>/')
def meal(id):

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
