import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "clave_secreta_destino"

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form.get('nombre')
    session['edad'] = request.form.get('edad')
    session['color'] = request.form.get('color')
    session['animal'] = request.form.get('animal')
    
    session['numero_suerte'] = random.randint(1, 99)

    predicciones = [
        {"tipo": "buena", "mensaje": "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría."},
        {"tipo": "buena", "mensaje": "Un éxito inesperado llegará a tu vida profesional. Aprovecha las oportunidades."},
        {"tipo": "mala", "mensaje": "Ten precaución con tus decisiones financieras este mes. Mantén la calma ante los retos."}
    ]

    session['prediccion'] = random.choice(predicciones)
    return redirect('/futuro')

@app.route('/futuro')
def futuro():
    if 'nombre' not in session:
        return redirect('/')
    return render_template('futuro.html')

if __name__ == "__main__":
    app.run(debug=True)