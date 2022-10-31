
from re import X
import xml.etree.ElementTree as ET

from clases import *
class Metodos:
    def __init__(self) -> None:
        pass
    def incertar_lista_de_listas(lista:list, clase, claseagregar):
        for elemento in lista:
            if elemento.iden==clase.iden:
                elemento.lista_recurso_confi.append(claseagregar)
            else:
                return False



    def leer_xmlconfiguracion(listarecurso:list, archivo,listacategoria:list, listaclientes:list):
        with open(archivo, encoding='utf-8') as file:
            if file.readable():
                    print(True)
                    xml_data= ET.fromstring(file.read())
                    lst_empresas= xml_data.findall('listaRecursos')
                    for recursos in lst_empresas:
                        recurso=recursos.findall("recurso")
                        for recur in recurso:
                            idenrecurso=""
                            recu=Recurso("","","","","",0.0)
                            iden=recur.attrib.values()
                            for x in iden:
                                idenrecurso=x
                                recu.iden=idenrecurso
                            nombrerecurso=recur.find('nombre').text
                            recu.nombre=nombrerecurso
                            abrevaturarecurso=recur.find('abreviatura').text
                            recu.abrebiatura=abrevaturarecurso
                            metrica=recur.find('metrica').text
                            recu.metrica=metrica
                            tiporecurso=recur.find('tipo').text
                            recu.tipo=tiporecurso
                            valorrecurso=recur.find('valorXhora').text
                            recu.valor_hora=float(valorrecurso)
                            listarecurso.append(recu)
                    #lectura de lista categoria
                    lst_categoria= xml_data.findall('listaCategorias')
                    for recursos in lst_categoria:
                        categoria=recursos.findall("categoria")
                        for cate in categoria:
                            idencatego1=""
                            catego=Categoria("","","","")
                            idencatego=cate.attrib.values()
                            for x in idencatego:
                                idencatego1=x
                                catego.iden=idencatego1
                            nombrecatego=cate.find('nombre').text
                            catego.nombre=nombrecatego
                            categodescripcion=cate.find('descripcion').text
                            catego.descripcion=categodescripcion
                            cargacatego=cate.find('cargaTrabajo').text
                            catego.cargaTrabajo=cargacatego
                            listacategoria.append(catego)
                            #lectura de listas de configuracion por categoria
                            lst_conficatego=cate.findall("listaConfiguraciones")
                            for conficatego in lst_conficatego:
                                lst_conficatego_1=conficatego.findall('configuracion')
                                for conf in lst_conficatego_1:
                                    codconfi=""
                                    conficate=Configuracion("","","")
                                    idconfcatego=conf.attrib.values()
                                    for x in idconfcatego:
                                        codconfi=x
                                        conficate.iden=codconfi
                                    nombreconficate=conf.find('nombre').text
                                    conficate.nombre=nombreconficate
                                    confidescrip=conf.find('descripcion').text
                                    conficate.descripcion=confidescrip
                                    catego.listaconfi.append(conficate)
                                    #lectura de lista de recursos de confi
                                    lst_recursoconfi=conf.findall("recursosConfiguracion")
                                    for confirecu in lst_recursoconfi:
                                        lst_confi_recu=confirecu.findall("recurso")
                                        
                                        for recu_lst in lst_confi_recu:
                                            cod_lst_recu=""
                                            clase_recuso=Recurso_confi("",0.0)
                                            id_lst_recu=recu_lst.attrib.values()
                                            for  x in id_lst_recu:
                                                cod_lst_recu=x
                                                clase_recuso.iden=cod_lst_recu
                                            numero_lst_recu=recu_lst.text
                                            clase_recuso.numero=float(numero_lst_recu)
                                            #print(clase_recuso.numero)
                                            Metodos.incertar_lista_de_listas(catego.listaconfi,conficate,clase_recuso)
                    #lectura de lista de clientes
                    lst_cliente=xml_data.findall('listaClientes')
                    for lst_client in lst_cliente:
                        lst_client_us=lst_client.findall("cliente")
                        for cliente in lst_client_us:
                            idcliente=""
                            client=Cliente("","","","","","")
                            cod_cliente= cliente.attrib.values()
                            for x in cod_cliente:
                                idcliente=X
                                client.iden=idcliente
                            nombrecliente=cliente.find('nombre').text
                            client.nombre=nombrecliente
                            usuariocliente=cliente.find('usuario').text
                            client.usuario=usuariocliente
                            clavecliente=cliente.find('clave').text
                            client.clave=clavecliente
                            direccioncliente=cliente.find('direccion').text
                            client.direccion=direccioncliente
                            correocliente=cliente.find('correoElectronico').text
                            client.correo=correocliente
                            listaclientes.append(client)
                            lst_instancia=cliente.findall('listaInstancias')
                            for lst_instan in lst_instancia:
                                instancia=lst_instan.findall('instancia')
                                for instan in instancia:
                                    idintsnacia=""
                                    claseintsncia=Instrancia("","","","","","")
                                    codintancia= instan.attrib.values()
                                    for x in codintancia:
                                        idintsnacia=X
                                        claseintsncia.iden=idintsnacia
                                        idconfiintsancia=instan.find('idConfiguracion').text
                                        claseintsncia.idconfi=idconfiintsancia
                                        nombreintancia=instan.find('nombre').text
                                        claseintsncia.nombre=nombreintancia
                                        fechainicio=instan.find('fechaInicio').text
                                        claseintsncia.fecha_inicio=fechainicio
                                        estadointancia=instan.find('estado').text
                                        claseintsncia.estado=estadointancia
                                        fechafinal=instan.find('fechaFinal').text
                                        claseintsncia.fecha_final=fechafinal
                                        client.listainstancia.append(claseintsncia)





                     
                        

                      

                       

            else:
                    print(False)
    def leer_xmlconfiguracion_consumo(listaconsumo:list, archivo):
     with open(archivo, encoding='utf-8') as file:
            if file.readable():
                    print(True)
                    xml_data= ET.fromstring(file.read())
                    lst_empresas= xml_data.findall('consumo')
                    for consumo in lst_empresas:
                        clase_consumo = Consumo("","",0.0,"")
                        codigo=consumo.attrib.values()
                        listas=[]
                        for x in codigo:
                            #print("la llvae es:" ,x)
                            
                            listas.append(x)
                        clase_consumo.idencliente=listas[0]
                        #print(confi.iden)
                        clase_consumo.ideninstancia=listas[1]
                        tiempo=consumo.find('tiempo').text
                        clase_consumo.tiempo=tiempo
                        fecha=consumo.find('fechaHora').text
                        clase_consumo.fechahora=fecha
                        listaconsumo.append(clase_consumo)

                       

            else:
                    print(False)
    def existe_o_no_en_la_lista(lista:list, clase):
        encontrado=False
        for x in lista:
            if x.iden==clase.iden:
                encontrado=True
                break
        if encontrado==True:
            return True
        else:
            return False
            
