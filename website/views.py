from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import json

from website import db
from .models import Tarefa

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        tarefa = request.form.get('tarefa')
        concluida = request.form.get('concluida')
        afazer = request.form.get('afazer')
        if concluida == 'marcada':
            concluida = 'Concluída'
        if afazer == 'marcada':
            afazer = 'A fazer'
            
        if len(tarefa) < 1:
            flash('Texto da tarefa é muito curto!', category='error')
        else:
            nova_tarefa = Tarefa(texto=tarefa, usuario_id=current_user.id, status = afazer or concluida)
            db.session.add(nova_tarefa)
            db.session.commit()
            flash("Nota incluída!", category="success")
            return redirect(url_for('views.home'))
    
    return render_template("home.html", usuario=current_user)

# @views.route('/alterar-Tarefa', methods=['POST', 'GET'])
# def altera_tarefa():
#     concluida = request.form.get('concluida2')
#     afazer = request.form.get('afazer2')
#     if concluida == 'marcada':


@views.route('/delete-Tarefa', methods=['POST'])
def delete_tarefa():
    data = json.loads(request.data)
    tarefa_id = data['tarefaId']
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        if tarefa.usuario_id == current_user.id:
            db.session.delete(tarefa)
            db.session.commit()
            flash("Tarefa excluída!", category="success")
    return jsonify({})

@views.route('/altera-concluido', methods=['POST'])
def altera_concluido():
    data = json.loads(request.data)
    tarefa_id = data['tarefaId']
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        if tarefa.usuario_id == current_user.id:
            tarefa.status = 'Concluída'
            db.session.commit()
            flash('Alterado o status', catgory = 'success')


@views.route('/altera-afazer', methods=['POST'])
def altera_afazer():
    data = json.loads(request.data)
    tarefa_id = data['tarefaId']
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        if tarefa.usuario_id == current_user.id:
            tarefa.status = 'A fazer'
            db.session.commit()
            flash('Alterado o status', category = 'success')


        

