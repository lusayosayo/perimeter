from perimeter.perimeter_core.models.nodes import Node, NodeInterface, NodeInterfaceIPAddress, NodeClusterMapping
from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping

def create(name, description):
    node = Node.objects.create(
        name=name,
        description=description,
    )

    return node

def modify(id, name, description):
    node = Node.objects.get(
        id=id,
    )

    node.name = name if name is not None else node.name
    node.description = description if description is not None else node.description

    return node

def delete(id):
    node = Node.objects.get(
        id=id,
    )

    response = node.delete()

    return node, response

def get(id):
    node = Node.objects.get(
        id=id,
    )

    return node

def add_node_interface(node, interface_type, interface_name, mac_address):
    assert isinstance(node, Node)

    node_interface = NodeInterface.objects.get_or_create(
        node=node,
        interface_name=interface_name,
        interface_type=interface_type,
        mac_address=mac_address,
    )

    return node_interface

def modify_node_interface(
    id,
    interface_type=None,
    interface_name=None,
    mac_address=None
):
    node_interface = NodeInterface.objects.get(
        id=id,
    )

    node_interface.interface_type = interface_type if interface_type is not None else node_interface.interface_type
    node_interface.interface_name = interface_name if interface_name is not None else node_interface.interface_name
    node_interface.mac_address = mac_address if mac_address is not None else node_interface.mac_address

    node_interface.save()

    return node_interface

def remove_node_interface(id):
    assert isinstance(node, Node)

    node_interface = node_interfaces.get(
        id=id,
    )

    node_interface.delete()

    return node_interface

def add_node_interface_ip_address(
    node_interface,
    gateway,
    ip_address,
    subnet_mask,
    ip_address_type="IPV4"
):
    assert isinstance(node_interface, NodeInterface)

    node_interface_ip_address = NodeInterfaceIPAddress.objects.create(
        node_interface=node_interface,
        gateway=gateway,
        subnet_mask=subnet_mask,
        ip_address_type=ip_address_type,
        ip_address=ip_address,
    )

    return node_interface_ip_address

def modify_node_interface_ip_address(
    id,
    node_interface=None,
    subnet_mask=None,
    gateway=None,
    ip_address=None,
    ip_address_type=None,
):
    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=id,
    )

    node_interface_ip_address.node_interface = node_interface if node_interface else node_interface_ip_address.node_interface
    node_interface_ip_address.gateway = gateway if gateway else node_interface_ip_address.gateway
    node_interface_ip_address.subnet_mask = subnet_mask if subnet_mask else node_interface_ip_address.subnet_mask
    node_interface_ip_address.ip_address_type = ip_address_type if ip_address_type else node_interface_ip_address.ip_address_type
    node_interface_ip_address.ip_address = ip_address if ip_address else node_interface_ip_address.ip_address

    node_interface_ip_address.save()

    return node_interface_ip_address

def remove_node_interface_ip_address(id):
    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=id,
    )

    node_interface_ip_address.delete()

    return node_interface_ip_address

def map_service_to_node_interface_ip_address(service, node_interface_ip_address):
    assert isinstance(service, Service) and isinstance(node_interface_ip_address, NodeInterfaceIPAddress)

    service_address_mapping = NodeInterfaceIPAddressServiceMapping.objects.get_or_create(
        service=service,
        node_interface_ip_address=node_interface_ip_address,
    )

    return service_address_mapping

def unmap_service_from_node_interface_ip_address(service, node_interface_ip_address):
    assert isinstance(service, Service) and isinstance(node_interface_ip_address, NodeInterfaceIPAddress)

    service_address_mapping = NodeInterfaceIPAddressServiceMapping.objects.get(
        service=service,
        node_interface_ip_address=node_interface_ip_address,
    )

    service_address_mapping.delete()

    return service_address_mapping
