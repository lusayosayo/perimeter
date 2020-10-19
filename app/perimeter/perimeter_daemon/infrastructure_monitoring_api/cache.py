""" This module will contain methods for caching infrastructure monitoring results.
    
    It is an integral feature for the dashboard.
"""

from perimeter.perimeter_daemon.infrastructure_monitoring_api.models import \
    ClusterAvailabilityCache, \
    NetworkAvailabilityCache, \
    NodeAvailabilityCache, \
    NodeInterfaceAvailabilityCache, \
    NodeInterfaceIPAddressAvailabilityCache, \
    NodeInterfaceIPAddressServiceAvailabilityCache

from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.networks import Network
from perimeter.perimeter_core.models.nodes import \
    Node, \
    NodeInterface, \
    NodeInterfaceIPAddress
from perimeter.perimeter_core.models.services import NodeInterfaceIPAddressServiceMapping

def cache_service_availability(ip_address_availability_cache, service_availability, node_interface_ip_address_service_mapping):
    service_availability_cache = NodeInterfaceServiceAvailabilityCache(
        ip_address_availability_cache=ip_address_availability_cache,
        node_interface_ip_address_service_mapping=node_interface_ip_address_service_mapping,
        status=service_availability['status'],
        description=service_availability['description'],
        timestamp=service_availability['timestamp']
    )

    service_availability_cache.save()

def cache_ip_address_availability(interface_availability_cache, ip_address_availability, ip_address):
    ip_address_availability_cache = NodeInterfaceIPAddressAvailabilityCache(
        interface_availability_cache=interface_availability_cache,
        ip_address=ip_address,
        status=ip_address_availability['status'],
        description=ip_address_availability['details'],
        timestamp=ip_address_availability['timestamp']
    )

    ip_address_availability_cache.save()

    for service_availability in ip_address_availability['service_availability']:
        service_mapping = NodeInterfaceIPAddressServiceMapping.objects.get(
            id=service_availability['id']
        )

        cache_service_availability(
            ip_address_availability_cache,
            service_availability,
            service_mapping
        )

def cache_interface_availability(node_availability_cache, interface_availability, node_interface):
    interface_availability_cache = NodeInterfaceAvailabilityCache(
        node_availability_cache=node_availability_cache,
        node_interface=node_interface,
        timestamp=interface_availability['timestamp']
    )

    interface_availability_cache.save()

    for ip_address_availability in interface_availability['ip_address_availability']:
        ip_address = NodeInterfaceIPAddress.objects.get(
            id=ip_address_availability['ip_address']['id']
        )

        cache_ip_address_availability(
            interface_availability_cache,
            ip_address_availability,
            ip_address
        )

def cache_node_availability(node_availability, node):
    node_availability_cache = NodeAvailabilityCache(
        node=node,
        timestamp=node_availability['timestamp']
    )

    node_availability_cache.save()

    for interface_availability in node_availability['interface_availability']:
        
        print(interface_availability)

        node_interface = NodeInterface.objects.get(
            id=interface_availability['interface']['id']
        )
        
        cache_interface_availability(
            node_availability_cache,
            interface_availability,
            node_interface
        )

def cache_cluster_availability(cluster_availability, cluster):
    cluster_availability_cache = ClusterAvailabilityCache(
        cluster=cluster,
        total_number_of_nodes=cluster_availability['total_number_of_nodes'],
        number_of_nodes_online=cluster_availability['number_of_nodes_online'],
        number_of_nodes_offline=cluster_availability['number_of_nodes_offline'],
        timestamp=cluster_availability['timestamp']
    )

    cluster_availability_cache.save()

    for node_availability in cluster_availability['node_availability']:
        node = Node.objects.get(
            id=node_availability['id']
        )

        cache_node_availability(node_availability, node)

def cache_network_availability(network_availability, network):
    network_availability_cache = NetworkAvailabilityCache(
        network=network,
        timestamp=network_availability['timestamp']
    )

    network_availability_cache.save()

    for node_availability in network_availability['node_availability']:
        node = Node.objects.get(
            id=node_availability['node']['id']
        )

        cache_node_availability(node_availability, node)
