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
    metodo.leer_xmlconfiguracion(lista_recursos,perfil)
    print(perfil.filename)
    for x in lista_recursos:
        print(x.iden)
    return perfil.filename
    
if __name__ == '__main__':
    app.run(debug=True)
