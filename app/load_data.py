#!/usr/bin/env python3

import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    from django import setup

    setup()

    test_handlers_xml_formatter()
    test_services_xml_formatter()
    build_vbs_nodes_cluster()
    test_cluster_xml_formatter()
    test_network_provider_xml_formatter()

def build_vbs_nodes_cluster():
    from perimeter.perimeter_core.data.xml.clusters import ClusterXMLFormatter
    from perimeter.modules.configurators import ptc

    import csv

    cluster_xml = ClusterXMLFormatter(
        name="VBS Servers",
        description="The servers for VBS."
    ).to_xml()

    node_list = csv.DictReader(open('data/SHOP_IPS.csv'))

    for node in ptc.build_nodes(node_list):
        cluster_xml.append(node)

    cluster = ClusterXMLFormatter()
    cluster.load_xml(cluster_xml)
    cluster.save_model()

def test_handlers_xml_formatter():
    from xml.etree import ElementTree as ET

    file = open('data/handlers/seed.xml')
    handlers = ET.ElementTree(file=file).getroot().findall('handler')

    from perimeter.perimeter_core.data.xml.service_handlers import ServiceHandlerXMLFormatter
    
    for handler in handlers:
        formatter = ServiceHandlerXMLFormatter()       
        formatter.load_xml(handler)
        formatter.save_model()

def test_services_xml_formatter():
    from xml.etree import ElementTree as ET

    file = open('data/services/seed.xml')
    services = ET.ElementTree(file=file).getroot().findall('service')

    from perimeter.perimeter_core.data.xml.services import ServiceXMLFormatter
    
    for service in services:
        formatter = ServiceXMLFormatter()       
        formatter.load_xml(service)
        formatter.save_model()

def test_cluster_xml_formatter():
    from xml.etree import ElementTree as ET

    file = open('data/clusters/seed.xml')
    cluster = ET.ElementTree(file=file).getroot()

    from perimeter.perimeter_core.data.xml.clusters import ClusterXMLFormatter

    formatter = ClusterXMLFormatter()

    formatter.load_xml(cluster)
    formatter.save_model()

def test_network_provider_xml_formatter():
    from xml.etree import ElementTree as ET

    file = open('data/environment/seed.xml')
    network_provider = ET.ElementTree(file=file).getroot()

    from perimeter.perimeter_core.data.xml.network_providers import NetworkProviderXMLFormatter

    formatter = NetworkProviderXMLFormatter()

    formatter.load_xml(network_provider)
    formatter.save_model()

main()