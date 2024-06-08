import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='frontend/static/js/build', static_url_path='/')

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.routes.ticket_routes import main
    from src.routes.db_infos import DB
    app.register_blueprint(main)
    app.register_blueprint(DB, url_prefix='/db')

    with app.app_context():
        db.create_all()

    return app
