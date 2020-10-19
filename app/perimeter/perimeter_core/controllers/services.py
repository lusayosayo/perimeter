from perimeter.perimeter_core.models.nodes import NodeInterfaceIPAddress
from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping

def create(
    port,
    protocol,
    process=None,
    description=None
):

    service = Service.objects.create(
        port=port,
        protocol=protocol,
        process=process,
        description=description,
    )

    return service

def modify(
    id,
    port=None,
    protocol=None,
    process=None,
    description=None,
):
    service = Service.objects.get(
        id=id,
    )

    service.port = port if port is not None else service.port
    service.protocol = protocol if protocol is not None else service.protocol
    service.process = process if process is not None else service.process
    service.description = description if description is not None else service.description

    service.save()

    return service

def delete(id):
    service = Service.objects.get(
        id=id,
    )

    response = service.delete()

    return service, response

def get(id):
    service = Service.objects.get(
        id=id,
    )

    return service
    