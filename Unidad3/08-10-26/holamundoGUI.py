from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    # Se agrega la etiqueta <a> para crear el enlace que se puede abrir
    return """
    <h1>!Hola Mundo desde Flask!</h1>
    <p>Gana 500 pesos en el siguiente enlace:</p>
    <a href="https://media.tenor.com/AeDxZNLg97sAAAAe/mono-que-saca-el-dedo.png" target="_blank">GANA 500 GRATIS</a>
    """

if __name__ == "__main__":
    app.run(debug=True)