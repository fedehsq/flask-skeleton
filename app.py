
import os
from flask import Flask
from views.index import index
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['HOST'] = os.getenv('HOST')
    app.config['DEBUG'] = os.getenv('DEBUG')
    app.config['ENV'] = os.getenv('ENV')
    app.config['SERVER'] = os.getenv('SERVER')
    app.register_blueprint(index)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=app.config['SERVER'])
