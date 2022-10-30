from flask import Flask, request

from metodos import *

lista_recursos=[]
lista_categoria=[]
lista_clientes=[]
metodo=Metodos
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/Configuracion",methods=['POST'])
def ObtenerDatos():
    perfil = request.files["confi"]
    perfil1=perfil
    metodo.leer_xmlconfiguracion(lista_recursos,perfil,lista_categoria,lista_clientes)
   
    print(perfil.filename)
    #for x in lista_recursos:
       # print(x.iden)
   
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
    return perfil.filename
    
if __name__ == '__main__':
    app.run(debug=True)
