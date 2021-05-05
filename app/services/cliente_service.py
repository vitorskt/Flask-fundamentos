from app.models import cliente_model
from app import db


def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes


def listar_cliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente


def cadastrar_cliente(cliente):
    db.session.add(cliente)
    db.session.commit()


def editar_cliente(cliente_bd, cliente_novo):
    cliente_bd.nome = cliente_novo.nome
    cliente_bd.email = cliente_novo.email
    cliente_bd.data_nascimento = cliente_novo.data_nascimento
    cliente_bd.profissao = cliente_novo.profissao
    cliente_bd.sexo = cliente_novo.sexo
    db.session.commit()


def remover_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()