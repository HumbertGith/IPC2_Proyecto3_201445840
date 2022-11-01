from fileinput import filename
from importlib.resources import path
from tkinter import filedialog
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

from metodos import *

lista_recursos=[]
lista_categoria=[]
lista_clientes=[]
lista_consumo=[]
metodo=Metodos
app = Flask(__name__)

#print(file)
@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/Configuracion",methods=['POST'])
def configuracion():
    perfil = request.files["confi"]
    filename= secure_filename(perfil.filename)
    perfil.save(path('BaseDatos',filename))
    file = filedialog.askopenfilename(title="abrir configuracion", filetypes=(("xml files","*.xml"),("all files", "*.*")))
    ruta=file
    
    metodo.leer_xmlconfiguracion(lista_recursos,ruta,lista_categoria,lista_clientes)
    consumo = request.files["consumo"]
    filename1= secure_filename(consumo.filename)
    consumo.save(path('BaseDatos',filename1))
    file1 = filedialog.askopenfilename(title="abrir consumos", filetypes=(("xml files","*.xml"),("all files", "*.*")))
    ruta=file1
    metodo.leer_xmlconfiguracion_consumo(lista_consumo,ruta)
    return render_template('index.html', respuesta1="el archivo de configuracion se envio correctamente", respuesta2="El mensaje de consumo se envio correctamente")

@app.route("/Consultar_Datos")
def Consultar_Datos():
    for x in lista_recursos:
        print(x.iden)
        print(x.nombre)
    print("*************************")
    for x in lista_categoria:
        print(x.iden)
        for j in x.listaconfi:
            print(j.nombre)
            for i in j.lista_recurso_confi:
                print(i.numero)
    i=1
    for x in lista_clientes:
        print(str(i)+x.nombre)
        i+=1
        for j in x.listainstancia:
            print(j.nombre)
    print("********************")
    for x in lista_consumo:
        print(x.tiempo)
    return render_template("consulta.html", variable= "algo \ndespues")  
@app.route("/recurso")
def recurso():
    return render_template("crearrecurso.html")
@app.route("/recurso/Crear_recurso",methods=['POST'])
def crear_recurso():
    iden=request.form['iden']
    nombre=request.form['nombre']
    abrebiatura=request.form['abre']
    metrica=request.form['metrica']
    tipo=request.form['tipo']
    valorhora=float(request.form['hora'])
    recurso= Recurso(iden,nombre,abrebiatura,metrica,tipo,valorhora)
    metodo.existe_en_lista(lista_recursos,recurso)
    return render_template('crearrecurso.html') 
categoria=Categoria("","","","")
@app.route("/categoria")
def categoria():
    return render_template("crearcategoria.html")
@app.route("/categoria/Crear_categoria",methods=['POST'])

def crear_categoria():
    try:
        global categoria
        idencategoria=request.form['iden']
        nombre=request.form['nombre']
        descripcion=request.form['des']
        carga=request.form['carga']
        categoria1=Categoria(idencategoria,nombre,descripcion,carga)
        categoria=categoria1
        lista_categoria.append(categoria)
        return "<p>categoria agregada con exito!</p>" 



    except:
        print("HUbo un error el ingreso de categoria")
@app.route("/categoria/Crear_configuracion",methods=['POST'])

def crear_configuracion():
    try:
        
        idenconfi=request.form['iden']
        nombre=request.form['nombre']
        descripcion=request.form['des']
        idrecurso=request.form['idrecu']
        cantidadrecurso=request.form['cantidad']

        confi=Configuracion(idenconfi,nombre,descripcion)
        recurso=Recurso_confi(idrecurso,cantidadrecurso)
        if metodo.existe_o_no_en_la_lista(lista_recursos,recurso)==True:

            confi.lista_recurso_confi.append(recurso)
        else:
            print("el recurso ingresado no esta en el catalogo de recursos")
        categoria.listaconfi.append(confi)
        return "<p>categoria agregada con exito!</p>" 



    except:
        print("HUbo un error el ingreso de categoria")  
clientes=Cliente("","","","","","") 
@app.route("/cliente")
def cliente():
    return render_template("crearcliente.html")
@app.route("/cliente/Crear_cliente",methods=['POST'])

def crear_cliente():
    try:
        global clientes
        iden=request.form['iden']
        nombre=request.form['nombre']
        usuario=request.form['us']
        clave=request.form['clave']
        direc=request.form['direc']
        correo=request.form['correo']
        cliente1=Cliente(iden,nombre,usuario,clave,direc,correo)
        clientes=cliente1
        lista_clientes.append(clientes)
        return "<p>cliente agregado con exito!</p>"
    except:
        print("Error al crear el cliente")
    
@app.route("/cliente/Crear_instancia",methods=['POST'])

def crear_instancia():
        iden=request.form['iden']
        idconfi=request.form['idconfi']
        nombre=request.form['nombre']
        fechainicio=request.form['fechainicio']
        estado=request.form['estado']
        fechafinal=request.form['fechafinal']
        instancia=Instrancia(iden,idconfi,nombre,fechainicio,estado,fechafinal)
        clientes.listainstancia.append(instancia)
        return "<p>instancia agregada con exito!</p>"
fecha=metodo.obtener_fecha("10/06/2022 89:90 guatemala")
print(fecha)
for x in fecha:
    print(x)
    for j in x :
        print(j)
if __name__ == '__main__':
    app.run(debug=True)
