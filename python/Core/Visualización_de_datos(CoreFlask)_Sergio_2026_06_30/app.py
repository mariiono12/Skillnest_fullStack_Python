from flask import Flask, render_template, request

app = Flask(__name__)

datos = [
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "logo": "https://cdn.simpleicons.org/discord/5865F2"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "logo": "https://cdn.simpleicons.org/instagram/E4405F"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "logo": "https://cdn.simpleicons.org/netflix/E50914"},
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "logo": "https://cdn.simpleicons.org/spotify/1DB954"},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "logo": "https://cdn.simpleicons.org/tiktok/000000"},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "logo": "https://cdn.simpleicons.org/twitch/9146FF"},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "logo": "https://cdn.simpleicons.org/youtube/FF0000"},
]

@app.route('/tabla')
def mostrar_tabla():
    pais_filtro = request.args.get('pais', 'Todos')
    ordenar_por = request.args.get('ordenar', 'nombre')
    direccion = request.args.get('direccion', 'asc')

    lista_filtrada = datos
    if pais_filtro != 'Todos':
        lista_filtrada = [p for p in datos if p['pais'] == pais_filtro]

    reverse_order = (direccion == 'desc')
    if ordenar_por in ['nombre', 'pais', 'fundado']:
        lista_filtrada = sorted(lista_filtrada, key=lambda x: x[ordenar_por], reverse=reverse_order)

    paises_unicos = sorted(list(set(p['pais'] for p in datos)))

    return render_template(
        'tabla.html',
        plataformas=lista_filtrada,
        paises=paises_unicos,
        pais_seleccionado=pais_filtro,
        ordenar_seleccionado=ordenar_por,
        direccion_seleccionada=direccion
    )

if __name__ == "__main__":
    app.run(debug=True)