import socket

from datetime import datetime
from django.http import HttpResponse

from perimeter.perimeter_core.models.nodes import NodeInterfaceIPAddress
from perimeter.perimeter_core.models.services import NodeInterfaceIPAddressServiceMapping

def check_service(request, service_mapping_id):
    service_mapping = NodeInterfaceIPAddressServiceMapping.objects.get(
        id=service_mapping_id,
    )
    
    ip_address = service_mapping.node_interface_ip_address
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    parameters = [ ip_address.ip_address, service_mapping.port ]

    sock_response = sock.connect_ex((parameters))
    response = None

    if sock_response = 111:
        response = {
            'status': 'offline',
            'summary': 'Connection refused.'
            'description': 'The connection was refused.',
            'timestamp': datetime.utcnow()
        }
    elif sock_response = 0:
        response = {
            'status': 'online',
            'summary': 'Connection refused.',
            'description': 'The port is open and accessible.',
            'timestamp': datetime.utcnow(),
        }
    else:
        response = {
            'status': 'unknown',
            'summary': 'Connection refused.',
            'description': 'The port is open and accessible.',
            'timestamp': datetime.utcnow()
        }

    return JsonResponse(response, safe=False)