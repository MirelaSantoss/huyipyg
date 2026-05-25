from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente import Clientes

cliente_controllers = Blueprint('cliente', __name__)

@cliente_controllers.route('/')
def index():

    cliente = Clientes.listar_cliente()
    return render_template('index.html', cliente = cliente)

@cliente_controllers.route('/add', methods=['POST'])
def add_cliente():  
    nome = request.form.get('nome')
    if nome:
        Clientes.add(nome)
    return redirect(url_for('cliente.index'))