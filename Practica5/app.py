#configuracion para el servidor
from flask import Flask, render_template, request, redirect, url_for, flash #importación de framework
from flask_mysqldb import MySQL

#Inicalizacion del APP
app = Flask(__name__) #se le indica que se va a trabajar con Flask - inicialización APP
#Configuración de la conexión
app.config['MySQL_HOST']='localhost:3306'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MySQL_DB']='bdflask'
app.secret_key='mysecretkey'
mysql=MySQL(app)

#Ruta principal
@app.route('/') #declara la ruta http://localhost:5000 - RUTA RAIZ/INDEX
def index():
    return render_template('index.html')

#Ruta http://localhost:5000/guardar - tipo POST para insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method=='POST':
        #pasamos a variables el contenido de los input
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        #conectar a la BD y ejecutar
        CS = mysql.connection.cursor()
        CS.execute('insert into tbalbum(titulo,artista,anio) values (%s,%s,%s)', (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
    flash('El album se ha guardado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"


#permite ejecutar el servidor en el puerto 5000
if __name__ == '__main__': 
    app.run(port=5000, debug=True)
