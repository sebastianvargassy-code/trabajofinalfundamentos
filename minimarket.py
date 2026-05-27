from flask import Flask, render_template_string, redirect, url_for, request
app = Flask(__name__)
USUARIO_CORRECTO = "Sebastian"
PASSWORD_CORRECTO = "1234"


# Contador de intentos
intentos = 0


# Página principal (Login)
login_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Inicio de Sesión</h1>
    <form method="POST">
        <label>Usuario:</label>
        <input type="text" name="usuario" required>
        <br><br>
        <label>Contraseña:</label>
        <input type="password" name="password" required>
        <br><br>
        <label for="tipo_usuario">Rol:</label>
        <select id="tipo_usuario" name="tipo_usuario">
            <option value="usuario">Usuario</option>
            <option value="admin">Administrador</option>
        </select>
        <br><br>
        <button type="submit">Validar</button>
    </form>
    <br>
    <h3>{{ mensaje }}</h3>
    <h4>Intentos restantes: {{ restantes }}</h4>
</body>
</html>
"""


# Página de bloqueo
bloqueado_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
 <title>Sistema Bloqueado</title>
</head>
<body>
    <h1>Sistema Bloqueado</h1>
    <h2>Ha superado el máximo de intentos permitidos.</h2>
</body>
</html>
"""
# INDEX
index_html = """
<!DOCTYPE html>
    <html lang="es">
    <head>
   
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,
    initial-scale=1.0">
    <title>Minimarket </title>
    <link rel="stylesheet" href="css/styles.css">
    </head>
    <style>
    *{
    margin: 0;
   
    box-sizing: border-box;
}
body{
    font-family: Arial, sans-serif;
    background-color:#d4c196;
    color:#000000;
    padding: 20px;
}
h1, h2{


    color: #d4c196;


}
header{
display: flex;
justify-content: space-between;
align-items: center;
background-color: #5a3907;
color: rgb(255, 254, 254);
padding: 15px 20px;


}
nav ul{


    display: flex;
    gap: 15px;
    list-style: none;
}
nav a{


    color: #d4c196;
    text-decoration: none;
    font-weight:bold;
}
.contenedor-tarjetas{
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    justify-content: space-evenly;
    margin: 30px 0;
}
.tarjeta{


    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0,0.1);
 width: 280px;
}
.galeria img{


    width:100%;
    border-radius: 8px;


}
@media screen and (max-width: 768px)
{


    header{


        flex-direction: column;
    }
    .contenedor-tarjetas{
        flex-direction: column;
        align-items: center;
    }
}
</style>
    <body>
        <header>
            <h1>Minimarket </h1>
            <nav>
                <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="http://127.0.0.1:5000/productos">Productos</a></li>                <li><a href="#">Contacto</a></li>
                <li><a href="#">Carrito</a></li>
           
                </ul>
            </nav>
        </header>
        <main>
             <p> Minimarket Nelly siempre a sus disposición cuenta con los productos indispensables para abastecer a la comunidad </p>

    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmrN-Sgy3YWNqUsjVziPRu9zKMV46mrh57sQ&s" alt="Descripción de la imagen">
</a>
        </main>
        <footer>
            <p>&copy; 2025 Mi sitio web. Todos los derechos reservados.</p>
        </footer>
    </body>
</html>
"""


# PRODUCTOS
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


@app.route('/inicio')
def inicio():
    return render_template_string(index_html)


@app.route('/productos')
def productos():
    return render_template_string(productos_html)


@app.route("/", methods=["GET", "POST"])
def login():
    global intentos
    mensaje = ""
    restantes = 3 - intentos


    # Verificar si el sistema está bloqueado
    if intentos >= 3:
        return redirect(url_for("bloqueado"))


    # Validar formulario
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]


        # Validar credenciales
        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO:
            intentos = 0 # Reiniciar intentos al tener éxito
            return redirect(url_for("inicio"))
        else:
            intentos += 1
            restantes = 3 - intentos
            mensaje = "Usuario o contraseña incorrectos"


            # Bloquear al tercer intento
            if intentos >= 3:
                return redirect(url_for("bloqueado"))


    return render_template_string(
        login_html,
        mensaje=mensaje,
        restantes=restantes
    )


# Ruta bloqueo
@app.route("/bloqueado")
def bloqueado():
    return render_template_string(bloqueado_html)
if __name__ == '__main__':
    app.run(debug=True)

