from xml.etree import ElementTree as ET


from perimeter.perimeter_core.models.nodes import \
    Node, NodeInterface, \
    NodeInterfaceIPAddress
from perimeter.perimeter_core.data.xml.services import ServiceMappingXMLFormatter

class NodeInterfaceIPAddressXMLFormatter():
    def __init__(
        self,
        type=None,
        ip_address=None,
        subnet_mask=None,
        gateway=None
    ):
        """ Accepts:
                'type': The type of IP addressing scheme. Either IPV4 or IPV6.
                'ip_address': The actual IP address.
                'subnet_mask': The subnet mask underwhich to apply the IP address.
                'gateway': The gateway underwhich to apply the IP address.
        """
        self.type = type
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        self.gateway = gateway

        self.services= list()

    def load_model(self, model):
        assert isinstance(model, NodeInterfaceIPAddress)

        self.type = model.ip_address_type
        self.ip_address = model.ip_address
        self.subnet_mask = model.subnet_mask
        self.gateway = model.gateway

        self.services = list()
        services_models = model.get_services()

        for service_model in services_models:
            service = ServiceMappingXMLFormatter().load_model(service_model)
            services.append(service)

    def to_model(self, interface):
        model = NodeInterfaceIPAddress.objects.get_or_create(
            ip_address_type=self.type,
            ip_address=self.ip_address,
            subnet_mask=self.subnet_mask,
            gateway=self.gateway,
            node_interface=interface,
        )[0]

        return model

    def save_model(self, interface):
        model = self.to_model(interface=interface)
        model.node_interface = interface
        model.save()

        from perimeter.perimeter_core.models.services import Service

        for service_mapping in self.services:
            service_name = service_mapping.service
            
            service = Service.objects.get(
                name=service_name,    
            )

            name = service.name
            ip_address = model.ip_address
            
            service_mapping.save_model(
                ip_address=model,
                service=service,
            )


    def load_xml(self, xml):
        assert isinstance(xml, ET.Element)

        self.type = xml.attrib["type"]
        self.ip_address = xml.attrib["ip_address"]
        self.subnet_mask = xml.attrib["subnet_mask"]
        self.gateway = xml.attrib["gateway"]

        self.services = list()
        services_xmls = xml.findall("service")

        for service_xml in services_xmls:
            service = ServiceMappingXMLFormatter()
            service.load_xml(service_xml)
            self.services.append(service)

    def to_xml(self):
        xml = ET.Element('ip_address')

        xml.attrib["type"] = self.type
        xml.attrib["ip_address"] = self.ip_address
        xml.attrib["subnet_mask"] = self.subnet_mask
        xml.attrib["gateway"] = self.gateway

        for service in self.services:
            service_xml = service.to_xml()
            xml.append(service_xml)

        return xml

class NodeInterfaceXMLFormatter():
    def __init__(
        self,
        name=None,
        type=None,
        mac_address=None,
    ):
        
        self.name = name
        self.type = type
        self.mac_address = mac_address

        self.ip_addresses= list()

    def load_model(self, model):
        assert isinstance(model, NodeInterface)

        self.name = model.interface_name
        self.type = model.interface_type
        self.mac_address = model.mac_address

        self.ip_addresses = list()
        ip_addresses_models = model.get_ip_addresses()

        for ip_address_model in ip_addresses_models:
            ip_address = NodeInterfaceIPAddressXMLFormatter().load_model(ip_address_model)
            self.ip_addresses.append(ip_address)

    def to_model(self, node):
        model = NodeInterface.objects.get_or_create(
            interface_name=self.name,
            interface_type=self.type,
            mac_address=self.mac_address,
            node=node,
        )[0]

        return model

    def save_model(self, node):
        model = self.to_model(node=node)
        model.node = node
        model.save()

        for ip_address in self.ip_addresses:
            ip_address.save_model(
                interface=model,
            )

    def load_xml(self, xml):
        assert isinstance(xml, ET.Element)

        self.name = xml.attrib["name"]
        self.type = xml.attrib["type"]
        self.mac_address = xml.attrib["mac_address"]

        self.ip_addresses = list()
        ip_addresses_xmls = xml.findall('ip_address')

        for ip_address_xml in ip_addresses_xmls:
            ip_address = NodeInterfaceIPAddressXMLFormatter()
            ip_address.load_xml(ip_address_xml)
            self.ip_addresses.append(ip_address)

    def to_xml(self):
        xml = ET.Element(
            "interface",
            name=self.name,
            type=self.type,
            mac_address=self.mac_address,
        )

        for ip_address in self.ip_addresses:
            ip_address_xml = ip_address.to_xml()
            xml.append(ip_address_xml)

        return xml

class NodeXMLFormatter():
    def __init__(
        self,
        name=None,
        description=None
    ):
        """ Accepts:
                'name': The name of the node.
                'description': The description of the node.
        """
        

        self.name = name
        self.description = description
        self.interfaces= list()

    def to_model(self):
        """ Converts the NodeXMLFormatter object to an instance of the Node model.
        """
        node = Node.objects.get_or_create(
            name=self.name,
            description=self.description
        )[0]
        
        return node

    def load_model(self, model):
        """ Reads from the node model object specified and creates a corresponding object.
        """
        assert isinstance(model, NodeInterface)

        self.name = model.name
        self.description = model.description

        interfaces_models = model.get_interfaces()

        for interface_model in interfaces_models:
            interface = NodeInterfaceXMLFormatter().load_model(interface_model)
            interfaces_models.append(interface)

    def save_model(self, cluster):
        model = self.to_model()
        model.save()

        from perimeter.perimeter_core.models.nodes import NodeClusterMapping

        mapping = NodeClusterMapping(
            node=model,
            cluster=cluster,
        )

        mapping.save()

        for interface in self.interfaces:
            interface.save_model(
                node=model,
            )

    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        element = ET.Element("node")

        element.attrib['name'] = self.name
        element.attrib['description'] = self.description

        return element

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        assert isinstance(xml, ET.Element)

        self.name = xml.attrib["name"]
        self.description = xml.attrib["description"]

        self.interfaces = list()
        interfaces_xmls = xml.findall('interface')

        for interface_xml in interfaces_xmls:
            interface = NodeInterfaceXMLFormatter()
            interface.load_xml(interface_xml)
            self.interfaces.append(interface)

