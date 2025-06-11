from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return """
<!DOTYPE html>
<html>
<head>
    
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>datosSqlite3</title>

    <style>

</style> 
</head>
<body>
   <header>
   <h1>api-sqlt3</h1>
  </header>
  <main>
  <section>
  <h2>¿Que es api-sqlt3?</h2>
  <p>es una api de funcion de datos con  sqlite3 una vercion de sql para dispositivos moviles cuenta con una capacida de gestionar tu base de datos de una mare rapida y sencilla.</p> 
  <div class="tablas">
   <h3>crea tus tablas</h3>
   <p>crea tu base de datos en pocos minutos</p>
   <button onclick="crear-datos()">crear</button>

  </div>
 
  <div class="agregar">
     <h3>agregar a tus proyecto</h3
   
  </div>

 </section>
 </main>
   <scritp>
      function crear-datos() {
       let crear-datos = prompt("ingresa un dato");
       alert(crear-datos)
     }
   </scritp>
</body>
</html>
     """

@app.route("/info")
def info():
    return jsonify({"mensaje": "Esta es una aplicación Flask básica"})

if __name__ == "__main__":
    app.run(port=5003)
