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
    def actualizarRegistros(self, id, nomb, clas, marc, prec):
        conx = self.conexionBD()
        if(id == ''):
            messagebox.showwarning('Error', 'Ingrese un ID.')
            conx.close()
        else:
            conx = self.conexionBD()
            if(nomb == '' or clas == '', marc == '', prec == ''):
                messagebox.showwarning('Error', 'Formulario incompleto.')
                conx.close()
            else:
                cursor = conx.cursor()
                datosA = (nomb, clas, marc, prec)
                sqlUpdate = 'update tbrRegistros set (nombre, clasificacion, marca, precio) = (?,?,?,?) where id = '+id
                cursor.execute(sqlUpdate, datosA)
                conx.commit()
                conx.close()
                messagebox.showinfo('Exit', 'Registro actualizado correctamente.')