from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# INDEX REDISEÑADO (Solo modifiqué este bloque)
index_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimarket Nelly</title>
    <style>
        /* Reseteo y Fuentes */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f7f5f0;
            color: #333333;
            display: flex;
            flex-direction: column;
            min-height: 100vi;
        }

        /* Header y Navegación */
        header {
            background-color: #5a3907;
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        header h1 {
            color: #d4c196;
            font-size: 24px;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            gap: 20px;
            list-style: none;
        }

        nav a {
            color: #f7f5f0;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        nav a:hover, nav li:first-child a {
            color: #d4c196;
        }

        /* Sección intro (Bienvenida) */
        .intro {
            
            color: white;
            padding: 60px 5%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 40px;
        }

        .intro-text {
            flex: 1;
            max-width: 600px;
        }

        .intro-text h2 {
            font-size: 36px;
            color: #d4c196;
            margin-bottom: 15px;
            line-height: 1.2;
        }

        .intro-text p {
            font-size: 18px;
            line-height: 1.6;
            color: #e2dcd0;
            margin-bottom: 25px;
        }

        .btn-ver-productos {
            display: inline-block;
            background-color: #d4c196;
            color: #362204;
            padding: 12px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.2s, background-color 0.2s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .btn-ver-productos:hover {
            background-color: #e5d4b1;
            transform: translateY(-2px);
        }

        .intro-img-container {
            flex: 1;
            display: flex;
            justify-content: center;
        }

        .intro img {
            max-width: 100%;
            height: auto;
            border-radius: 15px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            object-fit: cover;
            max-height: 300px;
        }

        /* Características / Tarjetas de Información */
        .features {
            padding: 50px 5%;
            text-align: center;
        }

        .features h3 {
            font-size: 28px;
            color: #5a3907;
            margin-bottom: 30px;
        }

        .contenedor-tarjetas {
            display: flex;
            gap: 25px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .tarjeta {
            background: white;
            padding: 30px 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            width: 280px;
            transition: transform 0.3s;
            text-align: center;
            border-top: 4px solid #5a3907;
        }

        .tarjeta:hover {
            transform: translateY(-5px);
        }

        .tarjeta-icono {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .tarjeta h4 {
            color: #5a3907;
            margin-bottom: 10px;
            font-size: 18px;
        }

        .tarjeta p {
            color: #666;
            font-size: 14px;
            line-height: 1.5;
        }

        /* Footer */
        footer {
            background-color: #362204;
            color: #a89c84;
            text-align: center;
            padding: 20px 0;
            margin-top: auto;
            font-size: 14px;
        }

        /* Responsivo */
        @media screen and (max-width: 768px) {
            header {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }

            .intro {
                flex-direction: column;
                text-align: center;
                padding: 40px 5%;
            }

            .intro-text h2 {
                font-size: 28px;
            }

            .intro-text p {
                font-size: 16px;
            }

            .intro-img-container {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Minimarket Nelly</h1>
        <nav>
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="/productos">Productos</a></li>
                <li><a href="#">Contacto</a></li>
                <li><a href="#">Carrito</a></li>
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
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmrN-Sgy3YWNqUsjVziPRu9zKMV46mrh57sQ&s" alt="Interior de Minimarket Nelly">
            </div>
        </section>

        <section class="features">
            <h3>¿Por qué elegirnos?</h3>
            <div class="contenedor-tarjetas">
                <div class="tarjeta">
                   
                    <h4>Variedad en los productos</h4>
                    <p>Abarrotes, snack y alimentos del día a día</p>
                </div>
                <div class="tarjeta">
                 
                    <h4>Productos frescos</h4>
                    <p>Renovación constante del stock.</p>
                </div>
                <div class="tarjeta">
                 
                    <h4>Buena atención</h4>
                    <p>Basada en el respeto.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Minimarket Nelly. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

# PRODUCTOS (Exactamente igual, sin ningún cambio)
productos_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artesanías de Chulucanas</title>
    <style>
    header{

    text-align: center;
    border-bottom: 1px solid;
    background-color: lightsalmon;
}
header h1{
 font-size: 43pt;

}
body{

    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: beige;

}
.contenedor
{max-width: 90%;
    padding: 0 20px;
margin:40px auto;}
/*grilla malla de 3 columnas*/
.malla-productos{

    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 30px;
}

.imagen-producto{
    width: 200px;
    height: 150px;
    
}
.tarjeta-producto
{
    background-color: white;
    border: 1px solid #aeeade;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
   padding: 5px;
   align-items: center;
}
.info-producto
{
    display: flex;
    flex-direction:column;

}
.info-producto h3{
    font-size: 14pt;
}
.info-producto p{
    font-size: 10pt;
    color:#5a4a40;
    flex-grow: 1;

}
.compra-producto{

    display:"flex";
    justify-content: space-between;
    align-items: center;
}
.precio{
    font-size: 15pt;
    font-weight: bold;
    color: black;
}
.boton-compra{
    background-color: #8c6239;
    color:white;
    padding: 8px 20px;
    font-size:9pt;
    border-radius:4px;
}
.boton-compra:hover{
    background-color:#6d4b2a
}
footer{




    text-align: center;
    font-size: 9pt;
    background-color: #5a4a40;
    color: white;
    padding: 10px 0px;    
}
    </style>

</head>
<body>




    <header>
        <h1>Productos</h1>
        <p>Buscar</p>
    </header>


    <main class="contenedor">
        <section class="malla-productos">


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i1.webp" alt="i1">
                <div class="info-producto">
                    <h3>Galleta soda</h3>
                    <p>6 unidades (222 gr)</p>
                </div>
                <span class="precio">S/.3.30</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i2.png" alt="i2">
                <div class="info-producto">
                    <h3>Coca Cola</h3>
                    <p>500 ml</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i3.jpg" alt="i3">
                <div class="info-producto">
                    <h3>Leche Gloria</h3>
                    <p>390 gr</p>
                </div>
                <span class="precio">S/.4.20</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i4.webp" alt="i4">
                <div class="info-producto">
                    <h3>Yogurt Laive</h3>
                    <p>1000 gr</p>
                </div>
                <span class="precio">S/.6.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i5.png" alt="i5">
                <div class="info-producto">
                    <h3>Pan en bolsa</h3>
                    <p>500 gr</p>
                </div>
                <span class="precio">S/.8.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i6.jpg" alt="i6">
                <div class="info-producto">
                    <h3>Galletas de vainilla</h3>
                    <p>6 unidades (222 gr)</p>
                </div>
                <span class="precio">S/.4.70</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i7.webp" alt="i7">
                <div class="info-producto">
                    <h3>Atún en lata</h3>
                    <p>140 gr</p>
                </div>
                <span class="precio">S/.5.80</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i8.png" alt="i8">
                <div class="info-producto">
                    <h3>Café Kirma</h3>
                    <p>180 gr</p>
                </div>
                <span class="precio">S/.21.90</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i9.jpg" alt="i9">
                <div class="info-producto">
                    <h3>Huevos</h3>
                    <p>15 unidades</p>
                </div>
                <span class="precio">S/.9.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i10.webp" alt="i10">
                <div class="info-producto">
                    <h3>Chocolate Triangulo</h3>
                    <p>30 gr</p>
                </div>
                <span class="precio">S/.2.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i11.png" alt="i11">
                <div class="info-producto">
                    <h3>Gaseosa KR</h3>
                    <p>1500 ml</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i12.jpg" alt="i12">
                <div class="info-producto">
                    <h3>Gaseosa sprite</h3>
                    <p>1500 ml</p>
                </div>
                <span class="precio">S/.6.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i13.webp" alt="i13">
                <div class="info-producto">
                    <h3>Galletas oreo</h3>
                    <p>432 gr</p>
                </div>
                <span class="precio">S/.8.20</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i14.png" alt="i14">
                <div class="info-producto">
                    <h3>Mayonesa</h3>
                    <p>190 gr</p>
                </div>
                <span class="precio">S/.5.80</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i15.jpg" alt="i15">
                <div class="info-producto">
                    <h3>Mermelada</h3>
                    <p>320 gr</p>
                </div>
                <span class="precio">S/.5.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i16.webp" alt="i16">
                <div class="info-producto">
                    <h3>Jamón San Fernando</h3>
                    <p>200 gr</p>
                </div>
                <span class="precio">S/.9.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i17.png" alt="i17">
                <div class="info-producto">
                    <h3>Margarina Manti</h3>
                    <p>225 gr</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>
 
            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i18.jpg" alt="i18">
                <div class="info-producto">
                    <h3>Mantequilla Laive</h3>
                    <p>200 gr</p>
                </div>
                <span class="precio">S/.7.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i19.webp" alt="i19">
                <div class="info-producto">
                    <h3>Café Ecco</h3>
                    <p>80 gr</p>
                </div>
                <span class="precio">S/.8.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i20.png" alt="i20">
                <div class="info-producto">
                    <h3>Café Altomayo</h3>
                    <p>170 gr</p>
                </div>
                <span class="precio">S/.25.10</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i21.png" alt="i21">
                <div class="info-producto">
                    <h3>Leche Fresca Gloria</h3>
                    <p>946 ml</p>
                </div>
                <span class="precio">S/.5.80</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i22.png" alt="i22">
                <div class="info-producto">
                    <h3>Leche sin lactosa Laive</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.5.20</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i23.png" alt="i23">
                <div class="info-producto">
                    <h3>Duraznos en almibar</h3>
                    <p>820 gr</p>
                </div>
                <span class="precio">S/.9.70</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i24.png" alt="i24">
                <div class="info-producto">
                    <h3>Gaseosa Guarana</h3>
                    <p>450 ml</p>
                </div>
                <span class="precio">S/.2.00</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i25.png" alt="i25">
                <div class="info-producto">
                    <h3>Pan Chabata</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i26.png" alt="i26">
                <div class="info-producto">
                    <h3>Pan caracol</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i27.png" alt="i27">
                <div class="info-producto">
                    <h3>Pan Francés</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.2.40</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i28.png" alt="i28">
                <div class="info-producto">
                    <h3>Gaseosa Concordia</h3>
                    <p>1500 ml</p>
                </div>
                <span class="precio">S/.4.00</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i29.png" alt="i29">
                <div class="info-producto">
                    <h3>Cifrut</h3>
                    <p>500 ml</p>
                </div>
                <span class="precio">S/.2.00</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i30.png" alt="i30">
                <div class="info-producto">
                    <h3>Pulp</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.4.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i31.png" alt="i31">
                <div class="info-producto">
                    <h3>Yopimix</h3>
                    <p>125 gr</p>
                </div>
                <span class="precio">S/.2.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i32.png" alt="i32">
                <div class="info-producto">
                    <h3>Helado de vainilla</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.14.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i33.png" alt="i33">
                <div class="info-producto">
                    <h3>Helado de fresa</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.14.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i34.png" alt="i34">
                <div class="info-producto">
                    <h3>Queso Chedar</h3>
                    <p>170 gr</p>
                </div>
                <span class="precio">S/.8.40</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i35.png" alt="i35">
                <div class="info-producto">
                    <h3>Chocolate Vizio</h3>
                    <p>63 gr</p>
                </div>
                <span class="precio">S/.4.20</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i36.png" alt="i36">
                <div class="info-producto">
                    <h3>Galleta rellenitas</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i37.png" alt="i37">
                <div class="info-producto">
                    <h3>Cereales Angel Chocolate</h3>
                    <p>250 gr</p>
                </div>
                <span class="precio">S/.6.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i38.png" alt="i38">
                <div class="info-producto">
                    <h3>Cereales Angel Maiz</h3>
                    <p>1000 gr</p>
                </div>
                <span class="precio">S/.14.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i39.png" alt="i39">
                <div class="info-producto">
                    <h3>Avena</h3>
                    <p>900 gr</p>
                </div>
                <span class="precio">S/.9.30</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i40.png" alt="i40">
                <div class="info-producto">
                    <h3>Chicle trident</h3>
                    <p>5 unidades</p>
                </div>
                <span class="precio">S/.1.50</span>
                <a href="#" class="boton-compra">Añadir</a>
            </article>


        </section>
    </main>


    <footer>
        <p>&copy; Todos los derechos reservados 2026</p>
    </footer>


</body>
</html>
"""

@app.route('/')
def inicio():
    return render_template_string(index_html)

@app.route('/productos')
def productos():
    return render_template_string(productos_html)

if __name__ == '__main__':
    app.run(debug=True)
