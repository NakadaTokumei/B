from b.xmlabstract import * 
import xml.etree.ElementTree as ET

# get_file operation
import wget

class ExecuteProcess(XMLAbstract):

    def __init__(self, xmlET):
        super().__init__(xmlET)
        self.operation = None
        self.Url = None
        self.output = None

    def do_parse(self):
        # For <executeProcess></executeProcess>.
        root = self.root
        for child in root:
            print("tag in ExecuteProcess Section " + child.tag)
            
        pass

    def get_file(self):
        wget.download(self.Url, self.output)
        pass

class Group(XMLAbstract):
    def __init__(self, xmlET):
        super().__init__(xmlET)

    def do_parse(self):
        root = self.root
        for child in root:
            if child.tag == "executeProcess":
                ExecuteProcess(child).do_parse()

class Groups(XMLAbstract):
    def __init__(self, xmlET):
        super().__init__(xmlET)

    def do_parse(self):
        root = self.root
        print("Tag : " + root[1].tag)
        for child in root:
            # parse <Group></Group>
            if child.tag == "Group":
                Group(child).do_parse()
            else:
                print("This tag is not allowed. WTF " + child)
