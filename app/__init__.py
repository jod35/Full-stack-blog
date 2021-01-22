from flask import Flask
from .config import DevConfig,TestConfig,ProdConfig
from .models import Post,Comment,User
from decouple import config
from .utils import db
from .api import resources

def create_app():

    app=Flask(__name__)
    
    app.config.from_object(DevConfig)
    db.init_app(app)

    app.register_blueprint(resources,url_prefix='/api')

    @app.shell_context_processor
    def make_shell_context():
        return {
            "app":app,
            "db":db,
            'User':User,
            'Post':Post,
            'Comment':Comment
             }

    
    return app
