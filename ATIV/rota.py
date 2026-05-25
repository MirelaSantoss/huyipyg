from flask import render_template
from models import cliente

@cliente.route('/')
def home():
    return render_template('home.html')

