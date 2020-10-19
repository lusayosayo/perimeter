from xml.etree import ElementTree as ET

from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.data.xml.nodes import NodeXMLFormatter

class ClusterXMLFormatter():
    def __init__(
        self,
        name=None,
        description=None
    ):
        """ Accepts:
                'name': The name of the cluster.
                'description': The description of the cluster.
        """
        self.name = name
        self.description = description
        self.nodes = list()

    def to_model(self):
        """ Converts the ClusterXMLFormatter object to an instance of the Cluster model.
        """
        cluster = Cluster.objects.get_or_create(
            name=self.name,
            description=self.description
        )[0]
        
        return cluster

    def load_model(self, cluster):
        """ Reads from the cluster model object specified and creates a corresponding object.
        """
        self.name = cluster.name
        self.description = cluster.description

        nodes_models = cluster.get_nodes()

        self.nodes = list()

        for node in nodes_models:
            node_xml = NodeXMLFormatter(node)
            self.nodes.append(node_xml)

    def save_model(self):
        model = self.to_model()
        model.save()

        nodes = self.nodes
        for node in nodes:
            node.save_model(cluster=model)

    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        xml = ET.Element("cluster")

        xml.attrib['name'] = self.name
        xml.attrib['description'] = self.description

        for node in self.nodes:
            node_xml = node.to_xml()
            xml.append(node_xml)

        return xml

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        self.name = xml.attrib["name"]
        self.description = xml.attrib["description"]

        self.nodes = list()
        nodes_xmls = xml.findall('node')

        for node_xml in nodes_xmls:
            node = NodeXMLFormatter()
            node.load_xml(node_xml)

            self.nodes.append(node)


