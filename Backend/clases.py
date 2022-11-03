import string


class Recurso:
    iden:string 
    nombre:string
    abrebiatura:string
    metrica:string
    tipo:string
    valor_hora:float

    def __init__(self,id, nombre,abrebiatura, metrica, tipo, valor_hora):
        self.iden = id
        self.nombre = nombre
        self.abrebiatura = abrebiatura
        self.metrica=metrica
        self.tipo=tipo
        self.valor_hora=valor_hora

class Categoria:
    iden:string 
    nombre:string
    descripcion:string
    cargaTrabajo:string
    listaconfi:list

    def __init__(self,id, nombre,descripcion, cargatrabajo):
        self.iden = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cargaTrabajo=cargatrabajo
        self.listaconfi=[]
class Configuracion:
    iden:string 
    nombre:string
    descripcion:string
    lista_recurso_confi:list

    def __init__(self,id, nombre,descripcion):
        self.iden = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.lista_recurso_confi=[]
class Recurso_confi:
    iden:string 
    numero:float
    def __init__(self,id, numero):
        self.iden = id
        self.numero = numero

class Cliente:
    iden:string 
    nombre:string
    usuario:string
    clave:string
    direccion:string
    correo:string
    deuda:float
    listainstancia:list
    listadeuda:list

    def __init__(self,id, nombre,usuario, clave, direccion, correo):
        self.iden = id
        self.nombre = nombre
        self.usuario = usuario
        self.clave=clave
        self.direccion=direccion
        self.correo=correo
        self.deuda=0.0
        self.listainstancia=[]   
        self.listadeuda=[]   
class Instrancia:
    iden:string 
    idconfi:string
    nombre:string
    fecha_inicio:string
    estado:string
    fecha_final:string

    def __init__(self,id, idconfi,nombre, fechainicio, estado, fechafinal):
        self.iden = id
        self.idconfi = idconfi
        self.nombre = nombre
        self.fecha_inicio=fechainicio
        self.estado=estado
        self.fecha_final=fechafinal
class Consumo:
    idencliente:string 
    ideninstancia:string
    tiempo:float
    fechahora:string

    def __init__(self,idcliente, ideninstancia,tiempo, fechahora):
        self.idencliente = idcliente
        self.ideninstancia = ideninstancia
        self.tiempo = tiempo
        self.fechahora=fechahora
class Datos_factura:
    deudaconsumo:float
    descripcion:string
    categoria:string
    idconfi:string
    
    def __init__(self,deuda, descripcion, categoria, confi):
        self.deudaconsumo=deuda
        self.descripcion=descripcion
        self.categoria=categoria    
        self.idconfi=confi  