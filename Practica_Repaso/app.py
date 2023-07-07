#configuracion para el servidor
from flask import Flask, render_template, request, redirect, url_for, flash #importación de framework
from flask_mysqldb import MySQL

#Inicalizacion del APP
app = Flask(__name__) #se le indica que se va a trabajar con Flask - inicialización APP
#Configuración de la conexión
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_fruteria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/') 
def ingresar():
    cc = mysql.connection.cursor() #CC = cursor de la consulta
    cc.execute('select * from tbfrutas')
    conFru = cc.fetchall( ) 
    return render_template('ingresar.html', listaF = conFru) 
#Ruta http://localhost:5000/guardar - tipo POST para insert
@app.route('/ingresar', methods=['POST'])
def guardar():
    if request.method=='POST':
        #pasamos a variables el contenido de los input
        Vfruta=request.form['txtFruta']
        Vtemporada=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']
        #conectar a la BD y ejecutar
        CS = mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta, temporada, precio, stock) values (%s,%s,%s,%s)', (Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()
    flash('La fruta se ha guardado correctamente')
    return redirect(url_for('ingresar'))

@app.route('/editar/<string:id>')
def editar(id):
    cursorID = mysql.connection.cursor()
    cursorID.execute('select * from tbfrutas  where id = %s', (id,))
    consultaID = cursorID.fetchone()
    return render_template('editarFruta.html', UpdateFruta = consultaID)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varFruta = request.form['txtFruta']
        varTemporada = request.form['txtTemporada']
        varPrecio = request.form['txtPrecio']
        varStock = request.form['txtStock']
        cursorUpd = mysql.connection.cursor()
        cursorUpd.execute('update tbfrutas set fruta = %s, temporada = %s, precio = %s, stock = %s where id = %s', (varFruta, varTemporada, varPrecio, varStock, id))
        mysql.connection.commit()
    flash ('La fruta '+varFruta+' se actualizo correctamente.')
    return redirect(url_for('ingresar'))

@app.route("/confirmacion/<id>")
def eliminar(id):
    cursorConfi = mysql.connection.cursor()
    cursorConfi.execute('select * from tbfrutas where id = %s', (id,))
    consuF = cursorConfi.fetchone()
    return render_template('borrar_frutas.html', fruta=consuF)

@app.route("/eliminar/<id>", methods=['POST'])
def eliminarBD(id):
    cursorDlt = mysql.connection.cursor()
    cursorDlt.execute('delete from tbfrutas where id = %s', (id,))
    mysql.connection.commit()
    flash('Se elimino la fruta con id '+ id)
    return redirect(url_for('ingresar'))

@app.route("/buscar", methods=['POST'])
def buscar():
    if request.method == 'POST':
        varFruta = request.form['txtFruta']
        cursorBuq = mysql.connection.cursor()
        cursorBuq.execute('select * from tbfrutas where fruta = %s', (varFruta))
        busq = cursorBuq.fetchone()
        mysql.connection.commit()
    return render_template('ingresar.html', busqXn = busq)

#permite ejecutar el servidor en el puerto 5000
if __name__ == '__main__': 
    app.run(port=5000, debug=True)
