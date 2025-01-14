import os
from flask import Flask 
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
metadata = db.metadata

def create_app():
    app = Flask(__name__)
    load_dotenv()

    db_parameters = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST', 'localhost'),
        "port": os.getenv('DB_PORT', '5432'),
        "dbname": os.getenv('DB_NAME')
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['dbname']}"
   

    db.init_app(app)

    migrate = Migrate(app)
    migrate.init_app(app, db)

    from app.resources.auth import auth
    from app.resources import user, card, raffle, home


    app.register_blueprint(auth)
    app.register_blueprint(home, url_prefix="/")

    app.register_blueprint(user, url_prefix='/app/V1/user')
    app.register_blueprint(card, url_prefix='/app/V1/card')
    app.register_blueprint(raffle, url_prefix='/app/V1/raffle')

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app