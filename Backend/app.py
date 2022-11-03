from fileinput import filename
from importlib.resources import path
import json
from tkinter import filedialog
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import webbrowser as wb

from metodos import *

lista_recursos=[]
lista_categoria=[]
lista_clientes=[]
lista_consumo=[]
metodo=Metodos


app = Flask(__name__)
try:
        lista_recursos=metodo.leerrecursos("recurso")
        lista_categoria=metodo.leerrecursos("catego")
        lista_clientes=metodo.leerrecursos("cliente")
        lista_consumo=metodo.leerrecursos("consumo")

except:
        print(" no se selecciono ningun archivo de configuracion o consumo")
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
@app.route("/Guardar",methods=['POST'])
def guardar():
    metodo.guardar_recursos(lista_recursos,"recurso")
    metodo.guardar_recursos(lista_categoria,"catego")
    metodo.guardar_recursos(lista_clientes,"cliente")
    metodo.guardar_recursos(lista_consumo, "consumo")
    return render_template('index.html',variable=" Se guardo la informacion de manera correcta")

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
        print(x.iden)
        i+=1
        for j in x.listainstancia:
            print(j.nombre)
    print("********************")
    for x in lista_consumo:
        print(x.tiempo)
    variable=metodo.mostrar_sistema(lista_recursos,lista_categoria,lista_clientes)
   
    print("***************************************")
    for x in lista_clientes:
        print(x.nombre)
        for j in x.listadeuda:
            print("***************************")
            print(str(j.descripcion))
            print(str(j.deudaconsumo))
            print(str(j.categoria))
            print(str(j.idconfi))
    return render_template("consulta.html",variable=variable)  
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
        metodo.existe_en_lista(lista_categoria,categoria)
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

            metodo.existe_en_lista(confi.lista_recurso_confi,recurso)
        else:
            print("el recurso ingresado no esta en el catalogo de recursos")
        metodo.existe_en_lista(categoria.listaconfi,confi)
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
        metodo.existe_en_lista(lista_clientes,clientes)
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
        metodo.existe_en_lista(clientes.listainstancia,instancia)
        return "<p>instancia agregada con exito!</p>"
@app.route("/consumo")
def consumo():
    return render_template("consumo.html")
@app.route("/consumo/Crear_consumo",methods=['POST'])

def crear_consumo():
        variable=""
        idencliente=request.form['idcliente']
        idinstancia=request.form['idinstancia']
        tiempo=request.form['tiempo']
        fecha=request.form['fecha']
        consumo= Consumo(idencliente,idinstancia,tiempo,fecha)
        if metodo.devolvertruofalse(lista_clientes,consumo)==True:
            lista_consumo.append(consumo)
            variable="El consumo fue agregado correctamente"
        else:
            variable="el nit o instancia no existen"
        return render_template("consumo.html",variable=variable)
@app.route("/factura")
def factura():
    return render_template("factura.html")
@app.route("/factura/Crear_factura",methods=['POST'])

def crear_factura():
    variable=""
    variable1=""
    iden=request.form['id']
    if metodo.devoloververdaderoofalse(lista_clientes,iden)==True:
      
        variable1=metodo.Generar_factura(lista_clientes,iden)
        variable="Factura generada"
    else:
        variable="El cliente no existe ingrese de nuevo"
    return render_template("factura.html" ,variable=variable, variable1=variable1)
@app.route("/deuda",methods=['POST'])
def deu():
    metodo.generar_deuda(lista_clientes,lista_recursos,lista_categoria,lista_consumo)
    
    return render_template('index.html',variable1="Datos agregados")      
@app.route("/reporte")
def reporte():
    var1=metodo.reporte_categoria(lista_clientes)
    var2=metodo.reporte_recursos(lista_clientes,lista_categoria,lista_recursos)
    return render_template("reporte.html", variable1=var1, variable2=var2)
@app.route("/ayuda",methods=['POST'])
def ayuda():
    try:
        configuracion=[('archivos pdf', '.pdf')]
        file = filedialog.askopenfilename(title="abrir",filetypes=configuracion, defaultextension=configuracion)
        wb.open_new(file)
        return render_template("index.html", datos="Nombre:   Luis Humberto Lemus Perez"+"\n"+"Carnet:       201445840"+"\n"+"Introduccion a la programcion y computacion 2"+"\n"+"Seccion:   D"+"\n"+"Proyecto 3"  )



    except:
        print("Hubo un error")
  
   
if __name__ == '__main__':
    app.run(debug=True)
   