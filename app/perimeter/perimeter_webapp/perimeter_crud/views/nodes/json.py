from datetime import datetime
from django.http import JsonResponse

from perimeter.perimeter_core.models.nodes import Node, NodeInterface, NodeInterfaceIPAddress
from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping

from perimeter.perimeter_core.controllers import nodes

from perimeter.perimeter_utils import networking

def map_node_interface_ip_address_to_service(request, node_id, node_interface_id, node_interface_ip_address_id, service_id):
    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=node_interface_ip_address_id,
    )

    service = Service.objects.get(
        id=service_id
    )

    try:
        parameters = {
            'node_interface_ip_address': node_interface_ip_address,
            'service': service
        }

        mapping = nodes.map_service_to_node_interface_ip_address(**parameters)

        if isinstance(mapping, NodeInterfaceIPAddressServiceMapping):
            response = {
                'status': 'success',
                'summary': 'The service has been mapped to the ip address successfully.',
                'description': '...'
            }
        else:
            response = {
                'status': 'failed',
                'summary': 'The service could not be mapped.',
                'description': '...'
            }
    except:
        response = {
            'status': 'failed',
            'summary': 'The service could not be mapped to the ip address instance.',
            'description': 'Let\'s think about this later...'
        }

        raise
    
    return JsonResponse(
        response,
        safe=False,
    )

def unmap_node_interface_ip_address_from_service(request, node_id, node_interface_id, node_interface_ip_address_id, service_id):
    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=node_interface_ip_address_id,
    )

    service = Service.objects.get(
        id=service_id
    )

    try:
        parameters = {
            'node_interface_ip_address': node_interface_ip_address,
            'service': service
        }

        mapping = nodes.unmap_service_from_node_interface_ip_address(**parameters)

        if isinstance(mapping, NodeInterfaceIPAddressServiceMapping):
            response = {
                'status': 'success',
                'summary': 'The service has been unmapped from the ip address successfully.',
                'description': '...'
            }
        else:
            response = {
                'status': 'failed',
                'summary': 'The service could not be unmapped.',
                'description': '...'
            }
    except:
        response = {
            'status': 'failed',
            'summary': 'The service could not be unmapped from the ip address instance.',
            'description': 'Let\'s think about this later...'
        }

        raise
    
    return JsonResponse(
        response,
        safe=False,
    )