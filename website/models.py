from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    tarefas = db.relationship('Tarefa')

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(1000))
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    status = db.Column(db.String(10))