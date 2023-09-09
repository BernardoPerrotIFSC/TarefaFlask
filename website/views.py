from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user

from website import db
from .models import Tarefa

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        tarefa = request.form.get('tarefa')

        if len(tarefa) < 1:
            flash('Texto da nota é muito curto!', category='error')
        else:
            nova_tarefa = Tarefa(texto=tarefa, usuario_id=current_user.id)
            db.session.add(nova_tarefa)
            db.session.commit()
            flash("Nota incluída!", category="success")
            return redirect(url_for('views.home'))
    
    return render_template("home.html", usuario=current_user)

@views.route('/delete-Tarefa', methods=['POST'])
def delete_nota():
    data = json.loads(request.data)
    tarefa_id = data['tarefaId']
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        if tarefa.usuario_id == current_user.id:
            db.session.delete(tarefa)
            db.session.commit()
            flash("Tarefa excluída!", category="success")
    return jsonify({})