import os
import shutil
import sys
from xml.dom.minidom import parse
from docutils.nodes import docinfo

def extractNFeData(xmle):
    xml = xmle
    doc = parse(xml)
    node = doc.documentElement
    nfeData = []

    ides = doc.getElementsByTagName("ide")

    for ide in ides:
        nfeData.append(ide.getElementsByTagName("nNF")[0].childNodes[0].nodeValue)

    emits = doc.getElementsByTagName("emit")

    for emit in emits:
        nfeData.append(emit.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xNome")[0].childNodes[0].nodeValue)

    dests = doc.getElementsByTagName("dest")

    for dest in dests:
        nfeData.append(dest.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("xNome")[0].childNodes[0].nodeValue)

    return nfeData


# Dados de Produtos
def extractNFeProd(xmle):
    doc = parse(xmle)
    node = doc.documentElement
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
