import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
 
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.routes.ticket_routes import main
    from src.routes.mot_routes import motorista_create
    from src.routes.placa_routes import placa
    app.register_blueprint(main)
    app.register_blueprint(motorista_create)
    app.register_blueprint(placa)

    with app.app_context():
        db.create_all()

    return app
