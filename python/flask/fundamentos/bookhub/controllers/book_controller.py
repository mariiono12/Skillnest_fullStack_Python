from flask import render_template, request, redirect, session, flash
from models.book import Book

def check_session():
    return 'user_id' in session

def index():
    if not check_session():
        return redirect('/')
    user_id = session['user_id']
    my_books = Book.get_user_books(user_id)
    community_books = Book.get_community_books(user_id)
    return render_template('books/index.html', my_books=my_books, community_books=community_books)

def new_book():
    if not check_session():
        return redirect('/')
    return render_template('books/new.html')

def create_book():
    if not check_session():
        return redirect('/')

    errors = Book.validate(request.form)
    if errors:
        for err in errors:
            flash(err, 'book_error')
        return redirect('/libros/nuevo')

    data = {
        'title': request.form['title'],
        'author': request.form['author'],
        'genre': request.form['genre'],
        'release_date': request.form['release_date'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    Book.save(data)
    flash("Libro agregado exitosamente", "success")
    return redirect('/libros')

def show_book(book_id):
    if not check_session():
        return redirect('/')

    book = Book.get_by_id(book_id)
    if not book:
        flash("Libro no encontrado.", "danger")
        return redirect('/libros')

    is_fav = Book.is_favorited_by_user(session['user_id'], book_id)
    fav_users = Book.get_favorited_users(book_id)

    return render_template('books/show.html', book=book, is_fav=is_fav, fav_users=fav_users)

def edit_book(book_id):
    if not check_session():
        return redirect('/')

    book = Book.get_by_id(book_id)
    if not book or book.user_id != session['user_id']:
        flash("No tienes permiso para editar este libro.", "danger")
        return redirect('/libros')

    return render_template('books/edit.html', book=book)

def update_book(book_id):
    if not check_session():
        return redirect('/')

    book = Book.get_by_id(book_id)
    if not book or book.user_id != session['user_id']:
        flash("Acción no autorizada.", "danger")
        return redirect('/libros')

    errors = Book.validate(request.form)
    if errors:
        for err in errors:
            flash(err, 'book_error')
        return redirect(f'/libros/editar/{book_id}')

    data = {
        'id': book_id,
        'title': request.form['title'],
        'author': request.form['author'],
        'genre': request.form['genre'],
        'release_date': request.form['release_date'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    Book.update(data)
    flash("Libro actualizado con éxito.", "success")
    return redirect('/libros')

def delete_book(book_id):
    if not check_session():
        return redirect('/')

    Book.delete(book_id, session['user_id'])
    flash("Libro eliminado.", "warning")
    return redirect('/libros')

def add_favorite(book_id):
    if not check_session():
        return redirect('/')

    Book.add_favorite(session['user_id'], book_id)
    return redirect(f'/libros/{book_id}')

def favorites():
    if not check_session():
        return redirect('/')

    fav_books = Book.get_user_favorites(session['user_id'])
    return render_template('books/favorites.html', fav_books=fav_books)