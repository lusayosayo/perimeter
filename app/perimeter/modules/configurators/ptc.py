from xml.etree import ElementTree as ET

from perimeter.perimeter_core.data.xml.nodes import NodeXMLFormatter, NodeInterfaceXMLFormatter, NodeInterfaceIPAddressXMLFormatter
from perimeter.perimeter_core.data.xml.services import ServiceMappingXMLFormatter

def build_services():
    services = list()

    service = ServiceMappingXMLFormatter(
        service="ICMP ECHO",
        port="0"
    ).to_xml()

    services.append(service)

    service = ServiceMappingXMLFormatter(
        service="VBS BACKOFFICE",
        port="8080"
    ).to_xml()

    services.append(service)

    service = ServiceMappingXMLFormatter(
        service="SSH",
        port="22"
    ).to_xml()

    services.append(service)

    service = ServiceMappingXMLFormatter(
        service="DB2 DATABASE",
        port="51000"
    ).to_xml()

    services.append(service)

    return services

def build_ip_address(ip_address):
    ip_address = NodeInterfaceIPAddressXMLFormatter(
        type="IPV4",
        ip_address=ip_address,
        subnet_mask="255.255.255.0",
        gateway="172.25.0.1",
    ).to_xml()

    for service in build_services():
        ip_address.append(service)

    return ip_address

def build_interface(ip_address):
    interface = NodeInterfaceXMLFormatter(
        name='eth0',
        type='Ethernet',
        mac_address='00:00:00:00:00:00',
    ).to_xml()
    
    ip_address = build_ip_address(ip_address)

    interface.append(ip_address)

    return interface

def build_node(name, ip_address):
    node = NodeXMLFormatter(
        name=name,
        description="VBS Backoffice Server for {0}".format(name)
    ).to_xml()

    interface = build_interface(ip_address)

    node.append(interface)

    return node

def build_nodes(node_list):
    nodes = list()

    for node_item in node_list:
        node = build_node(
            node_item["SHOP NAME"],
            node_item["IP ADDRESS"],
        )

        nodes.append(node)

    return nodes

