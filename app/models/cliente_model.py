from app import db
from sqlalchemy_utils import ChoiceType


class Cliente(db.Model):
    __tablename__ = "clientes"

    SEXO_CHOICES = [
        (u'M', u"Masculino"),
        (u'F', u"Feminino"),
        (u'N', u"Não Binário")
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    data_nascimento = db.Column(db.DateTime)
    profissao = db.Column(db.String(30))
    sexo = db.Column(ChoiceType(SEXO_CHOICES))
