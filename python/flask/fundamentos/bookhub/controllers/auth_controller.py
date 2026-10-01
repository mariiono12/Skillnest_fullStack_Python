from flask import render_template, request, redirect, session, flash
from models.user import User

def register_view():
    if 'user_id' in session:
        return redirect('/libros')
    return render_template('auth/login_register.html')

def register_process(bcrypt):
    errors = User.validate_register(request.form)
    if errors:
        for err in errors:
            flash(err, 'register_error')
        return redirect('/')

    hashed_pw = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['user_name'] = data['first_name']
    flash("¡Registro exitoso!", "success")
    return redirect('/libros')

def login_process(bcrypt):
    user = User.get_by_email(request.form.get('email', ''))
    if not user or not bcrypt.check_password_hash(user.password, request.form.get('password', '')):
        flash("Credenciales inválidas. Verifica tu correo y contraseña.", 'login_error')
        return redirect('/')

    session['user_id'] = user.id
    session['user_name'] = user.first_name
    return redirect('/libros')

def logout():
    session.clear()
    return redirect('/')