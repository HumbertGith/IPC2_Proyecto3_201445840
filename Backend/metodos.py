
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
        if archivo.readable():
                print(True)
                xml_data= ET.fromstring(archivo.read())
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



                     
                        

                      

                       

        else:
                print(False)
    def leer_xmlconfiguracion_categoria(listacategoria:list, archivo):
        if archivo.readable():
                print(True)
                xml_dat= ET.fromstring(archivo.read())
                lst_empresas= xml_dat.findall('listaCategorias')
                for recursos in lst_empresas:
                    categoria=recursos.findall("categoria")
                    for cate in categoria:
                        idencatego=""
                        catego=Categoria("","","","")
                        idencatego=cate.attrib.values()
                        for x in idencatego:
                            idencatego=x
                            catego.iden=idencatego
                        nombrecatego=cate.find('nombre').text
                        catego.nombre=nombrecatego
                        categodescripcion=cate.find('descripcion').text
                        catego.descripcion=categodescripcion
                        cargacatego=cate.find('cargaTrabajo').text
                        catego.cargaTrabajo=cargacatego
                        listacategoria.append(catego)
                        print(catego.iden)

                       

        else:
                print(False)