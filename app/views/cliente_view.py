from flask import render_template
from app import app


@app.route('/ola', defaults={'nome': None}, methods={'GET', 'POST'})
@app.route('/ola/<string:nome>')
def hello(nome):
    return render_template('clientes/teste.html', usuario=nome)
