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

@app.route("/")
def index():
    return render_template('ingresar.html')

#INGRESAR DATOS
@app.route('/ingresar', methods=['POST'])
def ingresar():
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
    return redirect(url_for('index'))

#PESTAÑA EDITAR FRUTA
@app.route('/editar')
def editar():
    cursorEdi = mysql.connection.cursor() #CC = cursor de la consulta
    cursorEdi.execute('select * from tbfrutas')
    conFru = cursorEdi.fetchall( ) 
    return render_template('consulta.html', listaF = conFru) 

#ACTUALIZAR FRUTA
@app.route('/actualizarVista/<string:id>')
def actualizarVista(id):
    cursorUpdV = mysql.connection.cursor()
    cursorUpdV.execute('select * from tbfrutas where id = %s', (id,))
    confru = cursorUpdV.fetchone()
    return render_template('editarFruta.html', UpdateFruta = confru)

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
    return redirect(url_for('editar'))

#ELIMINACION DATOS
@app.route('/confirmacion/<id>')
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
    return redirect(url_for('index'))

#CONSULTAR POR NOMBRE
@app.route("/consulta")
def consulta():
    return render_template('consultaxnombre.html')

@app.route("/buscarxnombre")
def buscarxnombre():
    varfrutas = request.form.get('txtFrutas', False)
    cursorCons = mysql.connection.cursor()
    cursorCons.execute('select * from tbfrutas where fruta = %s order by fruta', [varfrutas])
    datos = cursorCons.fetchone()
    print (datos)
    return render_template('consultaxnombre.html', listaF = datos)

if __name__ == '__main__': 
    app.run(port=5000, debug=True)
