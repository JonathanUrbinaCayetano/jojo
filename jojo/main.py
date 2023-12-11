from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return "Aprendiendo Flask"

@app.route('/mostrar-contacto')
def mostrar_contacto ():
    return "<h1>jonathanSSSSS</h1>"
@app.route('/lenguajes-de-programacion')
def lenguajes():
    return """
<h1>lenguajes de programacion</h1>
<li>python</>
<li>java</>
<li>visulS</>
</ul>
"""
@app.route('/recibir-nombre/<nombre>')
def recibir_nombre(nombre):
    return f"""
<h1>pagina de informacion</h1>
<h3>bienvenido {nombre}</h3>
"""

@app.route("/mostrar-calificaciones/<nombre>/<promedio>")
def mostrar_calificaciones(nombre, promedio):
    return f"""
<h1>pagina de informacion </h1>
<p>datos del alumno</p>
<h3>bienvenido {nombre}</h3>
<h4>tu promedio es {promedio}</h4>
"""
@app.route("/mostrar-precio-producto/<string:producto>/<float:precio>")
def mostrar_precio_producto( producto,precio):
    return f"""
<h1>pagina de informacion </h1>
<p>datos del producto{producto}</p>
<p>precio $ {precio:,.2f}</p>
"""

@app.route("/mostrar-tipo-vehiculo>")
@app.route("/mostrar-tipo-vehiculo/<tipo>")
def moatrar_tipo_vehiculo(tipo=None):
    texto=""
    if tipo !=None:
        texto=f"tipo de vehiculo {tipo}"
        
        return f"""
    <h1>datos del vehiculo </h1>
    {texto}
    """
    @app.route('/mostrar-contacto')
    def mostrar_contacto ():
        return redirect(url_for("contacto"))
    
    
    

    
        
    




if __name__== '__main__':
    app.run()

