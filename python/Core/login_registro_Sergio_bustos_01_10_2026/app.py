from flask import Flask
from flask_bcrypt import Bcrypt
from controllers import users

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'
bcrypt = Bcrypt(app)

# Rutas
@app.route('/')
def index():
    return users.index()

@app.route('/register', methods=['POST'])
def register():
    return users.register(bcrypt)

@app.route('/login', methods=['POST'])
def login():
    return users.login(bcrypt)

@app.route('/dashboard')
def dashboard():
    return users.dashboard()

@app.route('/logout')
def logout():
    return users.logout()

if __name__ == '__main__':
    app.run(debug=True)