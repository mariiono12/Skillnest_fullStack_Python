from flask import Flask

app = Flask(__name__)
# Necesaria para usar mensajes flash() y session
app.secret_key = "clave_secreta_usuarios_val"
