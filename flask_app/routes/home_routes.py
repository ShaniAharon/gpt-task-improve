from flask import Blueprint, render_template
from flask_login import login_required, current_user #acsses to logedin user data we need

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/', methods=['GET'])
@login_required
def home():
     return render_template("home.html", user=current_user) 


