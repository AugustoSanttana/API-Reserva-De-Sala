from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1310750412@177.81.186.211:5432/escola'

