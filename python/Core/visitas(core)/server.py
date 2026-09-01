from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# Es obligatorio configurar una secret_key para usar 'session'
app.secret_key = 'clave_secreta_super_segura'

@app.route('/')
def inicio():
    # Comprobación e inicialización de la propiedad 'visitas'
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1

    # Comprobación e inicialización del contador de reinicios
    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template('index.html')

@app.route('/sumar_dos', methods=['POST'])
def sumar_dos():
    # Sumamos 1 extra porque la recarga/redirección a '/' sumará otro 1
    if 'visitas' in session:
        session['visitas'] += 1
    return redirect('/')

@app.route('/incrementar_personalizado', methods=['POST'])
def incrementar_personalizado():
    # Obtenemos el número del formulario
    cantidad = request.form.get('cantidad', type=int)
    if cantidad and 'visitas' in session:
        # Descontamos 1 para compensar el incremento automático de la ruta '/'
        session['visitas'] += (cantidad - 1)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    # Reinicia las visitas a 0 y aumenta el contador de reinicios
    session['visitas'] = 0
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1
    return redirect('/')

@app.route('/destruir_sesion')
def destruir_sesion():
    # Elimina completamente todos los datos almacenados en sesión
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)