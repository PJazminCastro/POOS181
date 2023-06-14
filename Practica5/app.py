#configuracion para el servidor
from flask import Flask  #importación de framework
from flask_mysqldb import MySQL

#Inicalizacion del APP
app = Flask(__name__) #se le indica que se va a trabajar con Flask - inicialización APP
#Configuración de la conexión
app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MySQL_DB']='bdFlask'
mysql=MySQL(app)

#Ruta principal
@app.route('/') #declara la ruta http://localhost:5000 - RUTA RAIZ/INDEX
def index():
    return "Hola mundo FLASK"

@app.route('/guardar')
def guardar():
    return "Se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"


#permite ejecutar el servidor en el puerto 5000
if __name__ == '__main__': 
    app.run(port=5000, debug=True)
