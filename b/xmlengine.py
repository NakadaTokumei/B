from b.xmlabstract import * 
from b.groups.group import *

class XMLEngine:
    def __init__(self, fileName = ""):
        self.xmlET = ET.parse(fileName)
        self.root = self.xmlET.getroot()
        pass

    def check_root_xml_tag(self):
        if self.root.tag == "B":
            return True
        else:
            return False        

    def do_parse(self):
        if not self.check_root_xml_tag():
            print("It's wrong tag name now")

        root = self.root
        for child in root:
            print("Tag is " + child.tag)
            if child.tag == "Groups":
                Groups(child).do_parse()
        pass