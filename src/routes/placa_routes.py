from flask import Blueprint, redirect, url_for, render_template, flash
from src.forms import PlacasForm
from src.models import Placas
from src import db

placa = Blueprint('placa', __name__, template_folder='../frontend/components/create_plate')

@placa.route('/placa/view')
def view_placas():
    all_placas = Placas.query.all()
    return render_template('view_placas.html', placas=all_placas)

@placa.route('/placa/create_placa', methods=['POST', 'GET'])
def create_plate():
    form = PlacasForm()

    if form.validate_on_submit():
        criar_placa = Placas(
            placa = form.placa.data,
            motorista = form.motorista.data
        )

        db.session.add(criar_placa)
        db.session.commit()
        return redirect(url_for('placa.create_plate'))
    return render_template('create_plate.html', placa=form)


@placa.route('/placa/<id>/delete', methods=['POST'])
def delete_plate(id):
    placa_alvo = Placas.query.filter_by(id=id)
    db.session.delete(placa_alvo)
    db.session.commit()
    return redirect(url_for('placa.view_placas'))

@placa.route('/placa<id>/update', methods=['POST'])
def update_placa(id):
    placa_alvo = Placas.query.get_or_404(id)
    form = PlacasForm(obj=placa_alvo)

    if form.validate_on_submit():
        form.update(placa_alvo)
        db.session.commit()
        flash(f'Placa {placa_alvo} atualizada! :D')
        return redirect(url_for('placa.view_placas'))
    return render_template('create_plate.html', placa=form)