#!/usr/lib/python3.9
# -*-coding:utf-8 -*
"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte/

Trier des éléments XML par valeur d'attribut
https://tekipaki.hypotheses.org/2278
"""
import xml.etree.ElementTree as ET

input_path = "lexique_linguistique_japonais.xml"
output_path = "lexique_linguistique_japonais_TRI.xml"

with open(input_path, "r", encoding="utf-8") as input_file:
    tree = ET.parse(input_file)
    root = tree.getroot()

elements = root.findall("element")
elements_tries = sorted(elements, key=lambda element: int(element.attrib["id"]))
root[:] = elements_tries

xml_output = ET.tostring(root, encoding="utf-8", method="xml", xml_declaration=True).decode("utf-8")
with open(output_path, "w", encoding="utf-8", errors="replace", newline="") as target:
    target.write(xml_output)
