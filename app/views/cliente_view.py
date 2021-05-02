from flask import render_template
from app.forms import cliente_form

from app import app

# @app.route('/ola', defaults={'nome': None}, methods={'GET', 'POST'})
# @app.route('/ola/<string:nome>')
# def hello(nome):
#    return render_template('clientes/teste.html', usuario=nome)

@app.route("/cadastrar_cliente")
def cadastrar_cliente():
    form = cliente_form().ClienteForm()

    return render_template("clientes/form.html", form=form)