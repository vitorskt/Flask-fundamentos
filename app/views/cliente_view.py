from flask import render_template, redirect, url_for, request
from app.forms import cliente_form
from app import db
from app import app
from app.models import cliente_model
from app.entidades import cliente
from app.services import cliente_service


# @app.route('/ola', defaults={'nome': None}, methods={'GET', 'POST'})
# @app.route('/ola/<string:nome>')
# def hello(nome):
#    return render_template('clientes/teste.html', usuario=nome)

@app.route("/cadastrar_cliente", methods=['GET', 'POST'])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_model.Cliente(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao,
                                        sexo=sexo)

        try:
            cliente_service.cadastrar_cliente(cliente)
            return redirect(url_for("listar_clientes"))
        except:
            print("Erro ao cadastrar o cliente")

    return render_template("clientes/form.html", form=form)


@app.route("/listar_clientes", methods=['GET'])
def listar_clientes():
    clientes = cliente_service.listar_clientes()
    return render_template("clientes/lista_clientes.html", clientes=clientes)


@app.route("/listar_cliente/<int:id>")
def listar_cliente(id):
    cliente = cliente_service.listar_cliente(id)

    return render_template("clientes/lista_cliente.html", cliente=cliente)


@app.route("/editar_cliente/<int:id>", methods=['POST', 'GET'])
def editar_cliente(id):
    cliente_bd = cliente_service.listar_cliente(id)
    form = cliente_form.ClienteForm(obj=cliente_bd)
    form.sexo.data = cliente_bd.sexo

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao, sexo=sexo)

        try:
            cliente_service.editar_cliente(cliente_bd, cliente_novo)
            return redirect(url_for("listar_clientes"))
        except:
            print("Erro ao atualizar o cliente")
    return render_template("clientes/form.html", form=form)


@app.route("/remover_cliente/<int:id>", methods=['GET', 'POST'])
def remover_cliente(id):
    cliente = cliente_service.listar_cliente(id)
    if request.method == 'POST':
        try:
            cliente_service.remover_cliente(cliente)
            return redirect(url_for("listar_clientes"))
        except:
            print("Erro ao remover o cliente")

    return render_template("clientes/remover_cliente.html", cliente=cliente)
