import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Inicializamos el objeto Bcrypt
bcrypt = Bcrypt(app)