from xml.etree import ElementTree as ET

from perimeter.perimeter_core.models.networks import Network

class NetworkXMLFormatter():
    def __init__(
        self,
        name=None,
        description=None,
        subnet_mask=None,
        public_gateway=None,
        local_gateway=None,
    ):
        """ Accepts:
                'name': The name of the network.
                'description': The description of the network.
        """
        self.name = name
        self.description = description
        self.subnet_mask = subnet_mask
        self.public_gateway = public_gateway
        self.local_gateway = local_gateway

    def to_model(self, network_provider):
        """ Converts the NetworkXMLFormatter object to an instance of the Network model.
        """
        network = Network.objects.get_or_create(
            name=self.name,
            description=self.description,
            subnet_mask=self.subnet_mask,
            public_gateway=self.public_gateway,
            local_gateway=self.local_gateway,
            network_provider=network_provider,
        )[0]
        
        return network

    def load_model(self, network):
        """ Reads from the network model object specified and creates a corresponding object.
        """
        self.name = network.name
        self.description = network.description
        self.subnet_mask = network.subnet_mask
        self.public_gateway = network.public_gateway
        self.local_gateway = network.local_gateway

    def save_model(self, network_provider):
        model = self.to_model(network_provider=network_provider)
        model.save()

    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        xml = ET.Element("network")

        xml.attrib['name'] = self.name
        xml.attrib['description'] = self.description
        xml.attrib['subnet_mask'] = self.subnet_mask
        xml.attrib['public_gateway'] = self.public_gateway
        xml.attrib['local_gateway'] = self.local_gateway
        
        return xml

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        self.name = xml.attrib["name"]
        self.description = xml.attrib["description"]
        self.subnet_mask = xml.attrib["subnet_mask"]
        self.public_gateway = xml.attrib["public_gateway"]
        self.local_gateway = xml.attrib["local_gateway"]
