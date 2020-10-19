from django.test import TestCase
# Create your tests here.
from perimeter.perimeter_core.models.nodes import Node
from perimeter.perimeter_core.controllers import nodes

class ContactCRUDTestCase(TestCase):

    node = None

    def setUp(self):
        global node

        try:
            parameters = {
                'name': 'Victoria Avenue VBS Server',
                'description': 'VBS Server at Victoria Avenue Spar.',
            }
            
            node = nodes.create(parameters)
        except:
            pass

        self.assertIsNotNone(node)

    def test_test_modify_node(self):
        global node
        response = None
        
        try:
            parameters = {
                'id': node.id,
                'name': 'Chitawira',
                'description': 'Chitawira VBS Server'
            }

            response = nodes.modify(parameters)

        except:
            pass

        self.assertIsNotNone(response)

  from perimeter.perimeter_core.models.nodes import Node, NodeInterface, NodeInterfaceIPAddress, NodeClusterMapping

def test_create(parameters):
    name = parameters['name']
    description = parameters['description']

    node = Node.objects.create(
        name=name,
        description=description,
    )

    return node

def test_modify(parameters):
    id = parameters['id']

    node = Node.objects.get(
        id=id,
    )

    name = parameters['name']
    description = parameters['description']

    node.name = name
    node.description = description

    return node

def test_delete(parameters):
    id = parameters['id']

    node = Node.objects.get(
        id=id,
    )

    response = node.delete()

    return node, response

def test_get(parameters):
    id = parameters['id']

    node = Node.objects.get(
        id=id,
    )

    return node

def test_add_node_interface(parameters):
    node = parameters['node']

    interface_type = parameters['interface_type']
    interface_name = parameters['interface_name']
    mac_address = parameters['mac_address']

    node_interface = NodeInterface.objects.create(
        interface_name=interface_name,
        interface_type=interface_type,
        mac_address=mac_address,
    )

    return node_interface

def test_modify_node_interface(parameters):
    id = parameters['id']

    node_interface = NodeInterface.objects.get(
        id=id,
    )

    interface_type = parameters['interface_type']
    interface_name = parameters['interface_name']
    mac_address = parameters['mac_address']

    node_interface.interface_type = interface_type
    node_interface.interface_name = interface_name
    node_interface.mac_address = mac_address

    node_interface.save()

    return node_interface

def test_remove_node_interface(parameters):
    id = parameters['id']

    node_interface = NodeInterface.objects.get(
        id=id,
    )

    node_interface.remove()

    return node_interface

def test_add_node_interface_ip_address(parameters):
    node_interface = parameters['node_interface']
    
    network = parameters['network']
    gateway = parameters['gateway']
    ip_address_type = parameters['ip_address_type']
    ip_address = parameters['ip_address']

    node_interface_ip_address = NodeInterfaceIPAddress.objects.create(
        node_interface=node_interface,
        network=network,
        gateway=gateway,
        ip_address_type=ip_address_type,
        ip_address=ip_address,
    )

    return node_interface_ip_address

def test_modify_node_interface_ip_address(parameters):
    id = parameters['id']

    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=id,
    )

    network = parameters['network']
    gateway = parameters['gateway']
    ip_address_type = parameters['ip_address_type']
    ip_address = parameters['ip_address']

    node_interface_ip_address.network = network
    node_interface_ip_address.gateway = gateway
    node_interface_ip_address.ip_address_type = ip_address_type
    node_interface_ip_address.ip_address = ip_address

    node_interface_ip_address.save()

    return node_interface_ip_address

def test_remove_node_interface_ip_address(parameters):
    id = parameters['id']

    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=id,
    )

    node_interface_ip_address.remove()

    return node_interface_ip_address

def test_map_node_to_cluster(parameters):
    cluster = parameters['cluster']
    node = parameters['node']

    node_cluster_mapping = NodeClusterMapping.objects.create(
        node=node,
        cluster=cluster,
    )

    return node_cluster_mapping

def test_unmap_node_from_cluster(parameters):
    cluster = parameters['cluster']
    node = parameters['node']

    node_cluster_mapping = NodeClusterMapping.objects.get(
        node=node,
        cluster=cluster,
    )

    node_cluster_mapping.remove()

    return node_cluster_mapping
