from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questionnaire.db'
db = SQLAlchemy(app)

from flask_cors import CORS
cors = CORS(app, resources={r"/quizz/api/v1.0/*": {"origins": "*"}})