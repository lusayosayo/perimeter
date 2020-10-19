from xml.etree import ElementTree as ET

from perimeter.perimeter_core.models.service_handlers import ServiceHandler

class ServiceHandlerXMLFormatter():
    def __init__(
        self,
        name=None,
        description=None,
        app_name=None,
    ):
        """ Accepts:
                'name': The name of the handler.
                'description': The description of the handler.
        """
        self.name = name
        self.description = description
        self.app_name = app_name

    def to_model(self):
        """ Converts the ClusterXMLFormatter object to an instance of the Cluster model.
        """
        handler = ServiceHandler.objects.get_or_create(
            name=self.name,
            description=self.description,
            app_name=self.app_name,
        )[0]
        
        return handler

    def load_model(self, handler):
        """ Reads from the handler model object specified and creates a corresponding object.
        """
        self.name = handler.name
        self.app_name = handler.app_name
        self.description = handler.description

    def save_model(self):
        model = self.to_model()
        model.save()

    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        xml = ET.Element("handler")

        xml.attrib['name'] = self.name
        xml.attrib['description'] = self.description
        xml.attrib['app_name'] = self.app_name

        return xml

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        self.name = xml.attrib["name"]
        self.description = xml.attrib["description"]
        self.app_name = xml.attrib["app_name"]

