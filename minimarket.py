from flask import Flask, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave'

index_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimarket Nelly</title>
    <style>
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
            min-height: 100vh;
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
            background: linear-gradient(135deg, #5a3907, #362204);
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

productos_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimarket Nelly - Productos</title>
   <style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
/* Botón flotante para mostrar/ocultar el carrito */
.btn-toggle-carrito {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
    background-color: #b6926f;
    color: white;
    border: none;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    font-size: 20px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    transition: background-color 0.2s;
}
.btn-toggle-carrito:hover {
    background-color: #6d4b2a;
}

.carrito-flotante.oculto {
    display: none;
}

@media (max-width: 768px) {
    .carrito-flotante {
        position: fixed;
        top: 0;
        right: 0;
        width: 85%;
        height: 100vh;
        z-index: 999;
        overflow-y: auto;
        border-radius: 0;
        box-shadow: -4px 0 20px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }
    .carrito-flotante.oculto {
        display: block;
        transform: translateX(100%);
    }
}
.contenedor {
    max-width: 1200px;
    width: 95%;
    margin: 30px auto;
    display: flex; 
    gap: 30px;
}

.malla-productos {
    flex: 3;
    display: grid;
    grid-template-columns: repeat(4, minmax(150px, 1fr));
    gap: 15px;
}

.carrito-flotante {
    flex: 1;
    background-color: white;
    border: 1px solid #e2f3f0;
    border-radius: 12px;
    padding: 20px;
    height: fit-content;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    position: sticky;
    top: 20px;
}

.carrito-flotante h2 {
    font-size: 18px;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid lightsalmon;
}

.item-carrito {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    padding: 10px 0;
    border-bottom: 1px solid #f0f0f0;
}

.item-carrito p {
    color: #6a5a50;
    font-size: 12px;
}

.total-carrito {
    margin-top: 15px;
    display: flex;
    justify-content: space-between;
    font-size: 16px;
}

.btn-vaciar {
    display: block;
    text-align: center;
    background-color: #d9534f;
    color: white;
    text-decoration: none;
    padding: 8px;
    border-radius: 6px;
    font-size: 12px;
    margin-top: 15px;
    font-weight: bold;
}
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f7f5f0; 
    color: #333;
}

header {
    text-align: center;
    background-color: rgb(160, 113, 95);
    padding: 30px 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

header h1 {
    font-size: 32px; 
    color: #fff;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
}

.contenedor {
    max-width: 1200px;
    width: 95%; 
    margin: 30px auto;
}

.malla-productos {
    display: grid;
    grid-template-columns: repeat(5, minmax(150px, 1fr)); 
    gap: 15px; 
}

.tarjeta-producto {
    background-color: white;
    border: 1px solid #9b8360;
    border-radius: 8px; 
    display: flex;
    flex-direction: column;
    padding: 10px; 
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.tarjeta-producto:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
}

.imagen-producto {
    width: 100%;
    height: 120px;
    object-fit: cover; 
    border-radius: 6px;
    margin-bottom: 10px;
}

.info-producto {
    display: flex;
    flex-direction: column;
    gap: 4px;
    flex-grow: 1; 
}

.info-producto h3 {
    font-size: 15px; 
    color: #222;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.info-producto p {
    font-size: 12px; 
    color: #6a5a50;
    line-height: 1.3;
    margin-bottom: 10px;
}

.compra-producto {
    display: flex; 
    justify-content: space-between;
    align-items: center;
    margin-top: auto; 
    width: 100%;
}

.precio {
    font-size: 16px;
    font-weight: bold;
    color: #222;
}

.boton-compra {
    background-color: #b6926f;
    color: white;
    padding: 6px 12px;
    font-size: 11px; 
    font-weight: 600;
    border-radius: 4px;
    border: none;
    cursor: pointer;
    transition: background-color 0.2s;
}

.boton-compra:hover {
    background-color: #6d4b2a;
}

footer {
    text-align: center;
    font-size: 12px;
    background-color: #5a4a40;
    color: white;
    padding: 15px 0;
    margin-top: 40px;
}


@media (max-width: 1024px) {
    .malla-productos {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 600px) {
    .malla-productos {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
    
    .imagen-producto {
        height: 100px; 
    }
}
</style>
</head>
<body>

    <header>
        <h1>Productos</h1>
        <p>Buscar</p>
    </header>

    <main class="contenedor">
         <h4>Comestibles</h4><br>
        <section class="malla-productos">
           
            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i1.jpg" alt="i1">
                <div class="info-producto">
                    <h3>Galleta soda</h3>
                    <p>6 unidades (222 gr)</p>
                </div>
                <span class="precio">S/.3.30</span>
                <a href="/agregar/Galleta soda/3.30" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i2.jpg" alt="i2">
                <div class="info-producto">
                    <h3>Coca Cola</h3>
                    <p>500 ml</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="/agregar/Coca Cola/3.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i3.jpg" alt="i3">
                <div class="info-producto">
                    <h3>Leche Gloria</h3>
                    <p>390 gr</p>
                </div>
                <span class="precio">S/.4.20</span>
                <a href="/agregar/Leche Gloria/4.20" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i4.jpg" alt="i4">
                <div class="info-producto">
                    <h3>Yogurt Laive</h3>
                    <p>1000 gr</p>
                </div>
                <span class="precio">S/.6.50</span>
                <a href="/agregar/Yogurt Laive/6.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i5.jpg" alt="i5">
                <div class="info-producto">
                    <h3>Pan en bolsa</h3>
                    <p>500 gr</p>
                </div>
                <span class="precio">S/.8.50</span>
                <a href="/agregar/Pan en bolsa/8.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i6.jpg" alt="i6">
                <div class="info-producto">
                    <h3>Galletas de vainilla</h3>
                    <p>6 unidades (222 gr)</p>
                </div>
                <span class="precio">S/.4.70</span>
                <a href="/agregar/Galletas de vainilla/4.70" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i7.jpg" alt="i7">
                <div class="info-producto">
                    <h3>Atún en lata</h3>
                    <p>140 gr</p>
                </div>
                <span class="precio">S/.5.80</span>
                <a href="/agregar/Atún en lata/5.80" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i8.jpg" alt="i8">
                <div class="info-producto">
                    <h3>Café Kirma</h3>
                    <p>180 gr</p>
                </div>
                <span class="precio">S/.21.90</span>
                <a href="/agregar/Café Kirma/21.90" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i9.jpg" alt="i9">
                <div class="info-producto">
                    <h3>Huevos</h3>
                    <p>15 unidades</p>
                </div>
                <span class="precio">S/.9.50</span>
                <a href="/agregar/Huevos/9.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i10.jpg" alt="i10">
                <div class="info-producto">
                    <h3>Chocolate Triangulo</h3>
                    <p>30 gr</p>
                </div>
                <span class="precio">S/.2.50</span>
                <a href="/agregar/Chocolate Triangulo/2.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i11.jpg" alt="i11">
                <div class="info-producto">
                    <h3>Gaseosa KR</h3>
                    <p>1500 ml</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="/agregar/Gaseosa KR/3.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i12.jpg" alt="i12">
                <div class="info-producto">
                    <h3>Gaseosa sprite</h3>
                    <p>1500 ml</p>
                </div>
                <span class="precio">S/.6.50</span>
                <a href="/agregar/Gaseosa sprite/6.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i13.jpg" alt="i13">
                <div class="info-producto">
                    <h3>Galletas oreo</h3>
                    <p>432 gr</p>
                </div>
                <span class="precio">S/.8.20</span>
                <a href="/agregar/Galletas oreo/8.20" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i14.jpg" alt="i14">
                <div class="info-producto">
                    <h3>Mayonesa</h3>
                    <p>190 gr</p>
                </div>
                <span class="precio">S/.5.80</span>
                <a href="/agregar/Mayonesa/5.80" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i15.jpg" alt="i15">
                <div class="info-producto">
                    <h3>Mermelada</h3>
                    <p>320 gr</p>
                </div>
                <span class="precio">S/.5.50</span>
                <a href="/agregar/Mermelada/5.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i16.jpg" alt="i16">
                <div class="info-producto">
                    <h3>Jamón San Fernando</h3>
                    <p>200 gr</p>
                </div>
                <span class="precio">S/.9.50</span>
                <a href="/agregar/Jamón San Fernando/9.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i17.jpg" alt="i17">
                <div class="info-producto">
                    <h3>Margarina Manti</h3>
                    <p>225 gr</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="/agregar/Margarina Manti/3.50" class="boton-compra">Añadir</a>
            </article>
 
            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i18.jpg" alt="i18">
                <div class="info-producto">
                    <h3>Mantequilla Laive</h3>
                    <p>200 gr</p>
                </div>
                <span class="precio">S/.7.50</span>
                <a href="/agregar/Mantequilla Laive/7.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i19.jpg" alt="i19">
                <div class="info-producto">
                    <h3>Café Ecco</h3>
                    <p>80 gr</p>
                </div>
                <span class="precio">S/.8.50</span>
                <a href="/agregar/Café Ecco/8.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i20.jpg" alt="i20">
                <div class="info-producto">
                    <h3>Café Altomayo</h3>
                    <p>170 gr</p>
                </div>
                <span class="precio">S/.25.10</span>
                <a href="/agregar/Café Altomayo/25.10" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i21.jpg" alt="i21">
                <div class="info-producto">
                    <h3>Leche Fresca Gloria</h3>
                    <p>946 ml</p>
                </div>
                <span class="precio">S/.5.80</span>
                <a href="/agregar/Leche Fresca Gloria/5.80" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i22.jpg" alt="i22">
                <div class="info-producto">
                    <h3>Leche sin lactosa Laive</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.5.20</span>
                <a href="/agregar/Leche sin lactosa Laive/5.20" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i23.jpg" alt="i23">
                <div class="info-producto">
                    <h3>Duraznos en almibar</h3>
                    <p>820 gr</p>
                </div>
                <span class="precio">S/.9.70</span>
                <a href="/agregar/Duraznos en almibar/9.70" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i24.jpg" alt="i24">
                <div class="info-producto">
                    <h3>Gaseosa Guarana</h3>
                    <p>450 ml</p>
                </div>
                <span class="precio">S/.2.00</span>
                <a href="/agregar/Gaseosa Guarana/2.00" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i25.jpg" alt="i25">
                <div class="info-producto">
                    <h3>Pan Chabata</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="/agregar/Pan Chabata/3.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i26.jpg" alt="i26">
                <div class="info-producto">
                    <h3>Pan caracol</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="/agregar/Pan caracol/3.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i27.jpg" alt="i27">
                <div class="info-producto">
                    <h3>Pan Francés</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.2.40</span>
                <a href="/agregar/Pan Francés/2.40" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i28.jpg" alt="i28">
                <div class="info-producto">
                    <h3>Gaseosa Concordia</h3>
                    <p>1500 ml</p>
                </div>
                <span class="precio">S/.4.00</span>
                <a href="/agregar/Gaseosa Concordia/4.00" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i29.jpg" alt="i29">
                <div class="info-producto">
                    <h3>Cifrut</h3>
                    <p>500 ml</p>
                </div>
                <span class="precio">S/.2.00</span>
                <a href="/agregar/Cifrut/2.00" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i30.jpg" alt="i30">
                <div class="info-producto">
                    <h3>Pulp</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.4.50</span>
                <a href="/agregar/Pulp/4.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i31.jpg" alt="i31">
                <div class="info-producto">
                    <h3>Yopimix</h3>
                    <p>125 gr</p>
                </div>
                <span class="precio">S/.2.50</span>
                <a href="/agregar/Yopimix/2.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i32.jpg" alt="i32">
                <div class="info-producto">
                    <h3>Helado de vainilla</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.14.50</span>
                <a href="/agregar/Helado de vainilla/14.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i33.jpg" alt="i33">
                <div class="info-producto">
                    <h3>Helado de fresa</h3>
                    <p>1000 ml</p>
                </div>
                <span class="precio">S/.14.50</span>
                <a href="/agregar/Helado de fresa/14.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i34.jpg" alt="i34">
                <div class="info-producto">
                    <h3>Queso Chedar</h3>
                    <p>170 gr</p>
                </div>
                <span class="precio">S/.8.40</span>
                <a href="/agregar/Queso Chedar/8.40" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i35.jpg" alt="i35">
                <div class="info-producto">
                    <h3>Chocolate Vizio</h3>
                    <p>63 gr</p>
                </div>
                <span class="precio">S/.4.20</span>
                <a href="/agregar/Chocolate Vizio/4.20" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i36.jpg" alt="i36">
                <div class="info-producto">
                    <h3>Galleta rellenitas</h3>
                    <p>6 unidades</p>
                </div>
                <span class="precio">S/.3.50</span>
                <a href="/agregar/Galleta rellenitas/3.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i37.jpg" alt="i37">
                <div class="info-producto">
                    <h3>Cereales Angel Chocolate</h3>
                    <p>250 gr</p>
                </div>
                <span class="precio">S/.6.50</span>
                <a href="/agregar/Cereales Angel Chocolate/6.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i38.jpg" alt="i38">
                <div class="info-producto">
                    <h3>Cereales Angel Maiz</h3>
                    <p>1000 gr</p>
                </div>
                <span class="precio">S/.14.50</span>
                <a href="/agregar/Cereales Angel Maiz/14.50" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i39.jpg" alt="i39">
                <div class="info-producto">
                    <h3>Avena</h3>
                    <p>900 gr</p>
                </div>
                <span class="precio">S/.9.30</span>
                <a href="/agregar/Avena/9.30" class="boton-compra">Añadir</a>
            </article>

            <article class="tarjeta-producto">
                <img class="imagen-producto" src="./img/i40.jpg" alt="i40">
                <div class="info-producto">
                    <h3>Chicle trident</h3>
                    <p>5 unidades</p>
                </div>
                <span class="precio">S/.1.50</span>
                <a href="/agregar/Chicle trident/1.50" class="boton-compra">Añadir</a>
            </article>

        </section>
    </main>

    <footer>
        <p>&copy; Todos los derechos reservados 2026</p>
    </footer>
    
    <aside class="carrito-flotante oculto">
    <h2>Tu Carrito</h2>
    
    {% if session.get('carrito') %}
        <div class="lista-carrito">
            {% for id, item in session['carrito'].items() %}
            <div class="item-carrito">
                <div>
                    <strong>{{ item.nombre }}</strong>
                    <p>Cant: {{ item.cantidad }}</p>
                </div>
                <span>S/.{{ "%.2f"|format(item.precio * item.cantidad) }}</span>
            </div>
            {% endfor %}
        </div>
        
        <div class="total-carrito">
            <strong>Total: S/.{{ "%.2f"|format(total_actual) }}</strong>
        </div>
        
        <a href="/limpiar" class="btn-vaciar">Vaciar Carrito</a>
    {% else %}
        <p class="carrito-vacio">El carrito está vacío.</p>
    {% endif %}
</aside>

<button class="btn-toggle-carrito" onclick="toggleCarrito()">🛒</button>

<script>
    function toggleCarrito() {
        document.querySelector('.carrito-flotante').classList.toggle('oculto');
    }
</script>

</body>
</html>
"""

@app.route('/')
def inicio():
    carrito = session.get('carrito', {})
    total_actual = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render_template_string(index_html, total_actual=total_actual, session=session)

@app.route('/productos')
def productos():
    carrito = session.get('carrito', {})
    total_actual = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render_template_string(productos_html, session=session, total_actual=total_actual)

@app.route('/limpiar')
def limpiar_carrito():
    session.pop('carrito', None)
    return redirect(url_for('productos'))

@app.route('/agregar/<nombre>/<float:precio>')
def agregar_producto(nombre, precio):
    if 'carrito' not in session:
        session['carrito'] = {}
    for id, item in session['carrito'].items():
        if item['nombre'] == nombre:
            item['cantidad'] += 1
            break
    else:
        nuevo_id = str(len(session['carrito']) + 1)
        session['carrito'][nuevo_id] = {'nombre': nombre, 'precio': precio, 'cantidad': 1}
    session.modified = True
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(debug=True)
