from flask import Blueprint, render_template, request,redirect,url_for, flash
from ..models.user import User
from .. import db
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
          print(request.form)
          email = request.form.get('email')
          password = request.form.get('password')
          user = User.query.filter_by(email=email).first()
          if user:
              if check_password_hash(user.password, password):
                  flash('Logged in successfully!', category='success')
                  login_user(user, remember=True)
                  return redirect(url_for('home_routes.home'))
              else:
                  flash('Incorrect password, try again.', category='danger')
          else:
              flash('Email does not exist.', category='danger')
        
     return render_template("login.html") 

@auth_routes.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
     if request.method == 'POST':
          formData = request.form
          email = formData.get('email')
          first_name = formData.get('first_name')
          password = formData.get('password')
          confirm_password = formData.get('confirm_password')
        #   print(f"Email: {email}, First Name: {first_name}, Password: {password}, Confirm Password: {confirm_password}")
          user = User.query.filter_by(email=email).first()
          if user:
            flash('Email already exists.', category='danger')
          elif password != confirm_password:
            flash('Passwords don\'t match.', category='danger')
          else:
            hash_pass = generate_password_hash(password, method='sha256')
            new_user = User(email=email, first_name=first_name, password=hash_pass)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)#remember user after there session is expires
            flash('Account created!', category='success')
            return redirect(url_for('home_routes.home'))

            

     return render_template("sign_up.html") 

@auth_routes.route('/logout')
#If you decorate a view with this, it will ensure that the current user
#  is logged in and authenticated before calling the actual view.
@login_required
def logout():
    logout_user()#Logs a user out.
    return redirect(url_for('auth_routes.login'))
