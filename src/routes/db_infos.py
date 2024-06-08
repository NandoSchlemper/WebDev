from flask import Blueprint, render_template, url_for, flash, redirect, jsonify
from src import db
from src.models import Placas, Motoristas, LocalCarregamento


DB = Blueprint('Registers', __name__, template_folder='../frontend')

@DB.route('/')
def all_cadastros():
    all_tables = db.metadata.tables.keys()
    return jsonify(f'Tabelas Criadas: {all_tables}')