from flask import Flask
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

# Controladores
from controllers import auth_controller, book_controller

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'clave_super_secret_123')
bcrypt = Bcrypt(app)

# --- RUTAS DE AUTENTICACIÓN ---
@app.route('/')
def index():
    return auth_controller.register_view()

@app.route('/register', methods=['POST'])
def register():
    return auth_controller.register_process(bcrypt)

@app.route('/login', methods=['POST'])
def login():
    return auth_controller.login_process(bcrypt)

@app.route('/logout')
def logout():
    return auth_controller.logout()

# --- RUTAS DE LIBROS (CRUD & FAVORITOS) ---
@app.route('/libros')
def books_index():
    return book_controller.index()

@app.route('/libros/nuevo')
def book_new():
    return book_controller.new_book()

@app.route('/libros/crear', methods=['POST'])
def book_create():
    return book_controller.create_book()

@app.route('/libros/<int:book_id>')
def book_show(book_id):
    return book_controller.show_book(book_id)

@app.route('/libros/editar/<int:book_id>')
def book_edit(book_id):
    return book_controller.edit_book(book_id)

@app.route('/libros/actualizar/<int:book_id>', methods=['POST'])
def book_update(book_id):
    return book_controller.update_book(book_id)

@app.route('/libros/eliminar/<int:book_id>')
def book_delete(book_id):
    return book_controller.delete_book(book_id)

@app.route('/libros/favorito/<int:book_id>')
def book_favorite(book_id):
    return book_controller.add_favorite(book_id)

@app.route('/favoritos')
def favorites():
    return book_controller.favorites()

if __name__ == '__main__':
    app.run(debug=True)