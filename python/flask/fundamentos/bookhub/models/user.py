from config.connection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL().query_db(query, {'email': email})
        return cls(results[0]) if results else None

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL().query_db(query, {'id': user_id})
        return cls(results[0]) if results else None

    @staticmethod
    def validate_register(data):
        errors = []
        if len(data.get('first_name', '').strip()) < 2:
            errors.append("El nombre debe tener al menos 2 caracteres.")
        if len(data.get('last_name', '').strip()) < 2:
            errors.append("El apellido debe tener al menos 2 caracteres.")
        if not EMAIL_REGEX.match(data.get('email', '')):
            errors.append("El formato del correo electrónico no es válido.")
        elif User.get_by_email(data.get('email', '')):
            errors.append("El correo electrónico ya se encuentra registrado.")
        if len(data.get('password', '')) < 6:
            errors.append("La contraseña debe tener al menos 6 caracteres.")
        if data.get('password') != data.get('confirm_password'):
            errors.append("Las contraseñas no coinciden.")
        return errors