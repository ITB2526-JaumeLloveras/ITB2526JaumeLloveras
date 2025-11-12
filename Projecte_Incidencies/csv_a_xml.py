#Vull crear un fitxer XML en base a un CSV
#pasar d'un fitxer CSV a XML
#El fitxer CSV es el que es diu Incidencies.csv i es troba a la mateixa carpeta que el codi
#El fitxer XML que vull crear, s'ha de dir Incidencies.xml
#Vull que es crei i es guardi en la mateixa carpeta que el codi
#Vull que m'ho facis tenint en compte per poder ficar accentuacions i caracters especials
#i vull tambe que despres el XML no em generi errors
import csv
import xml.etree.ElementTree as ET
import re
import unicodedata
csv_file = 'Incidencies.csv'
xml_file = 'Incidencies.xml'
# Función para limpiar nombres de etiquetas XML
def limpiar_nombre_etiqueta(nombre):
    # Quita acentos
    nombre = ''.join(c for c in unicodedata.normalize('NFD', nombre)
                     if unicodedata.category(c) != 'Mn')
    # Reemplaza caracteres no alfanuméricos por guion bajo
    nombre = re.sub(r'\W+', '_', nombre.strip())
    # Asegura que no empiece con número
    if nombre and nombre[0].isdigit():
        nombre = '_' + nombre
    return nombre
# Función para indentar el XML
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# Crear raíz
root = ET.Element('Registros')
# Leer CSV y construir XML
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        registro = ET.SubElement(root, 'Registro')
        for key, value in row.items():
            campo_nombre = limpiar_nombre_etiqueta(key)
            campo = ET.SubElement(registro, campo_nombre)
            campo.text = value
# Indentar para que sea legible
indent(root)
# Guardar XML
tree = ET.ElementTree(root)
tree.write(xml_file, encoding='utf-8', xml_declaration=True)






