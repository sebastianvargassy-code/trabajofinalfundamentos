from flask import Flask, render_template_string, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'clave'


PRODUCTOS_DATOS = {
    "Galleta soda": {"peso": "6 unidades (222 gr)", "precio": 3.30, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F553905-1000-1000%2F502139.jpg%3Fv%3D637426568401030000&sp=1780454907T3eff30b2fde79422a4a0615ce109a173f43406a9151f5d4ac9df14f724955a02"},
    "Coca Cola": {"peso": "500 ml", "precio": 3.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fblogdapublicidade.com%2Fwp-content%2Fuploads%2F2024%2F04%2Fhistoria-logotipo-coca-cola.jpg&sp=1780454935Tf937e28fdad4546cee89ebf4e9c41414aa88c5ae711f20f6d9148a40f2d0dd4f"},
    "Leche Gloria": {"peso": "390 gr", "precio": 4.20, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse2.mm.bing.net%2Fth%2Fid%2FOIP.hHWhkRCeY2WK1YEcOBHJhwHaHa%3Fpid%3DApi&sp=1780455018T27bb5bb9332bc8ab3a9321556517dab34a68e73fbc03c852c8ad81e2e016694d"},
    "Yogurt Laive": {"peso": "1000 gr", "precio": 6.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F1623914-1000-1000%2F1077446003.jpg%3Fv%3D637571264039100000&sp=1780455051T7847371621c502631d499fc887a77b9181d84fa7eb1932d87829b6363b198043"},
    "Pan en bolsa": {"peso": "500 gr", "precio": 8.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fthf.bing.com%2Fth%2Fid%2FOIP.rNFVwo04_xjcg6bvEs3WXAHaHa%3Fr%3D0%26cb%3Dthfc1falcon%26pid%3DApi&sp=1780455067Tb4146b30c7ccec06ce9c92ef2843e314e23c4d7b6343430dc86b8a1ffab52605"},
    "Galletas de vainilla": {"peso": "6 unidades (222 gr)", "precio": 4.70, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fthf.bing.com%2Fth%2Fid%2FOIP.DjTxAgBSSaqQTjgCFt3xpwHaHa%3Fr%3D0%26cb%3Dthfc1falcon%26pid%3DApi&sp=1780455104Tf00f3fd4a4b63d2e40f4e7000b4f5698aefc13a448b71116add7a7c30cd70fa0"},
    "Atún en lata": {"peso": "140 gr", "precio": 5.80, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F26232485-1000-1000%2F20353584.jpg%3Fv%3D638187847433200000&sp=1780455134Tb105e0beae1208755a662cb6c8ab718720c069034c766e1fc89afb9a9d6ad457"},
    "Café Kirma": {"peso": "180 gr", "precio": 21.90, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse3.mm.bing.net%2Fth%2Fid%2FOIP.OE_lPeo1Y-Wd2d2X9qsTeQHaHa%3Fpid%3DApi&sp=1780455161T529b586b36786350f41d5ab3b567c03fb427178f4f1c71f8ae0f952fea50c577"},
    "Huevos": {"peso": "15 unidades", "precio": 9.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse1.explicit.bing.net%2Fth%2Fid%2FOIP.xACrLpjrzBm9sQTuWlwLWAHaEK%3Fcb%3Dthfvnextfalcon%26pid%3DApi&sp=1780455188T45ea3450cd44a828f84543edff16b18dd67cf7cfceb3c4878c3c276a16175f35"},
    "Chocolate Triangulo": {"peso": "30 gr", "precio": 2.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse3.mm.bing.net%2Fth%2Fid%2FOIP.hmlW7F1pFYt7z5pSBeXqqQAAAA%3Fpid%3DApi&sp=1780455212Tbfc8ff097ddf9107ef5fc20889552195eed7f6d158ff65ddcc422fe9699f2bbf"},
    "Gaseosa KR": {"peso": "1500 ml", "precio": 3.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fthf.bing.com%2Fth%2Fid%2FOIP.Ehem25uon5tvHiQsrfbtNAHaHa%3Fcb%3Dthfc1falcon%26pid%3DApi&sp=1780455230T5fbdef4eb2605aca6da67ac5795e519fdbd3fd5d41da900ae91b53feda0c975f"},
    "Gaseosa sprite": {"peso": "1500 ml", "precio": 6.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fjumboargentina.vtexassets.com%2Farquivos%2Fids%2F770528%2FGaseosa-Sprite-Sin-Az-car-Lima-lim-n-1-Gaseosa-Sprite-Sin-Az-car-Lima-lim-n-1-5-Lt-2-28515.jpg%3Fv%3D638128497938730000&sp=1780455249T37eb788f96eb443c8ba8543f109fc4a6108fe8030f51079b119040acf9e15e50"},
    "Galletas oreo": {"peso": "432 gr", "precio": 8.20, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse2.mm.bing.net%2Fth%2Fid%2FOIP.fKP_gzZeq9WWd93HkxBQtwHaHa%3Fr%3D0%26pid%3DApi&sp=1780455305T117f657b2eacd43921abf739eaf57ee8a270a1d1a5cf75cbd0379f88ee71bfa5"},
    "Mayonesa": {"peso": "190 gr", "precio": 5.80, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.B3vEJivvcNKfZsZwJHox7wHaHa%3Fpid%3DApi&sp=1780455324T61ad9daf558bb50b464233d6a1421f54dc20ae07a9499cb8deae7de3ad24d234"},
    "Mermelada": {"peso": "320 gr", "precio": 5.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.y27X3ox-I3ANcsqxcHsyfAHaHa%3Fr%3D0%26pid%3DApi&sp=1780455349T319f6a6d3130243205ff7bfb2ee6c35dac6ae3e7410a77d805f5f0f4e39fe790"},
    "Jamón San Fernando": {"peso": "200 gr", "precio": 9.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F400599-1000-1000%2F20200730.jpg%3Fv%3D637345287095800000&sp=1780455385T7f7cc64cdfbbb43fd124057e08a7a04e3d5bdac5b2239b57eb91148cd22428af"},
    "Margarina Manti": {"peso": "225 gr", "precio": 3.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.5UBhg4_Ki_7RGe1H_a0m1QHaHa%3Fpid%3DApi&sp=1780455412T993bccac040e6d47a0911546ce0d4e1323ca8d00fa53db05201999fc8aa3a68b"},
    "Mantequilla Laive": {"peso": "200 gr", "precio": 7.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F816669-1000-1000%2F25423.jpg%3Fv%3D637490906440700000&sp=1780455486Tb16174d349db5067f5b4e4e1f05c25381c212b1f3cede7cbfe58e8d94310018a"},
    "Café Ecco": {"peso": "80 gr", "precio": 8.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fthfvnext.bing.com%2Fth%2Fid%2FOIP.s_-XZ8RrVmfAKJmEB3RulgHaHa%3Fcb%3Dthfvnextfalcon%26pid%3DApi&sp=1780455546T83f25d5bb59f1d27634270f7cae5016256b0de7a041767ff083f214524fc23c1"},
    "Café Altomayo": {"peso": "170 gr", "precio": 25.10, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.IoiQlLZsMupf2PRDC1sxTQHaHa%3Fpid%3DApi&sp=1780455633T0bbf208e2f86fd77ad5114e1226cdebe039e5013e8f391949248ef098bb9aece"},
    "Leche Fresca Gloria": {"peso": "946 ml", "precio": 5.80, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F498636-1000-1000%2F20198432.jpg%3Fv%3D637405574876270000&sp=1780455651Ta806cf880fb7355e704c160e5a4305e8dbf37ecf572b6d1a0f4b28dc5395eb18"},
    "Leche sin lactosa Laive": {"peso": "1000 ml", "precio": 5.20, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.0hyEkivyIk9ClO5ewpsrhQHaJT%3Fpid%3DApi&sp=1780455673T0a2ca719d39b88cc0555cade5ee339258525314f504ab19dddca3cb6da1d888e"},
    "Duraznos en almibar": {"peso": "820 gr", "precio": 9.70, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.7Vg7YlqlS1wQuGhOQ1GhcgHaHa%3Fpid%3DApi&sp=1780455704Td34e3b419a380f2b7bdc3553fbd1c640fe84166b33275ba0ba3286d1ce6f3bda"},
    "Gaseosa Guarana": {"peso": "450 ml", "precio": 2.00, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fplazavea.vteximg.com.br%2Farquivos%2Fids%2F6760540-1000-1000%2F20171726.jpg%3Fv%3D637805496954900000&sp=1780455727Tb0169b10f2d5b43f1e3155629843fa6be46b2a7005abc92cb8920bf1bb54afa6"},
    "Pan Chabata": {"peso": "6 unidades", "precio": 1.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse4.explicit.bing.net%2Fth%2Fid%2FOIP.uhE2DDjLw3J1dSsThP7FtQHaHa%3Fcb%3Dthfc1falcon%26pid%3DApi&sp=1780455749Tddfac23f281cea25b0484eea2e14152a6d7cf2ae0ad60ba03a0f819dcf45c78a"},
    "Pan caracol": {"peso": "6 unidades", "precio": 1.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fcdn0.recetasgratis.net%2Fes%2Fposts%2F8%2F2%2F7%2Fpan_caracol_77728_orig.jpg&sp=1780455771Td2da34977897651f74dbb95578b18bef17a9ee7ebaa6a3925d0ebd55f33f4b1c"},
    "Pan Francés": {"peso": "6 unidades", "precio": 1.50, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.D_sm6Qiv9YJEcXnzcZHz8QHaEK%3Fpid%3DApi&sp=1780455797Tc813df28cb105472ad9e72a38cb96b06465aca504e9b3e539c6905e4a713cddd"},
    "Gaseosa Concordia": {"peso": "1500 ml", "precio": 4.00, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.tddNk4rvShjj3FZO-4iN3wHaHa%3Fpid%3DApi&sp=1780455825Tda67233eb7ec7e82f74707bbf33ff251ed863544eda477df6b734e00d3b2bd93"},
    "Avena": {"peso": "900 gr", "precio": 9.30, "img": "https://www.startpage.com/av/proxy-image?piurl=https%3A%2F%2Fthf.bing.com%2Fth%2Fid%2FOIP.9O6oKzGepxnCSVnF8vB7ywHaE8%3Fcb%3Dthfc1falcon%26pid%3DApi&sp=1780455859Ta5bbcf62607ec6351c4f1c036e051b2ac77c9227edf9c9418ce4781d800b4126"}

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
