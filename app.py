#configuracion para el servidor
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo FLASK"

if __name__ == '__main__': #permite ejecutar
    app.run(port=5000)
