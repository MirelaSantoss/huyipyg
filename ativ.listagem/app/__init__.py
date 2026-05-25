from flask import Flask


def create_app():
    
    app = Flask(__name__, template_folder='views')

    from app.controllers import filme_controller
    app.register_blueprint(filme_controller)
    
    return app