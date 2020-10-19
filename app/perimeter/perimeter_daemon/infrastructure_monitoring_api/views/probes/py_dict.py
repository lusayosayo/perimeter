from datetime import datetime

from django.shortcuts import render

from perimeter.perimeter_utils import networking

from perimeter.perimeter_core.models.networks import Network
from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.nodes import Node, NodeInterface, NodeInterfaceIPAddress
from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping

from perimeter.perimeter_daemon.infrastructure_monitoring_api import cache

def network_probe(network_id, cache_results=True, check_nodes=False, check_services=False):
    network = Network.objects.get(
        id=network_id,
    )

    public_gateway = network.public_gateway
    local_gateway = network.local_gateway

    is_public_gateway_available, public_gateway_ping_output = networking.is_online(
        ip_address=public_gateway,
        timeout=6,
        attempts=5,
    )

    is_local_gateway_available, local_gateway_ping_output = networking.is_online(
        ip_address=local_gateway,
        timeout=6,
        attempts=5,
    )

    response = {
        
        'public_gateway_status': {
            'is_available': is_public_gateway_available,
            'status': 'online' if is_public_gateway_available else 'offline',
            'details': public_gateway_ping_output,
            'timestamp': datetime.utcnow(),
        },
        'local_gateway_status': {
            'is_available': is_local_gateway_available,
            'status': 'online' if is_local_gateway_available else 'offline',
            'details': local_gateway_ping_output,
            'timestamp': datetime.utcnow(),
        },
        'node_availability': []
    }

    if check_nodes:
        ip_addresses = network.get_valid_ip_addresses()
        
        if ip_addresses:
            pass

        node_interface_ip_addresses = NodeInterfaceIPAddress.objects.filter(
            ip_address__in=ip_addresses,
        )

        nodes = []

        for node_ip in node_interface_ip_addresses:
            node = node_ip.get_node()
            result = node_probe(node)

            response['node_availability'].append(result)

    return response

def cluster_probe(cluster_id, cache_results=True, check_services=False):
    cluster = Cluster.objects.get(
        id=cluster_id,
    )

    nodes = cluster.get_nodes()

    response = {
        'cluster': cluster.to_dict(),
        'timestamp': datetime.utcnow(),
        'node_availability': []
    }

    for node in nodes:
        response['node_availability'].append(
            node_probe(node.id, check_services)      
        )

    return response

def node_probe(node_id, cache_results=True, check_services=False):
    node = Node.objects.get(
        id=node_id
    )

    response = {
        'node': node.to_dict(),
        'timestamp': datetime.utcnow(),
        'interface_availability': []
    }

    interfaces = node.get_interfaces()

    for interface in interfaces:
        response['interface_availability'].append(
            interface_probe(interface.id, check_services)
        )

    cache.cache_node_availability(response, node)

    return response

def interface_probe(interface_id, cache_results=True, check_services=False):
    interface = NodeInterface.objects.get(
        id=interface_id,
    )

    response = {
        'interface': interface.to_dict(),
        'timestamp': datetime.utcnow(),
        'ip_address_availability': []
    }

    ip_addresses = interface.get_ip_addresses()

    for ip_address in ip_addresses:
        response['ip_address_availability'].append(
            ip_address_probe(
                ip_address.id,
                cache_results=cache_results,
                check_services=check_services
            )
        )

    return response

def ip_address_probe(ip_address_id, cache_results=True, check_services=False):
    ip_address_obj = NodeInterfaceIPAddress.objects.get(
        id=ip_address_id,
    )

    ip_address = ip_address_obj.to_dict()

    is_online, details = networking.is_online(
        ip_address,
        timeout=6,
        attempts=5
    )

    response = {
        'ip_address': ip_address,
        'is_available': is_online,
        'status': 'online' if is_online else 'offline',
        'details': details,
        'timestamp': datetime.utcnow(),
        'service_availability': [],
    }

    if check_services:
        services = ip_address.get_services()

        for service in services:
            response['service_availability'].append(
                service_probe(
                    service.id,
                    cache_results=cache_results
                )
            )

    return response

def service_probe(interface_service_mapping_id, cache_results=True,):
    pass

def check_connectivity(node_id):
    node = Node.objects.get(
        id=node_id,
    )

    ip_address = node.get_bindable_ip_address()

    is_online, details = networking.is_online(
        ip_address=ip_address,
    )

    if is_online:
        response = {
            'status': 'online',
            'summary': 'The node is online.',
            'details': 'The node has been successfully pinged.',
            'timestamp': datetime.utcnow(),
        }
    else:
        response = {
            'status': 'offline',
            'summary': 'The node is offline or unreadable.',
            'details': details,
            'timestamp': datetime.utcnow(),
        }

    return response
