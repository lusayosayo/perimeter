from xml.etree import ElementTree as ET

from perimeter.perimeter_core.models.network_providers import NetworkProvider

from perimeter.perimeter_core.data.xml.networks import NetworkXMLFormatter
from perimeter.perimeter_core.data.xml.contacts import ContactXMLFormatter

class NetworkProviderXMLFormatter():
    def __init__(
        self,
        name=None,
        description=None,
        street_address=None,
    ):
        """ Accepts:
                'name': The name of the network_provider.
                'description': The description of the network_provider.
        """
        self.name = name
        self.description = description
        self.street_address = street_address

        self.contacts= list()
        self.networks= list()

    def to_model(self):
        """ Converts the NetworkXMLFormatter object to an instance of the Network model.
        """
        network_provider = NetworkProvider.objects.get_or_create(
            name=self.name,
            description=self.description,
            street_address=self.street_address,
        )[0]
        
        return network_provider

    def load_model(self, network_provider):
        """ Reads from the network_provider model object specified and creates a corresponding object.
        """
        self.name = network_provider.name
        self.description = network_provider.description
        self.street_address = network_provider.street_address

        contacts_models = network_provider.get_contacts()

        self.contacts = list()

        for contact_model in self.contacts_models:
            contact = ContactXMLFormatter(contact_model)
            self.contacts.append(contact)

        networks_models = network_provider.get_networks()

        self.networks = list()

        for network in networks_models:
            network_xml = NetworkXMLFormatter(network)
            self.networks.append(network_xml)

    def save_model(self):
        model = self.to_model()
        model.save()

        contacts = self.contacts

        for contact in contacts:
            contact.save_model(network_provider=model)

        networks = self.networks
        
        for network in networks:
            network.save_model(network_provider=model)

    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        xml = ET.Element("network_provider")

        xml.attrib['name'] = self.name
        xml.attrib['description'] = self.description
        xml.attrib['street_address'] = self.street_address

        for contact in self.contacts:
            contact_xml = contact.to_xml()
            xml.append(contact_xml)

        for network in self.networks:
            network_xml = network.to_xml()
            xml.append(network_xml)

        return xml

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        self.name = xml.attrib["name"]
        self.description = xml.attrib["description"]
        self.street_address = xml.attrib["street_address"]

        self.contacts = list()
        contacts_xmls = xml.find('contacts').findall('contact')
        
        for contact_xml in contacts_xmls:
            contact = ContactXMLFormatter()
            contact.load_xml(contact_xml)

            self.contacts.append(contact)

        self.networks = list()
        networks_xmls = xml.find('networks').findall('network')

        for network_xml in networks_xmls:
            network = NetworkXMLFormatter()
            network.load_xml(network_xml)

            self.networks.append(network)
