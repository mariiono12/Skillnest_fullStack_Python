from config.connection import connectToMySQL
import re
from datetime import datetime, date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.birthday = data['birthday']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password, birthday)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(birthday)s);
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
        
        # Validar Nombre
        first_name = data.get('first_name', '').strip()
        if len(first_name) < 2:
            errors.append("El nombre debe tener al menos 2 caracteres.")
        elif not NAME_REGEX.match(first_name):
            errors.append("El nombre solo debe contener letras.")

        # Validar Apellido
        last_name = data.get('last_name', '').strip()
        if len(last_name) < 2:
            errors.append("El apellido debe tener al menos 2 caracteres.")
        elif not NAME_REGEX.match(last_name):
            errors.append("El apellido solo debe contener letras.")

        # Validar Email
        email = data.get('email', '').strip()
        if not EMAIL_REGEX.match(email):
            errors.append("Formato de correo electrónico no válido.")
        elif User.get_by_email(email):
            errors.append("El correo ya se encuentra registrado.")

        # BONUS ORO: Validar Fecha de Nacimiento (Mayor de 18 años)
        birthday_str = data.get('birthday', '')
        if not birthday_str:
            errors.append("Debes ingresar tu fecha de nacimiento.")
        else:
            try:
                birth_date = datetime.strptime(birthday_str, '%Y-%m-%d').date()
                today = date.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                if age < 18:
                    errors.append("Debes ser mayor de 18 años para registrarte.")
            except ValueError:
                errors.append("La fecha de nacimiento ingresada no es válida.")

        # Validar Contraseña
        password = data.get('password', '')
        if len(password) < 8:
            errors.append("La contraseña debe tener al menos 8 caracteres.")
        # BONUS PLATA: Al menos una mayúscula y un número
        elif not PASSWORD_REGEX.match(password):
            errors.append("La contraseña debe incluir al menos un número y una letra mayúscula.")

        # Confirmación de contraseña
        if password != data.get('confirm_password', ''):
            errors.append("Las contraseñas no coinciden.")

        return errors