from flask import Flask, Blueprint, flash, redirect, url_for, render_template
from src.forms import MotoristasForm
from src.models import Motoristas
from src import db


motorista_create = Blueprint('mot', __name__, template_folder='../frontend/components')

@motorista_create.route('/motorista/view')
def view_motorista():
    mot_list = Motoristas.query.all()
    return render_template('create_driver/view.html', mots=mot_list)

@motorista_create.route('/motorista/new', methods=['POST', 'GET'])
def create_motorista():
    form = MotoristasForm()
    if form.validate_on_submit():
        mot_in_db = Motoristas.query.filter_by(nome=form.nome.data).first()

        if mot_in_db:
            flash(f'Motorista {form.nome.data} ja esta cadastrado!')
            return redirect(url_for('mot.create_motorista'))

        motorista = Motoristas(
            nome = form.nome.data
        )

        db.session.add(motorista)
        db.session.commit()
        
        flash(f'Motorista {form.nome.data} cadastrado com sucesso ;)')
        return redirect(url_for('mot.create_motorista'))
    return render_template('create_driver/create_mot.html', mot=form )


@motorista_create.route('/motorista/<int:id>/delete', methods=['POST'])
def delete_motorista(id):
    mot = Motoristas.query.get_or_404(id)
    db.session.delete(mot)
    db.session.commit()
    flash(f'Motorista deletado com sucesso', 'sucess')
    return redirect(url_for('mot.view_motorista'))


@motorista_create.route('/motorista/<int:id>/update', methods=['POST', 'GET'])
def update_motorista(id):
    motorista_atual = Motoristas.query.get_or_404(id)
    form = MotoristasForm(obj=motorista_atual)

    if form.validate_on_submit():
        form.update(motorista_atual)
        db.session.commit()
        flash(f'Motorista {motorista_atual}, alterado com sucesso!')
        return redirect(url_for('mot.view_motorista'))
    return render_template('create_driver/create_mot.html', mot=form)

# jinja2.exceptions.TemplateAssertionError: block 'content' defined twice