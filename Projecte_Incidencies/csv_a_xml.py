#Vull crear un fitxer XML en base a un CSV
#pasar d'un fitxer CSV a XML
#El fitxer CSV es el que es diu Incidencies.csv
#El fitxer XML vull que es digui Incidencies.xml
import csv
import xml.etree.ElementTree as ET
def csv_a_xml(fitxer_csv, fitxer_xml):
    arrel = ET.Element("Incidencies")

    with open(fitxer_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            incidencia = ET.SubElement(arrel, "Incidencia")
            for camp, valor in fila.items():
                subelement = ET.SubElement(incidencia, camp)
                subelement.text = valor

    arbre = ET.ElementTree(arrel)
    arbre.write(fitxer_xml, encoding='utf-8', xml_declaration=True)
# Exemple d'ús
csv_a_xml('Incidencies.csv', 'Incidencies.xml')

