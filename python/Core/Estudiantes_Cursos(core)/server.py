from flask_app import app

# Importamos los controladores para registrar las rutas en la aplicación
from flask_app.controllers import cursos
from flask_app.controllers import estudiantes

if __name__ == "__main__":
    app.run(debug=True)