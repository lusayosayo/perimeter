import socket
import platform
import subprocess

from datetime import datetime
from django.http import HttpResponse, JsonResponse

from perimeter.perimeter_core.models.nodes import NodeInterfaceIPAddress
from perimeter.perimeter_core.models.services import NodeInterfaceIPAddressServiceMapping

def ping(request, service_mapping_id):
    service_mapping = NodeInterfaceIPAddressServiceMapping.objects.get(
        id=service_mapping_id,
    )
    
    ip_address = service_mapping.node_interface_ip_address
    output = __ping(ip_address, 5, 4)

    if 'Reply from {ip_address}:'.format(ip_address=ip_address) in output:
        response = {
            'status': 'online',
            'summary': 'Connection accepted.',
            'description': 'The connection was refused.',
            'timestamp': datetime.utcnow()
        }

    else:
        response = {
            'status': 'offline',
            'summary': 'Connection refused.',
            'description': 'The port is open and accessible.',
            'timestamp': datetime.utcnow(),
        }

    return JsonResponse(response, safe=False)

def __ping(hostname, timeout, attempts):
    """ This method implements a platform independant ping.
    """
    if platform.system() == "Windows":
        command = "ping {0} -n {1} -w {2}".format(
            hostname,
            attempts,
            str(timeout*1000)
        )
    else:
        command = "ping -i {0} -c {1} {2}".format(
            str(timeout),
            attempts,
            hostname
        )

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = str(process.stdout.read())

    return output