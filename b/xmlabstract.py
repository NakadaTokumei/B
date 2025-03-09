import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

class XMLAbstract(ABC):
    @abstractmethod
    def __init__(self, xmlET : ET.Element):
        self.root = xmlET
        pass

    @abstractmethod
    def do_parse(self):
        # Nothing Here Now.
        pass