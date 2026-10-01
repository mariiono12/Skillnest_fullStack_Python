from flask import render_template, request, redirect, session, flash
from models.user import User

def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

def register(bcrypt):
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
        'password': hashed_pw,
        'birthday': request.form['birthday']
    }

    user_id = User.save(data)
    session['user_id'] = user_id
    flash("¡Registro completado con éxito!", "success")
    return redirect('/dashboard')

def login(bcrypt):
    user = User.get_by_email(request.form.get('email', ''))
    if not user or not bcrypt.check_password_hash(user.password, request.form.get('password', '')):
        flash("Credenciales inválidas. Por favor intenta de nuevo.", 'login_error')
        return redirect('/')

    session['user_id'] = user.id
    return redirect('/dashboard')

def dashboard():
    if 'user_id' not in session:
        flash("Debes iniciar sesión para acceder.", "login_error")
        return redirect('/')
    
    user = User.get_by_id(session['user_id'])
    return render_template('dashboard.html', user=user)

def logout():
    session.clear()
    return redirect('/')