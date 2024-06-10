from flask import Blueprint, render_template, url_for, flash, redirect, jsonify
from src import db
from src.models import Tickets
from src.forms import TicketForm

main = Blueprint('main', __name__, template_folder='../frontend/components/create_ticket')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/item/view')
def view():
    all_tickets = Tickets.query.all()
    return render_template('view.html', tickets=all_tickets)

@main.route('/item/new', methods=['POST', 'GET'])
def new_ticket():
    form = TicketForm()
    if form.validate_on_submit():
        existing_ticket = Tickets.query.filter_by(nfe=form.nfe.data).first()
        if existing_ticket:
            flash(f'O ticket com NFE {form.nfe.data} ja existe', 'danger')
            return redirect(url_for('main.new_ticket'))
        
        ticket = Tickets(carregamento = form.carregamento.data,
                         nfe = form.nfe.data,
                         placa = form.placa.data,
                         tara = form.tara.data,
                         peso_total = form.peso_total.data,
                         excesso = form.excesso.data)
        # Instanciamos o objeto ticket
        
        db.session.add(ticket)
        # Adicionamos o ticket no DB
        db.session.commit()
        # Damos um commit nas alteracoes de valores do DB
        flash(f'O ticket {ticket.nfe} foi adicionado! :)', 'success')
        return redirect(url_for('main.new_ticket', ticket_id=ticket.nfe))
    
    return render_template('create.html', form=form)

@main.route('/item/<int:nfe>/delete', methods=['POST'])
def delete_ticket(nfe):
    item = Tickets.query.get_or_404(nfe)
    db.session.delete(item)
    db.session.commit()
    flash(f'Ticket numero: {nfe} deletado!', 'success')
    return redirect(url_for('main.index'))

from src.models import LocalCarregamento
from src.forms import LocalCarregamentoForm

@main.route('/item/carregamento/view')
def view_carregamento():
    all_locals = LocalCarregamento.query.all()
    return render_template('view_carregamento.html', carregamentos=all_locals)

@main.route('/item/carregamento/new', methods=['POST', 'GET'])
def create_carregamento():
    form = LocalCarregamentoForm()

    if form.validate_on_submit():
        new_carregamento = LocalCarregamento(
            local = form.local.data,
            gps = form.gps.data
        )

        db.session.add(new_carregamento)
        db.session.commit()
        flash(f'Local de carregamento: {new_carregamento.local} foi criado!')
        return redirect(url_for('main.view_carregamento'))
    return render_template('create_carregamento.html', carregamento=form)

@main.route('/item/<id>/delete_carregamneto', methods=['POST'])
def delete_carregamento(id):
    search_carregamento = LocalCarregamento.query.get_or_404(id)
    db.session.delete(search_carregamento)
    db.session.commit()
    return redirect(url_for('main.view_carregamento'))

@main.route('/item/<id>/update_carregamneto', methods=['POST'])
def update_carregamento(id):
    search_carregamento = LocalCarregamento.query.get_or_404(id)
    form = LocalCarregamentoForm(obj=search_carregamento)

    if form.validate_on_submit():
        form.update(search_carregamento)
        db.session.commit()
        flash(f'Local do carregamento cadastrado com sucesso')
        return redirect(url_for('main.view_carregamento'))
    return render_template('create_carregamento.html', carregamento=form)