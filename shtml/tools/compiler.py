import xml.etree.ElementTree as ET
import lxml.html.clean as clean
import os
import codecs
import HTMLParser


class Compiler():
    def __init__(self):
        self.parser =HTMLParser.HTMLParser()
    def compile(self, file):

        full_path = os.path.dirname(os.path.realpath(file))


        tree = ET.parse(file)
        doc = tree.getroot()
        matches = doc.findall('.//div')

        for element in matches:
            if element.get('content') is not None:
                with codecs.open(full_path + '/' + element.get('content')) as f:
                    element.text = f.read()
                    f.close()

        with codecs.open(full_path + '/' + os.path.basename(file).replace('.shtml', '.html'), mode='wb+') as f:
            txt = self.parser.unescape(ET.tostring(doc))
            f.write(txt)
            f.close()

        