from abc import ABC, abstractmethod
class Template(ABC):

    def parsedata(self, data):
        self.openfile()
        self.parse(data)
        self.closefile()

    def openfile(self):
        print("Opening file...")
    def closefile(self):
        print("Closing file...")

    @abstractmethod
    def parse(self, data):
        pass

class JsonParser(Template):

    def parse(self, json_string):
        # Simulate parsing a JSON string
        print(f"Parsing JSON string: {json_string}")

class XmlParser(Template):    
    
    def parse(self, xml_string):
        # Simulate parsing an XML string
        print(f"Parsing XML string: {xml_string}")

if __name__ == "__main__":
    json_parser = JsonParser()
    json_parser.parsedata('{"key": "value"}')
    
    xml_parser = XmlParser()
    xml_parser.parsedata("<key>value</key>")