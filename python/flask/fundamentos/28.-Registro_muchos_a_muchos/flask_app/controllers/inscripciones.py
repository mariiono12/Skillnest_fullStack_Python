from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.models.inscripcion import Inscripcion
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso


@app.route("/")
def index():
    estudiantes = Estudiante.get_all()
    cursos = Curso.get_all()
    inscripciones = Inscripcion.get_all()
    return render_template(
        "index.html",
        estudiantes=estudiantes,
        cursos=cursos,
        inscripciones=inscripciones
    )

   


@app.route("/inscribir", methods=["POST"])
def inscribir():
    estudiante_id = request.form.get("estudiante_id")
    curso_id = request.form.get("curso_id")

    if not estudiante_id or not curso_id:
        flash("Debes seleccionar un estudiante y un curso.", "danger")
        return redirect("/")

    datos = {
        "estudiante_id": estudiante_id,
        "curso_id": curso_id
    }

    if Inscripcion.existe(datos):
        flash("El estudiante ya está inscrito en este curso.", "warning")
        return redirect("/")

    Inscripcion.inscribir_estudiante_en_curso(datos)
    flash("Inscripción realizada con éxito.", "success")
    return redirect("/")

@app.route("/estudiante/eliminar/<int:id>")
def eliminar_estudiante(id):
        Estudiante.delete(id)
        flash("Estudiante eliminado correctamente.", "warning")
        return redirect("/")