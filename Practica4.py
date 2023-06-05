from tkinter import *
from tkinter import ttk
import tkinter as tk
from DatosP4 import *


controlador = ConstructorBD()

def ejecutaRegistro():
    controlador.registrarBebidas(varNom.get(), varClas.get(), varMarc.get(), varPrec.get())
def ejecutaEliminar():
    controlador.eliminarRBebidas(varId.get())
def ejecutaConsulta():
    rUsu = controlador.consultarRegistros()
    tablaCons.delete(*tablaCons.get_children())
    for usu in rUsu:
        tablaCons.insert('', 'end', text=usu[0], values=(usu[1], usu[2], usu[3], usu[4]))
def ejecutaActualizacion():
    controlador.actualizarRegistros(varIdA.get(), varNomb.get(), varClasi.get(), varMarca.get(), varPreci.get())
def consultaUno():
    conx = sqlite3.connect("C:/Users/mimoc/OneDrive/OTROS/GitHub/POOS181/RegistroBebidas.db")
    cursor = conx.cursor()
    consulta = 'select avg(precio) from tbrRegistros'
    cursor.execute(consulta)
    res = cursor.fetchone()
    precioprom = res[0]
    messagebox.showinfo ('Precio promedio', 'El precio promedio de las bebidas es: '+str(precioprom)+'')
    conx.close()
def consultaDos():
    controlador.consultaDos(varMarcaUno.get())
def consultaTres():
    controlador.consultaTres(varClasifTres.get())

ventana = Tk()
ventana.title('Almacen de bebidas - Practica 4')
ventana.geometry('500x300')

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#Pestaña agregar producto
titulo = Label(pestana1, text='Registro productos').pack()
varNom = tk.StringVar()
lblNom = Label(pestana1, text='Nombre: ').pack()
txtNom = Entry(pestana1, textvariable=varNom).pack()
varClas = tk.StringVar()
lblClas = Label(pestana1, text='Clasificación: ').pack()
txtClas = tk.Entry(pestana1, textvariable=varClas).pack()
varMarc = tk.StringVar()
lblMarc = Label(pestana1, text='Marca: ').pack()
txtMarc = tk.Entry(pestana1, textvariable=varMarc).pack()
varPrec = tk.StringVar()
lblPrec = Label(pestana1, text='Precio: ').pack()
txtPrec = tk.Entry(pestana1, textvariable=varPrec).pack()

btnRegistrar = Button(pestana1, text='Guardar', command=ejecutaRegistro).pack()

#Pestaña eliminar producto
titulo2 = Label(pestana2, text='Eliminar productos').pack()
varId = tk.StringVar()
lblId = Label(pestana2, text='Id: ').pack()
txtId = Entry(pestana2, textvariable=varId).pack()

btnEliminar = Button(pestana2, text='Eliminar', command=ejecutaEliminar).pack()

#Pestaña consulta
titulo3= Label(pestana3,text= 'Registros', fg='purple', font=('Modern',18)).pack()
tablaCons = ttk.Treeview(pestana3)
tablaCons['columns'] = ('Nombre', 'Clasificacion', 'Marca', 'Precio')
tablaCons.column('#0', width=50, minwidth=50)
tablaCons.column('Nombre', width=120, minwidth=120)
tablaCons.column('Clasificacion', width=150, minwidth=150)
tablaCons.column('Marca', width=100, minwidth=100)
tablaCons.column('Precio', width=100, minwidth=100)
tablaCons.heading('#0', text='ID', anchor=tk.CENTER)
tablaCons.heading('Nombre', text='Nombre', anchor=tk.CENTER)
tablaCons.heading('Clasificacion', text='Clasificacion', anchor=tk.CENTER)
tablaCons.heading('Marca', text='Marca', anchor=tk.CENTER)
tablaCons.heading('Precio', text='Precio', anchor=tk.CENTER)
tablaCons.pack()

btnConsulta = Button(pestana3, text="Consultar", command=ejecutaConsulta).pack()

#Pestaña actualizar
titulo4 = Label(pestana4, text='Registro productos').pack()
varIdA = tk.StringVar()
lblIdA = Label(pestana4, text='Id: ').pack()
txtIdA = Entry(pestana4, textvariable=varIdA).pack()
varNomb = tk.StringVar()
lblNomb = Label(pestana4, text='Nombre: ').pack()
txtNomb = Entry(pestana4, textvariable=varNomb).pack()
varClasi = tk.StringVar()
lblClasi = Label(pestana4, text='Clasificación: ').pack()
txtClasi = tk.Entry(pestana4, textvariable=varClasi).pack()
varMarca = tk.StringVar()
lblMarca = Label(pestana4, text='Marca: ').pack()
txtMarca = tk.Entry(pestana4, textvariable=varMarca).pack()
varPreci = tk.StringVar()
lblPreci = Label(pestana4, text='Precio: ').pack()
txtPreci = tk.Entry(pestana4, textvariable=varPreci).pack()

btnRegistrar = Button(pestana4, text='Actualizar', command=ejecutaActualizacion).pack()

#Pestaña consultas
titulo5 = Label(pestana5, text='Consultas').pack()
btnConsulta1 = Button(pestana5, text='Precio promedio de bebidas', command=consultaUno).pack()
varMarcaUno = tk.StringVar()
lblMarcaUno = Label(pestana5, text='Marca: ').pack()
txtMarcaUno = Entry(pestana5, textvariable=varMarcaUno).pack()
btnConsulta2 = Button(pestana5, text='Cantidad de bebidas por marca', command=consultaDos).pack()
varClasifTres = tk.StringVar()
lblClasifTes = Label(pestana5, text='Clasificación: ').pack()
txtClasifTres = Entry(pestana5, textvariable=varClasifTres).pack()
btnConsulta3 = Button(pestana5, text='Cantidas por clasificación', command=consultaTres).pack()

panel.add(pestana1, text='Alta bebidas')
panel.add(pestana2, text='Baja bebidas')
panel.add(pestana3, text='Consultar bebidas')
panel.add(pestana4, text='Actualizar bebidas')
panel.add(pestana5, text='Consultas')


ventana.mainloop()