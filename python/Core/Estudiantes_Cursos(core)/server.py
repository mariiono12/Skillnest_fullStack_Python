from flask_app import app

# Importar los controladores para que las rutas se registren en la app
from flask_app.controllers import cursos
from flask_app.controllers import estudiantes

if __name__ == "__main__":
    app.run(debug=True)