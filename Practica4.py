from tkinter import *;
from tkinter import ttk;
from DatosP4 import *;
import tkinter as tk;

ventana = Tk()
ventana.title('Almacen de bebidas - Practica 4')
ventana.geometry('250x400')

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

#Pestaña agregar producto
titulo = Label(pestana1, text='Registro productos').pack()
varId = tk.StringVar()
lblId = Label(pestana1, text='Id: ').pack()
txtId = Entry(pestana1, textvariable=varId).pack()
varNom = tk.StringVar()
lblNom = Label(pestana1, text='Nombre: ').pack()
txtNom = Entry(pestana1, textvariable=varNom).pack()
varClas = tk.StringVar()
lblClas = Label(pestana1, text='Clasificación: ').pack()
txtClas = tk.Entry(pestana1, textvariable=varClas).pack()
varPrec = tk.StringVar()
lblPrec = Label(pestana1, text='Precio: ').pack()
txtPrec = tk.Entry(pestana1, textvariable=varPrec).pack()

btnRegistrar = Button(pestana1, text='Guardar').pack()

#Pestaña eliminar producto
titulo2 = Label(pestana2, text='Eliminar productos')
varId = tk.StringVar()
lblId = Label(pestana1, text='Id: ').pack()
txtId = Entry(pestana1, textvariable=varId).pack()

btnEliminar = Button(pestana2, text='Eliminar').pack()

#Pestaña consulta
subCons= Label(pestana3,text= 'Registros', fg='purple', font=('Modern',18)).pack()
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

btnConsulta = Button(pestana3, text="Consultar").pack()

panel.add(pestana1, text='Alta bebidas')
panel.add(pestana2, text='Baja bebidas')
panel.add(pestana3, text='Consultar bebidas')
panel.add(pestana4, text='Actualizar bebidas')

ventana.mainloop()