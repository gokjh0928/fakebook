from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    # __name__ as reference to current file
    app = Flask(__name__)

    # (configurations, blueprints, additional packages, etc)
    app.config.from_object(config_class)
    
    # Tell the Flask application to use SQLAlchemy and Migrate and LoginManager
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    # now build the rest of the application now that app has been instantiated
    
    # blueprint for main pages
    from app.blueprints.main import bp as main
    app.register_blueprint(main)
    # blueprint for blog related pages
    from app.blueprints.blog import bp as blog
    app.register_blueprint(blog)
    # blueprint for shop related pages
    from app.blueprints.shop import bp as shop
    app.register_blueprint(shop)
    # blueprint for authentication related pages
    from app.blueprints.authentication import bp as authentication
    app.register_blueprint(authentication)

    # tells flask to use this app instance, and use its context
    with app.app_context():
        # build routes(paths) ---> Not needed anymore since each blueprint has own route file
        # from .import routes
        pass
    return app





