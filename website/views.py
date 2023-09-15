from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import json

from website import db
from .models import Tarefa

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
#mostra a rota e permite os métodos get e post
@login_required
def home():

    if request.method == 'POST':
        # se o metodo do request for post
        tarefa = request.form.get('tarefa')
        #tarefa vai receber o campo de escrita da tarefa no html
        concluida = request.form.get('concluida')
        #concluida vai receber o value do check box concluida
        afazer = request.form.get('afazer')
        #afazer recebe o value do check box a fazer
        nenhum = request.form.get('nenhum')
        #nenhum recebe o valor do checkbox nenhum
        if concluida == 'concluida':
            concluida = 'Concluída'
        elif afazer == 'afazer':
            afazer = 'A fazer'
        elif nenhum == 'nenhum':
            nenhum = 'Nenhum'
        else:
            nenhum = 'Nenhum'
        # caso algum dos check box seja acionado ele vai receber o status da tarefa que for escrita
        #se não for clicado em nenhum checkbox o status sera nenhum
        if len(tarefa) < 1:
            flash('Texto da tarefa é muito curto!', category='error')
        else:
            nova_tarefa = Tarefa(texto=tarefa, usuario_id=current_user.id, status = afazer or concluida or nenhum)
            #nova tarefa vai receber o texto, seu usuario, e o status
            db.session.add(nova_tarefa)
            db.session.commit()
            # é salvo no banco de dados
            flash("Tarefa incluída!", category="success")
            return redirect(url_for('views.home'))
    
    return render_template("home.html", usuario=current_user)



@views.route('/delete-Tarefa', methods=['POST'])
@login_required
def delete_tarefa():
    data = json.loads(request.data)
    #rebebe o sinal de que o botao de excluir foi acionado
    tarefa_id = data['tarefaId']
    #é salvo o id da tarefa
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        # se o current user for o dono da tarefa ela vai ser excluida do banco de dados
        if tarefa.usuario_id == current_user.id:
            db.session.delete(tarefa)
            db.session.commit()
            flash("Tarefa excluída!", category="success")
    return jsonify({})

@views.route('/altera-concluido', methods=['POST'])
@login_required
def altera_concluido():
    data = json.loads(request.data)
    #rebebe o sinal de que o botao foi acionado
    tarefa_id = data['tarefaId']
    #é salvo o id da tarefa
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        # se o current user for o dono da tarefa a tarefa vai receber o novo status de concluido
        if tarefa.usuario_id == current_user.id:
            tarefa.status = 'Concluída'
            db.session.commit()
            flash('Alterado o status', category = 'success')


@views.route('/altera-afazer', methods=['POST'])
@login_required
def altera_afazer():
    data = json.loads(request.data)
    #rebebe o sinal de que o botao foi acionado
    tarefa_id = data['tarefaId']
    #é salvo o id da tarefa
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        # se o current user for o dono da tarefa a tarefa vai receber o novo status de afazer
        if tarefa.usuario_id == current_user.id:
            tarefa.status = 'A fazer'
            db.session.commit()
            flash('Alterado o status', category = 'success')


@views.route('/altera-nenhum', methods=['POST'])
@login_required
def altera_nenhum():
    data = json.loads(request.data)
    #rebebe o sinal de que o botao foi acionado
    tarefa_id = data['tarefaId']
    #é salvo o id da tarefa
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        # se o current user for o dono da tarefa a tarefa vai receber o novo status de nenhum
        if tarefa.usuario_id == current_user.id:
            tarefa.status = 'Nenhum'
            db.session.commit()
            flash('Altera o status', category= 'success')




   
    




        

