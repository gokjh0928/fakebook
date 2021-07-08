from flask import Flask
from config import Config

def create_app(config_class=Config):
    # __name__ as reference to current file
    app = Flask(__name__)
    
    # now build the rest of the application now that app has been instantiated
    # (configurations, blueprints, additional packages, etc)
    app.config.from_object(config_class)  
    
    # blueprint for main pages
    from app.blueprints.main import bp as main
    app.register_blueprint(main)
    # blueprint for blog related pages
    from app.blueprints.blog import bp as blog
    app.register_blueprint(blog)
    # blueprint for shop related pages
    from app.blueprints.shop import bp as shop
    app.register_blueprint(shop)

    # tells flask to use this app instance, and use its context
    with app.app_context():
        # build routes(paths) ---> Not needed anymore since each blueprint has own route file
        # from .import routes
        pass
    return app





