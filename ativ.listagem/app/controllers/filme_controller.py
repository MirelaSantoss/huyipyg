
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Filme

filme_controller = Blueprint('filmes', __name__)

@filme_controller.route('/')
def index():

    filmes = Filme.listar_filmes()
    return render_template('index.html', filmes=filmes)

@filme_controller.route('/add', methods=['POST'])
def add_filmes():  
    titulo = request.form.get('titulo')
    if titulo:
        Filme.add(titulo)
    return redirect(url_for('filmes.index'))


@filme_controller.route('/completar/<int:filme_id>')
def completar_filme(filme_id):

    Filme.completar(filme_id)
    return redirect(url_for('filmes.index'))

@filme_controller.route('/deletar/<int:filme_id>', methods = ['DELETE'])
def deletar_filme(filme_id):

    Filme.deletar(filme_id)
    return '', 204