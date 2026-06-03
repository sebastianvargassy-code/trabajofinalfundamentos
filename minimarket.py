from flask import Flask, render_template_string, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'clave'


PRODUCTOS_DATOS = {
    "Galleta soda": {"peso": "6 unidades (222 gr)", "precio": 3.30, "img": "https://plazavea.vteximg.com.br/arquivos/ids/25835356-1000-1000/502139.jpg"},
    "Coca Cola": {"peso": "500 ml", "precio": 3.50, "img": "https://yopo.pe/wp-content/uploads/2023/12/COCA-500-ORIGINAL-RAPPI.jpg"},
    "Leche Gloria": {"peso": "390 gr", "precio": 4.20, "img": "https://www.gloria.com.pe/images/lataa.png"},
    "Yogurt Laive": {"peso": "1000 gr", "precio": 6.50, "img": "https://wongfood.vtexassets.com/arquivos/ids/809652-1200-auto?v=639023674094630000&width=1200&height=auto&aspect=true"},
    "Pan en bolsa": {"peso": "500 gr", "precio": 8.50, "img": "https://media.istockphoto.com/id/518733512/es/foto/pan-en-bolsa-de-pl%C3%A1stico.jpg?s=612x612&w=0&k=20&c=UPaAZgdhKw7Rq-1KMJtAHLEl4ioz8Q6DVMm0AY1gRcs="},
    "Galletas de vainilla": {"peso": "6 unidades (222 gr)", "precio": 4.70, "img": "https://vegaperu.vtexassets.com/arquivos/ids/157311/7622300279776.jpg?v=637618918678400000"},
    

}
index_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimarket Nelly</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background-color: #f7f5f0; color: #333; display: flex; flex-direction: column; min-height: 100vh; }
        header { background-color: #5a3907; padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.3); }
        header h1 { color: #d4c196; font-size: 24px; font-weight: bold; }
        nav ul { display: flex; gap: 20px; list-style: none; }
        nav a { color: #f7f5f0; text-decoration: none; font-weight: 500; transition: color 0.3s; }
        nav a:hover, nav li:first-child a { color: #d4c196; }
        .intro { background: linear-gradient(135deg, #5a3907, #362204); color: white; padding: 60px 5%; display: flex; align-items: center; justify-content: space-between; gap: 40px; }
        .intro-text { flex: 1; max-width: 600px; }
        .intro-text h2 { font-size: 36px; color: #d4c196; margin-bottom: 15px; }
        .intro-text p { font-size: 18px; line-height: 1.6; color: #e2dcd0; margin-bottom: 25px; }
        .btn-ver-productos { display: inline-block; background-color: #d4c196; color: #362204; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: bold; transition: background-color 0.2s; }
        .btn-ver-productos:hover { background-color: #e5d4b1; }
        .intro-img-container { flex: 1; display: flex; justify-content: center; }
        .intro img { max-width: 100%; height: auto; border-radius: 15px; box-shadow: 0 8px 24px rgba(0,0,0,0.2); max-height: 300px; object-fit: cover; }
        .features { padding: 50px 5%; text-align: center; }
        .features h3 { font-size: 28px; color: #5a3907; margin-bottom: 30px; }
        .contenedor-tarjetas { display: flex; gap: 25px; flex-wrap: wrap; justify-content: center; }
        .tarjeta { background: white; padding: 30px 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); width: 280px; border-top: 4px solid #5a3907; }
        .tarjeta h4 { color: #5a3907; margin-bottom: 10px; }
        .tarjeta p { color: #666; font-size: 14px; }
        footer { background-color: #362204; color: #a89c84; text-align: center; padding: 20px 0; margin-top: auto; font-size: 14px; }
        @media screen and (max-width: 768px) { header { flex-direction: column; gap: 15px; } .intro { flex-direction: column; text-align: center; } }
    </style>
</head>
<body>
    <header>
        <h1>Minimarket Nelly</h1>
        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/productos">Productos</a></li>
                <li><a href="/contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="intro">
            <div class="intro-text">
                <h2>Siempre a tu disposición</h2>
                <p>Acercamos productos de calidad para su consumo en el hogar, de calidad, frescos y a precios competitivos.</p>
                <a href="/productos" class="btn-ver-productos">Ver Productos</a>
            </div>
            <div class="intro-img-container">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmrN-Sgy3YWNqUsjVziPRu9zKMV46mrh57sQ&s" alt="Interior">
            </div>
        </section>
    </main>
    <footer><p>&copy; 2026 Minimarket Nelly. Todos los derechos reservados.</p></footer>
</body>
</html>
"""

productos_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimarket Nelly - Productos</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background-color: #f7f5f0; color: #333; display: flex; flex-direction: column; min-height: 100vh; }
        
        header { text-align: center; background-color: rgb(160, 113, 95); padding: 25px 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        header h1 { font-size: 28px; color: #fff; }
        header .nav-link { color: #f7f5f0; text-decoration: none; margin-top: 5px; display: inline-block; font-size: 14px; }

        /* Contenedor Split de Dos Columnas */
        .contenedor-main { max-width: 1300px; width: 95%; margin: 30px auto; display: flex; gap: 25px; align-items: flex-start; }
        
        /* Columna Izquierda: Catálogo */
        .malla-productos { flex: 3; display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 15px; }
        .tarjeta-producto { background-color: white; border: 1px solid #9b8360; border-radius: 8px; display: flex; flex-direction: column; padding: 12px; transition: transform 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
        .tarjeta-producto:hover { transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.08); }
        .imagen-producto { width: 100%; height: 120px; object-fit: contain; background: #fafafa; border-radius: 6px; margin-bottom: 10px; }
        .info-producto { display: flex; flex-direction: column; gap: 4px; flex-grow: 1; }
        .info-producto h3 { font-size: 14px; color: #222; }
        .info-producto p { font-size: 12px; color: #6a5a50; margin-bottom: 10px; }
        .compra-producto { display: flex; justify-content: space-between; align-items: center; margin-top: auto; }
        .precio { font-size: 15px; font-weight: bold; color: #222; }
        .boton-compra { background-color: #b6926f; color: white; padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 4px; text-decoration: none; transition: background-color 0.2s; }
        .boton-compra:hover { background-color: #6d4b2a; }

        /* Columna Derecha: Carrito Estático Lateral Fijo */
        .carrito-estatico { width: 340px; background-color: white; border: 1px solid #e2f3f0; border-radius: 12px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); position: sticky; top: 20px; }
        .carrito-estatico h2 { font-size: 18px; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid lightsalmon; color: #5a3907; }
        .lista-carrito { max-height: 350px; overflow-y: auto; margin-bottom: 15px; }
        .item-carrito { display: flex; justify-content: space-between; align-items: center; font-size: 13px; padding: 10px 0; border-bottom: 1px solid #f0f0f0; }
        .item-info p { color: #6a5a50; font-size: 11px; }
        .item-derecha { display: flex; align-items: center; gap: 10px; }
        .btn-quitar { color: #ccc; text-decoration: none; font-size: 16px; font-weight: bold; transition: color 0.2s; padding: 0 4px; }
        .btn-quitar:hover { color: #d9534f; }
        
        .total-carrito { display: flex; justify-content: space-between; font-size: 16px; font-weight: bold; padding-top: 10px; border-top: 1px solid #eee; }
        .btn-vaciar { display: block; text-align: center; background-color: #d9534f; color: white; text-decoration: none; padding: 10px; border-radius: 6px; font-size: 13px; margin-top: 15px; font-weight: bold; }
        .btn-vaciar:hover { background-color: #c9302c; }
        .carrito-vacio { text-align: center; color: #999; font-size: 13px; padding: 20px 0; }

        footer { text-align: center; font-size: 12px; background-color: #5a4a40; color: white; padding: 15px 0; margin-top: auto; }

        /* Ajuste Responsivo */
        @media (max-width: 900px) {
            .contenedor-main { flex-direction: column; }
            .carrito-estatico { width: 100%; position: relative; top: 0; }
        }
    </style>
</head>
<body>

    <header>
        <h1>Nuestros Productos</h1>
        <a class="nav-link" href="/">← Volver al Inicio</a>
    </header>

    <main class="contenedor-main">
        <div class="malla-productos">
            {% for nombre, data in productos.items() %}
            <article class="tarjeta-producto">
                <img class="imagen-producto" src="{{ data.img }}" alt="{{ nombre }}">
                <div class="info-producto">
                    <h3>{{ nombre }}</h3>
                    <p>{{ data.peso }}</p>
                </div>
                <div class="compra-producto">
                    <span class="precio">S/.{{ "%.2f"|format(data.precio) }}</span>
                    <a href="/agregar/{{ nombre }}" class="boton-compra">Añadir</a>
                </div>
            </article>
            {% endfor %}
        </div>

        <aside class="carrito-estatico">
            <h2>Tu Carrito</h2>
            <div class="lista-carrito">
                {% if session.get('carrito') %}
                    {% for item_id, item in session['carrito'].items() %}
                    <div class="item-carrito">
                        <div class="item-info">
                            <strong>{{ item.nombre }}</strong>
                            <p>Cant: {{ item.cantidad }} (S/.{{ "%.2f"|format(item.precio) }} c/u)</p>
                        </div>
                        <div class="item-derecha">
                            <span>S/.{{ "%.2f"|format(item.precio * item.cantidad) }}</span>
                            <a href="/quitar/{{ item_id }}" class="btn-quitar" title="Eliminar producto">✕</a>
                        </div>
                    </div>
                    {% endfor %}
                {% else %}
                    <div class="carrito-vacio">El carrito está vacío.</div>
                {% endif %}
            </div>
            
            {% if session.get('carrito') %}
            <div class="total-carrito">
                <span>Total:</span>
                <span>S/.{{ "%.2f"|format(total) }}</span>
            </div>
            <a href="/vaciar" class="btn-vaciar">Vaciar Carrito</a>
            {% endif %}
        </aside>
    </main>

    <footer>
        <p>&copy; Todos los derechos reservados 2026</p>
    </footer>
</body>
</html>
"""
contacto_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimarket Nelly - Contacto</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background-color: #f7f5f0; color: #333; display: flex; flex-direction: column; min-height: 100vh; }
        header { background-color: #5a3907; padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.3); }
        header h1 { color: #d4c196; font-size: 24px; font-weight: bold; }
        nav ul { display: flex; gap: 20px; list-style: none; }
        nav a { color: #f7f5f0; text-decoration: none; font-weight: 500; transition: color 0.3s; }
        nav a:hover, nav li:nth-child(3) a { color: #d4c196; }

        .contenedor-contacto { max-width: 600px; width: 90%; margin: 60px auto; background-color: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); padding: 40px; border-top: 5px solid #5a3907; text-align: center; }
        .contenedor-contacto h2 { color: #5a3907; font-size: 28px; margin-bottom: 20px; }
        
        .info-seccion { margin-top: 30px; }
        .info-item { margin-bottom: 25px; }
        .info-item h4 { color: #5a3907; font-size: 16px; margin-bottom: 8px; text-transform: uppercase; }
        .info-item p { color: #555; font-size: 15px; line-height: 1.6; }

        footer { background-color: #362204; color: #a89c84; text-align: center; padding: 20px 0; margin-top: auto; font-size: 14px; }
    </style>
</head>
<body>
    <header>
        <h1>Minimarket Nelly</h1>
        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/productos">Productos</a></li>
                <li><a href="/contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <main style="display: flex; flex-direction: column; flex-grow: 1;">
        <section class="contenedor-contacto">
            <h2>Información de Contacto</h2>
            <div class="info-seccion">
                <div class="info-item">
                    <h4>Nuestra Ubicación</h4>
                    <p>c.8 Bayovar, Sjl,Lima, Perú</p>
                </div>
                <div class="info-item">
                    <h4> Horario de Atención</h4>
                    <p>Lunes a Sábado: 7:00 AM - 10:00 PM<br>Domingos: 8:00 AM - 2:00 PM</p>
                </div>
                <div class="info-item">
                    <h4> Teléfono</h4>
                    <p>+51 935206954</p>
                </div>
            </div>
        </section>
    </main>

    <footer><p>&copy; 2026 Minimarket Nelly. Todos los derechos reservados.</p></footer>
</body>
</html>
"""
@app.route('/')
def index():
    return render_template_string(index_html)

@app.route('/productos')
def productos():
    carrito = session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render_template_string(productos_html, productos=PRODUCTOS_DATOS, total=total)

@app.route('/agregar/<nombre>')
def agregar(nombre):
    if nombre in PRODUCTOS_DATOS:
        carrito = session.get('carrito', {})
        
     
        encontrado = False
        for item_id, item in carrito.items():
            if item['nombre'] == nombre:
                item['cantidad'] += 1
                encontrado = True
                break
                
        if not encontrado:
            nuevo_id = str(uuid.uuid4())
            carrito[nuevo_id] = {
                'nombre': nombre,
                'precio': PRODUCTOS_DATOS[nombre]['precio'],
                'cantidad': 1
            }
            
        session['carrito'] = carrito
        session.modified = True
    return redirect(url_for('productos'))
@app.route('/contacto')
def contacto():
    return render_template_string(contacto_html)
@app.route('/quitar/<item_id>')
def quitar(item_id):
    carrito = session.get('carrito', {})
    if item_id in carrito:
        carrito.pop(item_id)
        session['carrito'] = carrito
        session.modified = True
    return redirect(url_for('productos'))

@app.route('/vaciar')
def vaciar():
    session.pop('carrito', None)
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(debug=True)
