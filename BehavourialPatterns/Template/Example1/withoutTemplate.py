class JsonParser:
    def openfile(self):
        print("Opening file...")
    def closefile(self):
        print("Closing file...")
    def parse(self, json_string):
        self.openfile()
        # Simulate parsing a JSON string
        print(f"Parsing JSON string: {json_string}")
        self.closefile()

class XmlParser:    
    def openfile(self):
        print("Opening file...")
    def closefile(self):
        print("Closing file...")
    def parse(self, xml_string):
        self.openfile()
        # Simulate parsing an XML string
        print(f"Parsing XML string: {xml_string}")
        self.closefile()

if __name__ == "__main__":
    json_parser = JsonParser()
    json_parser.parse('{"key": "value"}')
    
    xml_parser = XmlParser()
    xml_parser.parse("<key>value</key>")