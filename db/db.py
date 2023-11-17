import json
import pymysql

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"
# carpeta donde se guardan las fotos
UPLOAD_FOLDER = r'tarea_2\static\uploads'

def get_conn():
    conn = pymysql.connect(
        db=DB_NAME,
        user=DB_USERNAME,
        passwd=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    return conn

# consultas para artesanos

def get_artesano_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM artesano WHERE id = %s", (id))
    artesano = cursor.fetchone()
    return artesano

# esta rara esta funcion (entregarle el id de la comuna devuelve multiples artesanos)
def get_artesano_by_id_comuna(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT artesano.id, comuna.nombre, descripcion_artesania, artesano.nombre, email, celular FROM artesano, comuna WHERE artesano.comuna_id=comuna.id AND artesano.id = %s", (id))
    artesanos = cursor.fetchone()
    return artesanos

def get_artesano_by_email(email):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM artesano WHERE email = %s", (email))
    artesano = cursor.fetchone()
    return artesano

def get_artesano_by_nombre(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM artesano WHERE nombre = %s", (nombre))
    artesano = cursor.fetchone()
    return artesano
    
def get_artesano_by_numero(numero):
    conn = get_conn()
    cursor = conn.cursor()
    if numero is not None and numero != '':
        cursor.execute("SELECT * FROM artesano WHERE celular = %s", (numero))
        artesano = cursor.fetchone()
        return artesano
    return None

def get_lista_artesanos(artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM artesano WHERE artesano = %s", (artesano))
    artesano = cursor.fetchone() # puede ser fetchall, creo
    return artesano

def get_artesanos_pagina(pagina):   
    pag = 5*(pagina-1)
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT artesano.id, comuna.nombre, descripcion_artesania, artesano.nombre, email, celular FROM artesano, comuna WHERE artesano.comuna_id=comuna.id ORDER BY id DESC LIMIT %s, 5", (pag))
    artesanos = cursor.fetchall()
    return artesanos

def get_tipos(artesano):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM artesano WHERE nombre = %s", (artesano,))
    artesano_id = cursor.fetchone()[0]
    cursor.execute("SELECT tipo_artesania_id FROM artesano_tipo WHERE artesano_id = %s", (artesano_id,))
    id_artesanias = cursor.fetchall()
    nombres_artesanias = []
    for id_artesania in id_artesanias:
        cursor.execute("SELECT nombre FROM tipo_artesania WHERE id = %s", (id_artesania[0],))
        nombre_artesania = cursor.fetchone()
        nombres_artesanias.append(nombre_artesania[0])

    return nombres_artesanias

def get_fotos(artesano_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_archivo FROM foto WHERE artesano_id = %s", (artesano_id,))
    fotos = cursor.fetchall()
    return fotos

def get_region_by_comuna(comuna):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM region WHERE id = (SELECT region_id FROM comuna WHERE nombre = %s)", (comuna))
    region = cursor.fetchone()
    return region[0]

def get_cantidad_artesanos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM artesano")
    total = cursor.fetchone()
    return total

# consultas para hinchas

def get_hincha_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hincha WHERE id = %s", (id))
    hincha = cursor.fetchone()
    return hincha

def get_hincha_by_email(email):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hincha WHERE email = %s", (email))
    hincha = cursor.fetchone()
    return hincha

def get_hincha_by_nombre(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hincha WHERE nombre = %s", (nombre))
    hincha = cursor.fetchone()
    return hincha

def get_hincha_by_numero(numero):
    conn = get_conn()
    cursor = conn.cursor()
    if numero is not None and numero != '':
        cursor.execute("SELECT * FROM hincha WHERE celular = %s", (numero))
        hincha = cursor.fetchone()
        return hincha
    return None

def get_deportes(hincha):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM hincha WHERE nombre = %s", (hincha,))
    hincha_id = cursor.fetchone()[0]
    cursor.execute("SELECT deporte_id FROM hincha_deporte WHERE hincha_id = %s", (hincha_id,))
    id_deportes = cursor.fetchall()
    nombres_deportes = []
    for id_deporte in id_deportes:
        cursor.execute("SELECT nombre FROM deporte WHERE id = %s", (id_deporte[0],))
        nombre_deporte = cursor.fetchone()
        nombres_deportes.append(nombre_deporte[0])

    return nombres_deportes

def get_lista_hinchas(hincha):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hincha WHERE hincha = %s", (hincha))
    hinchas = cursor.fetchone() # puede ser fetchall, creo
    return hinchas

def get_hinchas_pagina(pagina):
    pag = 5*(pagina-1)
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT hincha.id, comuna.nombre, modo_transporte, hincha.nombre, email, celular FROM hincha, comuna WHERE hincha.comuna_id=comuna.id ORDER BY id DESC LIMIT %s, 5", (pag))
    hinchas = cursor.fetchall()
    return hinchas

# creamos artesano en la base da datos

def crear_artesano(comuna_id, descripcion, nombre, numero, email ):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s, %s, %s, %s, %s)", (comuna_id, descripcion, nombre, email, numero))
    conn.commit()
    
def agregar_tipos_artesano(artesano, tipos):
    conn = get_conn()
    cursor = conn.cursor()

    for tipo in tipos:
        cursor.execute("SELECT id FROM tipo_artesania WHERE nombre = %s", (tipo))
        tipo_id = cursor.fetchone()

        if tipo_id is not None:
            cursor.execute("SELECT id FROM artesano WHERE nombre = %s", (artesano))
            artesano_id  = cursor.fetchone()
            cursor.execute("INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s,%s)", (artesano_id, tipo_id))
            conn.commit()

def agregar_fotos_artesano(artesano, fotos):
    conn = get_conn()
    cursor = conn.cursor()
    # conseguir el id del artesano
    cursor.execute("SELECT id FROM artesano WHERE nombre = %s", (artesano))
    artesano_id = cursor.fetchone()
    cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s, %s, %s)", (UPLOAD_FOLDER, fotos, artesano_id))
    conn.commit()

# insertamos un artesano en la base de datos

def registrar_artesano(nombre, email, numero, comuna_id, descripcion,tipos, fotos):
    # validar que no exista un artesano con el mismo email
    error = ''
    _email_artesano = get_artesano_by_email(email)
    if _email_artesano is not None:
        error += "El correo ya esta en uso."
        return False, error
    
    # validar que no este ya registrado (vamos a asumir que no hay 2 artesanos con el mismo nombre, explicar en el README)
    _nombre_artesano = get_artesano_by_nombre(nombre)
    if _nombre_artesano is not None:
        error += "El artesano ya esta registrado."
        return False, error
    
    # validamos que no exista un artesano con el mismo numero de telefono
    _numero_artesano = get_artesano_by_numero(numero)
    if _numero_artesano is not None:
        error += "El numero de telefono ya esta en uso."
        return False, error
    
    crear_artesano(comuna_id, descripcion, nombre, numero, email )
    agregar_tipos_artesano(nombre, tipos)   
    return True, None

# creamos hincha en la base da datos

def crear_hincha(comuna_id, transporte, nombre, email, numero, comentario):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hincha (comuna_id, modo_transporte, nombre, email, celular, comentarios) VALUES (%s, %s, %s, %s, %s, %s)", (comuna_id, transporte, nombre, email, numero, comentario))
    conn.commit()

def registrar_hincha(nombre, email, numero, comuna_id, comentario, deportes, transporte):
    # validar que no exista un hincha con el mismo email
    error = ''
    _email_hincha = get_hincha_by_email(email)
    if _email_hincha is not None:
        error += "El correo ya esta en uso."
        return False, error
    
    # validar que no este ya registrado (vamos a asumir que no hay 2 hinchas con el mismo nombre, explicar en el README)
    _nombre_hincha = get_hincha_by_nombre(nombre)
    if _nombre_hincha is not None:
        error += "El hincha ya esta registrado."
        return False, error
    
    # validamos que no exista un hincha con el mismo numero de telefono
    _numero_hincha = get_hincha_by_numero(numero)
    if _numero_hincha is not None:
        error += "El numero de telefono ya esta en uso."
        return False, error
    
    crear_hincha(comuna_id, transporte, nombre, email, numero, comentario)
    agregar_hincha_deportes(nombre, deportes)   
    return True, None

def agregar_hincha_deportes(hincha, deportes):
    conn = get_conn()
    cursor = conn.cursor()

    for deporte in deportes:
        cursor.execute("SELECT id FROM deporte WHERE nombre = %s", (deporte))
        deporte_id = cursor.fetchone()

        if deporte_id is not None:
            cursor.execute("SELECT id FROM hincha WHERE nombre = %s", (hincha))
            hincha_id  = cursor.fetchone()
            cursor.execute("INSERT INTO hincha_deporte (hincha_id, deporte_id) VALUES (%s,%s)", (hincha_id, deporte_id))
            conn.commit()

# conseguir la lista de regiones
def get_lista_region():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM region")
    regiones = [region[0] for region in cursor.fetchall()]
    return regiones
    
# a partir del nombre de la region recuperamos su id
def get_region_id(region):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM region WHERE nombre = %s", (region))
    id = cursor.fetchone()
    return id

# conseguir la lista de comuna segun la id de la region
def get_lista_comunas_by_region(region):
    region_id = get_region_id(region)
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM comuna WHERE region_id = %s", (region_id))
    comunas = cursor.fetchall()
    return comunas

def get_comuna_by_nombre(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM comuna WHERE nombre = %s", (nombre))
    id = cursor.fetchone()
    return id

# conseguir la lista de tipos de artesania
def get_tipo_artesania():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM tipo_artesania")
    artesanias = [artesania[0] for artesania in cursor.fetchall()]
    return artesanias


def get_lista_deportes():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM deporte")
    deportes = [deporte[0] for deporte in cursor.fetchall()]
    return deportes

def get_hincha_by_id_comuna(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT hincha.id, comuna.nombre, comentarios, hincha.nombre, email, celular , modo_transporte FROM hincha, comuna WHERE hincha.comuna_id=comuna.id AND hincha.id = %s", (id))
    hinchas = cursor.fetchone()
    return hinchas

def get_cantidad_tipos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo_artesania_id, COUNT(*) as cantidad FROM artesano_tipo GROUP BY tipo_artesania_id")
    tipos = cursor.fetchall()
    cantidad_tipos = {}

    for tipo_id, cantidad in tipos:
        cursor.execute("SELECT nombre FROM tipo_artesania WHERE id = %s", (tipo_id))
        tipo_id = cursor.fetchone()[0]
        cantidad_tipos[tipo_id] = cantidad

    conn.commit()  # Agregar esta línea para confirmar los cambios
    return cantidad_tipos

def get_cantidad_deportes():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT deporte_id, COUNT(*) as cantidad FROM hincha_deporte GROUP BY deporte_id")
    deportes = cursor.fetchall()
    cantidad_deportes = {}

    for deporte_id, cantidad in deportes:
        cursor.execute("SELECT nombre FROM deporte WHERE id = %s", (deporte_id))
        deporte_id = cursor.fetchone()[0]
        cantidad_deportes[deporte_id] = cantidad

    return cantidad_deportes

