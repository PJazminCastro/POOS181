from tkinter import messagebox
import sqlite3
import bcrypt

class ConstructorBD:

    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/mimoc/OneDrive/OTROS/GitHub/POOS181/RegistroBebidas.db")
            print('Conectado a la BD')
            return conexion
        except sqlite3.OperationalError:
            print('No se logro la conexión')
    def registrarBebidas(self, nombre, clasificacion, marca, precio):
        conx = self.conexionBD()
        if(nombre == '' or clasificacion == '' or marca == '' or precio == ''):
            messagebox.showwarning('Error', 'Formulario incompleto.')
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (nombre, clasificacion, marca, precio)
            sqlInsert = 'insert into tbrRegistros(nombre, clasificacion, marca, precio) values (?,?,?,?)'
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo('Exito', 'Registro guardado.')
    def eliminarRBebidas(self, id):
        conx = self.conexionBD()
        if(id == ''):
            messagebox.showwarning('Error', 'Ingrese un ID')
            conx.close()
        else:
            conx = self.conexionBD()
            cursor = conx.cursor()
            sqlDelete = 'delete from tbrRegistros where id = '+id+''
            cursor.execute(sqlDelete)
            conx.commit()
            conx.close()
            messagebox.showinfo('Exito', 'Registro eliminado correctamente.')
    def consultarRegistros(self):
        conx = self.conexionBD()
        try:
            cursor = conx.cursor()
            sqlSelect = 'select * from tbrRegistros'
            cursor.execute(sqlSelect)
            RSUuarios = cursor.fetchall()
            conx.close()
            return RSUuarios
        except sqlite3.OperationalError:
            print('Error de consulta')
    def actualizarRegistros(self, id, nombre, clasificacion, marca, precio):
        conx = self.conexionBD()
        if(id == ''):
            messagebox.showwarning('Error', 'Ingrese un ID')
            conx.close()
        else:
            conx = self.conexionBD()
            if(nombre == '' or clasificacion == '' or marca == '' or precio == ''):
                messagebox.showwarning('Error', 'Formulario incompleto.')
                conx.close()
            else:
                cursor = conx.cursor()
                datos = (nombre, clasificacion, marca, precio)
                sqlUpdate = 'update tbrRegistros set (nombre, clasificacion, marca, precio) = (?,?,?,?) where id = '+id
                cursor.execute(sqlUpdate, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo('Exito', 'Registro actualizado correctamente.')
    def consultaDos(self, marcaUno):
        conx = self.conexionBD()
        cursor = conx.cursor()
        if(marcaUno == ''):
            messagebox.showwarning('Error', 'Formulario incompleto.')
            conx.close()
        else:
            consultados = 'select count(*) from tbrRegistros where marca = ?'
            cursor.execute(consultados, (marcaUno,))
            resu = cursor.fetchone()
            canbebidas = resu[0]
            messagebox.showinfo('Cantidad x marca', 'La cantidad de bebidas de la marca '+marcaUno+'  es: '+str(canbebidas))
            conx.close()
    def consultaTres(self, clasifTres):
        conx = self.conexionBD()
        cursor = conx.cursor()
        if(clasifTres == ''):
            messagebox.showwarning('Error', 'Formulario incompleto.')
            conx.close()
        else:
            consultados = 'select count(*) from tbrRegistros where clasificacion = ?'
            cursor.execute(consultados, (clasifTres,))
            resu = cursor.fetchone()
            canbebida = resu[0]
            messagebox.showinfo('Cantidad x clasificación', 'La cantidad de bebidas de la clasificación '+clasifTres+'  es: '+str(canbebida))
            conx.close()
        