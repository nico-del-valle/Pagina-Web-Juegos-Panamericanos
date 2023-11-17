from db import db
from flask import Flask, request, render_template, redirect, url_for, jsonify, Response

from utils import validations as val
import os
from werkzeug.utils import secure_filename
import uuid
import filetype


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# definimos path donde guardarmeos los archivos
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ruta de indice
@app.route('/')
def index():
    return render_template('index.html')

# ruta para registrar hincha

@app.route('/registrar_hincha', methods=['GET', 'POST'])
def registrar_hincha():
    if request.method == 'GET':
        regiones = db.get_lista_region()
        deportes = db.get_lista_deportes()
        return render_template('agregar-hincha.html', regiones=regiones, deportes=deportes)
    
    elif request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        region = request.form['region'] 
        comuna = request.form['comuna']
        numero = request.form['numero']
        deportes = request.form.getlist('deportes')  
        transporte = request.form['transporte']
        comentario = request.form['comentario']
        print (comuna)
       
        # validaciones

        valido, error = val.validate_hincha(nombre, email, numero, comentario, deportes, transporte,region,comuna)

        # Si hay algún error, muestra el formulario con los mensajes de error correspondientes
        if not valido:
            regiones = db.get_lista_region()
            deportes = db.get_lista_deportes()
            errores = error.split(".")
            return render_template('agregar-hincha.html', regiones=regiones, deportes=deportes, errores=errores)

        # si no hay errores
        comuna_id = db.get_comuna_by_nombre(comuna)
        status, msg = db.registrar_hincha(nombre, email, numero, comuna_id, comentario, deportes, transporte)
        
        if status:
            return redirect(url_for('index', registered=True))
        error = msg
        regiones = db.get_lista_region()
        deportes = db.get_lista_deportes()
        return render_template('agregar-hincha.html', regiones=regiones, deportes=deportes, error=error)

# ruta para registrar artesano

@app.route('/registrar_artesano', methods=['GET', 'POST'])
def registrar_artesano():
    if request.method == 'GET':
        regiones = db.get_lista_region()
        artesanias = db.get_tipo_artesania()
        return render_template('agregar-artesano.html', regiones=regiones, artesanias=artesanias)

    elif request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        region = request.form['region'] 
        comuna = request.form['comuna']
        numero = request.form['numero']
        tipo = request.form.getlist('artesanias')  
        fotos = request.files.getlist('foto')  
        descripcion = request.form['descripcion']
        
        valido,error = val.validate_artesano(nombre, email, numero, fotos, descripcion,tipo,region,comuna)
        
        if not valido:
            regiones = db.get_lista_region()
            artesanias = db.get_tipo_artesania()
            errores = error.split(".")
            return render_template('agregar-artesano.html', regiones=regiones, artesanias=artesanias, errores=errores)

        # Si no hay errores, registra al artesano
        comuna_id = db.get_comuna_by_nombre(comuna)
        
        status, msg = db.registrar_artesano(nombre, email, numero, comuna_id, descripcion,tipo,fotos)
        # esto podria poner en bd.py
        if status:
            for file in fotos:
                    filename = secure_filename(file.filename)
                    filename = f"{uuid.uuid4()}_{filename}"  # Use UUID to ensure unique filenames
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    db.agregar_fotos_artesano(nombre, filename)  

            return redirect(url_for('index', registered=True))
        error = msg

        regiones = db.get_lista_region()
        artesanias = db.get_tipo_artesania()
        return render_template('agregar-artesano.html', regiones=regiones, artesanias=artesanias, error=error)

# ruta para ver lista de hinchas

@app.route('/ver_hinchas/<int:num>')
def lista_hinchas(num):
    hinchas = db.get_hinchas_pagina(num)
    return render_template('ver-hinchas.html', hinchas=hinchas, get_deportes=db.get_deportes, get_region=db.get_region_by_comuna, num=num)

# ruta para ver datos de hincha especifico

@app.route('/ver-hincha/<int:hincha_id>' , methods=['GET'])
def informacion_hincha(hincha_id):
    hincha = db.get_hincha_by_id_comuna(hincha_id)
    return render_template('informacion-hincha.html', hincha=hincha, get_deportes=db.get_deportes, get_region=db.get_region_by_comuna)

# ruta para ver lista de artesanos

@app.route('/ver-artesanos/<int:num>')
def lista_artesanos(num):
    artesanos = db.get_artesanos_pagina(num)
    return render_template('ver-artesanos.html', artesanos=artesanos, get_tipos=db.get_tipos, get_fotos=db.get_fotos, num=num)

# rutas para ver artesano especifico

@app.route('/ver-artesano/<int:artesano_id>'  , methods=['GET'])
def informacion_artesano(artesano_id):
    artesano = db.get_artesano_by_id_comuna(artesano_id)
    return render_template('informacion-artesano.html', artesano=artesano, get_tipos=db.get_tipos, get_fotos=db.get_fotos, get_region=db.get_region_by_comuna)

# rutas para ver estadisticas

@app.route('/estadisticas')
def stats():
    return render_template('stats.html')

# funcion para obtener las comunas segun region
@app.route('/obtener_comunas/<region>', methods=['GET'])
def obtener_comunas(region):
    comunas = db.get_lista_comunas_by_region(region)
    return jsonify(comunas)


# obtener estadisticas

@app.route('/get-stats-artesanos', methods=['GET'])
def get_stats_artesanos():
    artesanos_data = db.get_cantidad_tipos()
    return jsonify(artesanos_data)

@app.route('/get-stats-hinchas', methods=['GET'])
def get_stats_hinchas():
    deportes_stats = db.get_cantidad_deportes()
    return jsonify(deportes_stats)



# estamos funciones no si siguen siendo utiles

@app.route('/api/total-artisans', methods=['GET'])
def total_artisans():
    total = db.get_cantidad_artesanos()
    return jsonify({'total': total})

# main de la app

if __name__ == '__main__':
    app.run(debug=True)

