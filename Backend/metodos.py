
import xml.etree.ElementTree as ET

from clases import *
class Metodos:
    def __init__(self) -> None:
        pass
    def leer_xmlconfiguracion(listarecurso:list, archivo):
        if archivo.readable():
                print(True)
                xml_data= ET.fromstring(archivo.read())
                lst_empresas= xml_data.findall('listaRecursos')
                for recursos in lst_empresas:
                    recurso=recursos.findall("recurso")
                    for recur in recursos:
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

                       

        else:
                print(False)