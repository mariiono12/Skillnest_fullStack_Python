from config.connection import connectToMySQL
from datetime import datetime

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.genre = data['genre']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.creator_name = data.get('creator_name', '')
        self.favorites_count = data.get('favorites_count', 0)

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO books (title, author, genre, release_date, description, user_id)
            VALUES (%(title)s, %(author)s, %(genre)s, %(release_date)s, %(description)s, %(user_id)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
            UPDATE books
            SET title = %(title)s, author = %(author)s, genre = %(genre)s,
                release_date = %(release_date)s, description = %(description)s
            WHERE id = %(id)s AND user_id = %(user_id)s;
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, book_id, user_id):
        query = "DELETE FROM books WHERE id = %(id)s AND user_id = %(user_id)s;"
        return connectToMySQL().query_db(query, {'id': book_id, 'user_id': user_id})

    @classmethod
    def get_by_id(cls, book_id):
        query = """
            SELECT b.*, CONCAT(u.first_name, ' ', u.last_name) AS creator_name,
                   (SELECT COUNT(*) FROM favorites WHERE book_id = b.id) AS favorites_count
            FROM books b
            JOIN users u ON b.user_id = u.id
            WHERE b.id = %(id)s;
        """
        results = connectToMySQL().query_db(query, {'id': book_id})
        return cls(results[0]) if results else None

    @classmethod
    def get_user_books(cls, user_id):
        query = """
            SELECT b.*, (SELECT COUNT(*) FROM favorites WHERE book_id = b.id) AS favorites_count
            FROM books b
            WHERE b.user_id = %(user_id)s
            ORDER BY b.created_at DESC;
        """
        results = connectToMySQL().query_db(query, {'user_id': user_id})
        return [cls(row) for row in results] if results else []

    @classmethod
    def get_community_books(cls, user_id):
        query = """
            SELECT b.*, u.first_name AS creator_name,
                   (SELECT COUNT(*) FROM favorites WHERE book_id = b.id) AS favorites_count
            FROM books b
            JOIN users u ON b.user_id = u.id
            WHERE b.user_id != %(user_id)s
            ORDER BY b.created_at DESC;
        """
        results = connectToMySQL().query_db(query, {'user_id': user_id})
        return [cls(row) for row in results] if results else []

    @classmethod
    def add_favorite(cls, user_id, book_id):
        query = "INSERT IGNORE INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL().query_db(query, {'user_id': user_id, 'book_id': book_id})

    @classmethod
    def is_favorited_by_user(cls, user_id, book_id):
        query = "SELECT * FROM favorites WHERE user_id = %(user_id)s AND book_id = %(book_id)s;"
        results = connectToMySQL().query_db(query, {'user_id': user_id, 'book_id': book_id})
        return len(results) > 0

    @classmethod
    def get_favorited_users(cls, book_id):
        query = """
            SELECT u.first_name, u.last_name
            FROM favorites f
            JOIN users u ON f.user_id = u.id
            WHERE f.book_id = %(book_id)s;
        """
        return connectToMySQL().query_db(query, {'book_id': book_id}) or []

    @classmethod
    def get_user_favorites(cls, user_id):
        query = """
            SELECT b.*, u.first_name AS creator_name
            FROM favorites f
            JOIN books b ON f.book_id = b.id
            JOIN users u ON b.user_id = u.id
            WHERE f.user_id = %(user_id)s;
        """
        results = connectToMySQL().query_db(query, {'user_id': user_id})
        return [cls(row) for row in results] if results else []

    @staticmethod
    def validate(data):
        errors = []
        if len(data.get('title', '').strip()) < 2:
            errors.append("El título debe tener al menos 2 caracteres.")
        if len(data.get('author', '').strip()) < 2:
            errors.append("El autor es obligatorio.")
        if not data.get('genre'):
            errors.append("Debes seleccionar un género.")
        
        release_date = data.get('release_date')
        if not release_date:
            errors.append("La fecha de publicación es obligatoria.")
        else:
            try:
                date_val = datetime.strptime(release_date, '%Y-%m-%d').date()
                if date_val > datetime.now().date():
                    errors.append("La fecha de publicación no puede ser futura.")
            except ValueError:
                errors.append("La fecha ingresada no es válida.")

        if len(data.get('description', '').strip()) < 10:
            errors.append("La descripción debe tener al menos 10 caracteres.")

        return errors