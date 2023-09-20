from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicalizacion del APP
app = Flask(__name__) #se le indica que se va a trabajar con Flask - inicialización APP
#Configuración de la conexión
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_Floreria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index():
    cc = mysql.connection.cursor() 
    cc.execute('select * from tbflores')
    conFlores = cc.fetchall( ) 
    return render_template('index.html', listflores = conFlores) 

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method=='POST':
        varNombre=request.form['txtNombre']
        varCantidad=request.form['txtCantidad']
        varPrecio=request.form['txtPrecio']
        CS = mysql.connection.cursor()
        CS.execute('insert into tbflores(nombre, cantidad, precio) values (%s,%s,%s)', (varNombre, varCantidad, varPrecio))
        mysql.connection.commit()
    flash('La flor se ha guardado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    cursorID = mysql.connection.cursor()
    cursorID.execute('select * from tbflores  where id = %s', (id,))
    consultaID = cursorID.fetchone()
    return render_template('editarFlor.html', UpdateFlor = consultaID)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        vaNombre = request.form['txtNombre']
        vaCantidad = request.form['txtCantidad']
        vaPrecio = request.form['txtPrecio']
        cursorUpd = mysql.connection.cursor()
        cursorUpd.execute('update tbflores set nombre = %s, cantidad = %s, precio = %s where id = %s', (vaNombre, vaCantidad, vaPrecio, id))
        mysql.connection.commit()
    flash ('La flor'+vaNombre+' se actualizo correctamente.')
    return redirect(url_for('index'))

@app.route("/confirmacion/<id>")
def eliminar(id):
    cursorConfi = mysql.connection.cursor()
    cursorConfi.execute('select * from tbflores where id = %s', (id,))
    consuF = cursorConfi.fetchone()
    return render_template('confirmacion.html', dltFlor=consuF)

@app.route("/eliminar/<id>", methods=['POST'])
def eliminarBD(id):
    cursorDlt = mysql.connection.cursor()
    cursorDlt.execute('delete from tbflores where id = %s', (id,))
    mysql.connection.commit()
    flash('Se elimino la flor con id '+ id)
    return redirect(url_for('index'))

if __name__ == '__main__': 
    app.run(port=5000, debug=True)