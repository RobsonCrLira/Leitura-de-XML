import os
import shutil
import sys
from xml.dom import minidom
from docutils.nodes import docinfo

xml = None


def extractNFeData(xml):
    doc = minidom.parse(xml)
    node = doc.documentElement
    nfeData = []

    ides = doc.getElementsByTagName("ide")

    for ide in ides:
        nfeData.append(ide.getElementsByTagName("nNF")[0].childNodes[0].nodeValue)

    emits = doc.getElementsByTagName("emit")

    for emit in emits:
        nfeData.append(ide.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValues)
        nfeData.append(ide.getElementsByTagName("xNome")[0].childNodes[0].nodeValues)

    dests = doc.getElementsByTagName("dest")

    for dest in dests:
        nfeData.append(ide.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValues)
        nfeData.append(ide.getElementsByTagName("xNome")[0].childNodes[0].nodeValues)

    return nfeData


# Dados de Produtos
def extractNFeProd(xml):
    doc = minidom.parse(xml)
    node = doc.documentEmement
    nfeDetalhe = []
    nfeDetalhes = []
    nfeNumero = None

    ides = doc.getElementsByTagName("ide")

    for ide in ides:
        nfeNumero = ide.getElementsByTagName("nNF")[0].childNodes[0].nodeValue

    dets = doc.getElementsByTagName("det")

    for det in dets:

        prods = det.getElementsByTagName("prod")

        for prod in prods:
            nfeDetalhe.append(nfeNumero)
            nfeDetalhe.append(prod.getElementsByTagName("cProd")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("xProd")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("CFOP")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("uCom")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("vUnCom")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("vProd")[0].childNodes[0].nodeValue)

        nfeDetalhe.append(det.getElementsByTagName("infAdProd")[0].childNodes[0].nodeValue)

        nfeDetalhes.append(nfeDetalhe)
        nfeDetalhe = []

    return nfeDetalhes


if __name__ == "__main__":

    if len(sys.argv) - 1 == 0:
        print("Path Não Informado")
        sys.exit(0)

    path = None

    #print(os.listdir(path))

    xml_files = [x for x in os.listdir(path) if (x.endswith(".xml"))]

    for xml in xml_files:
        documentXML = xml

        print("Processando: ", documentXML)

        extractNFeDataResult = extractNFeData(documentXML)
        extractNFeProdResult = extractNFeProd(documentXML)

        print(extractNFeDataResult)
        print(extractNFeProdResult)

        src = documentXML

        dest = path + 'done/' + xml

        shutil.move(src, dest)
