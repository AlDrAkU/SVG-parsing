from infrabel_utils import SHARE_PATH_ICT511
from lxml.etree import tostring
from lxml import etree
from lxml.builder import E
from IPython.display import display, HTML
import os
display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))

def parse_svg(svg_file):
    parsedXML = etree.parse(os.path.join(SHARE_PATH_ICT511, 'gft2sap', 'crosscheck', 'test_svg',svg_file));a = etree.Element('root')
    for node in parsedXML.getroot():
        ids = node.attrib.get('id')

        if not ids is None:
            b = etree.SubElement(a,"parent")
        if not ids is None:
            z = etree.SubElement(b,'id_parent');z.text = ids
        for node_child in node:
            dd = node_child.attrib.get('d');ident = node_child.attrib.get('id');style = node_child.attrib.get('style');
            x = node_child.attrib.get('x');y = node_child.attrib.get('y')
            if not ident is None:
                c = etree.SubElement(b,'path')
            if not ident is None:    
                s = etree.SubElement(c,'id');s.text = ident
            if not dd is None:
                d = etree.SubElement(c,'d');d.text = dd
            if not style is None:
                e = etree.SubElement(c,'style');e.text = style
            if not x is None:
                f = etree.SubElement(c,'x');f.text = x
            if not y is None:
                g = etree.SubElement(c,'y');g.text = y

    et_string = etree.ElementTree(a)
    svg_file = svg_file.split('.')[0]
    file_name = svg_file+'_clean' + '.xml'
    destination = os.path.join(SHARE_PATH_ICT511, 'gft2sap', 'crosscheck', 'test_svg','extracted',file_name)
    et_string.write(destination, pretty_print=True,xml_declaration=True,   encoding="utf-8")

def check_extract():
    folder = [filename for filename in os.listdir(os.path.join(SHARE_PATH_ICT511, 'gft2sap', 'crosscheck', 'test_svg')) if os.path.isfile(os.path.join(SHARE_PATH_ICT511, 'gft2sap', 'crosscheck', 'test_svg', filename))]
    for filename in folder:
        if filename.endswith(".svg"):
            parse_svg(filename)
        else:
            continue
check_extract()