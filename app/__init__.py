from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, static_folder='static/swagger', static_url_path='')
app.config.from_object('app.config')
api = Api(app)

from app import views