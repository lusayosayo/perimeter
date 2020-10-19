from xml.etree import ElementTree as ET

from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping
from perimeter.perimeter_core.models.service_handlers import ServiceHandler

class ServiceXMLFormatter():
    def __init__(
        self,
        port=None,
        protocol=None,
        name=None,
        display_name=None,
        process=None,
        process_description=None,
        handler=None,
    ):
        # bookfi.net
        """ Accepts:
                'port': The port of the service.
                'protocol': The protocol running under the specified port.
                'process': The name of the process serving the protocol.
                'process_description: Any expository string about the process.
        """
        self.port = port
        self.protocol = protocol
        self.name = name
        self.display_name = display_name
        self.process = process
        self.process_description = process_description
        self.handler = handler

    def to_model(self, handler):
        """ Converts the ServiceXMLFormatter object to an instance of the Node model.
        """
        service = Service.objects.get_or_create(
            port=self.port,
            protocol=self.protocol,
            name=self.name,
            display_name=self.display_name,
            process=self.process,
            process_description=self.process_description,
            handler=handler,
        )[0]
        
        return service

    def load_model(self, service):
        """ Reads from the service model object specified and creates a corresponding object.
        """
        self.port = service.port
        self.protocol = service.protocol
        self.name  = service.name
        self.display_name = display_name
        self.process = service.process
        self.process_description = service.process_description
        self.handler = service.handler

    def save_model(self, ip_address=None):
        from perimeter.perimeter_core.models.services import NodeInterfaceIPAddressServiceMapping

        from perimeter.perimeter_core.models.service_handlers import ServiceHandler

        handler = ServiceHandler.objects.get(
            name=self.handler,
        )

        model = self.to_model(
            handler=handler,
        )

        model.save()

        if ip_address:
            assert isinstance(ip_address, NodeInterfaceIPAddress)

            mapping = NodeInterfaceIPAddressServiceMapping(
                service=model,
                node_interface_ip_address=ip_address,
            )

            mapping.save()
        
    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        xml = ET.Element(
            tag="service"
        )

        xml.attrib['port'] = self.port
        xml.attrib['protocol'] = self.protocol
        xml.attrib['name'] = self.name
        xml.attrib['display_name'] = self.display_name
        xml.attrib['process'] = self.process
        xml.attrib['process_description'] = self.process_description
        xml.attrib['handler'] = self.handler

        return xml

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        self.port = xml.attrib["port"]
        self.protocol = xml.attrib["protocol"]
        self.name = xml.attrib["name"]
        self.display_name = xml.attrib["display_name"]
        self.process = xml.attrib["process"]
        self.process_description = xml.attrib["process_description"]
        self.handler = xml.attrib["handler"]

class ServiceMappingXMLFormatter:
    def __init__(
        self,
        service=None,
        port=None,
    ):
        self.service = service
        self.port = port

    def load_model(self, model):
        self.service = model.service.name
        self.port = model.service.port
    
    def to_model(self, service, ip_address):
        from perimeter.perimeter_core.models.nodes import NodeInterfaceIPAddress
        assert isinstance(service, Service) and isinstance(ip_address, NodeInterfaceIPAddress)

        model = NodeInterfaceIPAddressServiceMapping.objects.get_or_create(
            service=service,
            node_interface_ip_address=ip_address,
            port=self.port,
        )[0]

        return model

    def load_xml(self, xml):
        assert isinstance(xml, ET.Element)

        self.port = xml.attrib["port"]
        self.service = xml.attrib["name"]

    def to_xml(self):
        xml = ET.Element('service')

        xml.attrib['port'] = self.port
        xml.attrib['name'] = self.service

        return xml

    def save_model(self, service, ip_address):
        model = self.to_model(service, ip_address)
        model.save()
