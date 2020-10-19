from django.shortcuts import loader, redirect
from django.http import HttpResponse
from django.db.models import F

from perimeter.perimeter_core.controllers import nodes

from perimeter.perimeter_core.models.nodes import Node, \
    NodeInterface, INTERFACE_TYPES, \
    NodeInterfaceIPAddress, IP_ADDRESS_TYPES, \
    NodeClusterMapping

from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.network_providers import NetworkProvider
from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping

def index(request):
    template = loader.get_template('perimeter_crud/module_blocks/nodes/index.dtl.html')
    
    nodes = Node.objects.all()
    network_providers = NetworkProvider.objects.all()
    clusters = Cluster.objects.all()
    
    context = {
        'nodes': nodes,
    }

    return HttpResponse(template.render(context, request))

def create(request):
    if request.POST.get('node_name'):
        name = request.POST.get('node_name')
        description = request.POST.get('node_description')

        parameters = {
            'name': name,
            'description': description,
        }

        node = nodes.create(**parameters)

        redirection_url = '/perimeter/nodes/{}/show'.format(
            node.id,
        )
        
        return redirect(redirection_url)

    else:
        template = loader.get_template('perimeter_crud/module_blocks/nodes/create.dtl.html')
        context = {}

        return HttpResponse(template.render(context, request))

def edit(request, node_id):
    if request.POST.get('node_name'):
        return HttpResponse('save changes')
    else:
        node = Node.objects.get(
            id=node_id,
        )

        node_interfaces = NodeInterface.objects.filter(
            node=node,
        )

        clusters = Cluster.objects.all()

        context = {
            'node': node,
            'clusters': clusters,
            'node_interfaces': node_interfaces,
        }

        template = loader.get_template('perimeter_crud/module_blocks/nodes/edit.dtl.html')
        
        return HttpResponse(template.render(context, request))

def show(request, node_id):
    template = loader.get_template('perimeter_crud/module_blocks/nodes/show.dtl.html')
    
    node = Node.objects.get(
        id=node_id,
    )
    
    node_interfaces = NodeInterface.objects.filter(
        node=node,
    )

    clusters = Cluster.objects.all()

    context = {
        'node': node,
        'clusters': clusters,
        'node_interfaces': node_interfaces,
    }

    return HttpResponse(template.render(context, request))

def delete(request):
    pass

def add_node_interface(request, node_id):
    node = Node.objects.get(
        id=node_id,
    )

    if request.POST.get('interface_name'):
        interface_name = request.POST.get('interface_name')
        interface_type = request.POST.get('interface_type')
        mac_address = request.POST.get('mac_address')

        parameters = {
            'node': node,
            'interface_name': interface_name,
            'interface_type': interface_type,
            'mac_address': mac_address,
        }

        node_interface = nodes.add_node_interface(**parameters)

        redirect_url = '/perimeter/nodes/{}/edit'.format(
            node.id,
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/add.dtl.html')
        
        existing_interfaces = NodeInterface.objects.filter(
            node=node,
        )

        interface_count = len(existing_interfaces)
        
        autogen_name = 'eth{}'.format(
            interface_count,
        )

        autogen = {
            'name': autogen_name,
        }
        
        interface_types = INTERFACE_TYPES
        
        context = {
            'node': node,
            'interface_types': interface_types,
            'autogen': autogen,
        }

        return HttpResponse(template.render(context, request))

def show_node_interface(request, node_id, node_interface_id):
    node = Node.objects.get(
        id=node_id,
    )

    interfaces = NodeInterface.objects.filter(
        node=node,
    )

    node_interface = interfaces.get(
        id=node_interface_id,
    )
    
    template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/show.dtl.html')
        
    ip_addresses = NodeInterfaceIPAddress.objects.filter(
        node_interface=node_interface,
    )

    interface_types = INTERFACE_TYPES
    
    context = {
        'node': node,
        'node_interface': node_interface,
        'interface_types': interface_types,
        'node_interface_ip_addresses': ip_addresses,
    }

    return HttpResponse(template.render(context, request))

def edit_node_interface(request, node_id, node_interface_id):      
    node = Node.objects.get(
        id=node_id,
    )

    interfaces = NodeInterface.objects.filter(
        node=node,
    )

    node_interface = interfaces.get(
        id=node_interface_id,
    )

    if request.POST.get('interface_name'):
        interface_name = request.POST.get('interface_name')
        interface_type = request.POST.get('interface_type')
        mac_address = request.POST.get('mac_address')

        parameters = {
            'id': node_interface_id,
            'interface_name': interface_name,
            'interface_type': interface_type,
            'mac_address': mac_address,
        }

        node_interface = nodes.modify_node_interface(**parameters)

        redirect_url = '/perimeter/nodes/{}/interfaces/{}/edit'.format(
            node.id,
            node_interface.id,
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/edit.dtl.html')
        
        ip_addresses = NodeInterfaceIPAddress.objects.filter(
            node_interface=node_interface,
        )

        interface_types = INTERFACE_TYPES
        
        context = {
            'node': node,
            'node_interface': node_interface,
            'interface_types': interface_types,
            'node_interface_ip_addresses': ip_addresses,
        }

        return HttpResponse(template.render(context, request))

def remove_node_interface(request, node_id, node_interface_id):
    node = Node.objects.get(
        id=node_id,
    )

    node_interfaces = NodeInterface.objects.filter(
        node=node,
    )

    node_interface = node_interfaces.get(
        id=node_interface_id,
    )

    parameters = {
        'id': node_interface.id,
    }

    node_interface, response = nodes.remove_node_interface(**parameters)

    redirect_url = '/perimeter/nodes/{}/edit'.format(
        node.id,
    )

    return redirect(redirect_url)

def add_node_interface_ip_address(request, node_id, node_interface_id):
    node = Node.objects.get(
        id=node_id,
    )

    node_interface = NodeInterface.objects.get(
        id=node_interface_id,
    )

    if request.POST.get('ip_address'):
        ip_address = request.POST.get('ip_address')
        ip_address_type = request.POST.get('ip_address_type')
        subnet_mask = request.POST.get('subnet_mask')
        gateway = request.POST.get('gateway')
    
        parameters = {
            'node_interface': node_interface,
            'ip_address_type': ip_address_type,
            'ip_address': ip_address,
            'subnet_mask': subnet_mask,
            'gateway': gateway
        }

        node_interface_ip_address = nodes.add_node_interface_ip_address(**parameters)

        redirect_url = '/perimeter/nodes/{}/node_interfaces/{}/show'.format(
            node.id,
            node_interface.id,
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/ip_addresses/add.dtl.html')
        
        ip_address_types = IP_ADDRESS_TYPES
        
        context = {
            'node': node,
            'node_interface': node_interface,
            'ip_address_types': ip_address_types,
        }

        return HttpResponse(template.render(context, request))

def edit_node_interface_ip_address(request, node_id, node_interface_id, node_interface_ip_address_id):
    node = Node.objects.get(
        id=node_id,
    )

    node_interface = NodeInterface.objects.get(
        id=node_interface_id,
    )

    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=node_interface_ip_address_id,
    )

    service_mappings = NodeInterfaceIPAddressServiceMapping.objects.filter(
        node_interface_ip_address=node_interface_ip_address,
    ).values("service_id")

    services = Service.objects.filter(id__in=service_mappings)
    services.annotate(mapped_port=F('port'))
    
    for service in services:
        service.mapped_port=NodeInterfaceIPAddressServiceMapping.objects.get(service_id=service.id).port

    if request.POST.get('ip_address'):
        ip_address = request.POST.get('ip_address')
        ip_address_type = request.POST.get('ip_address_type')
        subnet_mask = request.POST.get('subnet_mask')
        gateway = request.POST.get('gateway')

        parameters = {
            'id': node_interface_ip_address.id,
            'node_interface': node_interface,
            'ip_address_type': ip_address_type,
            'ip_address': ip_address,
            'subnet_mask': subnet_mask,
            'gateway': gateway
        }

        node_interface_ip_address = nodes.modify_node_interface_ip_address(**parameters)

        redirect_url = '/perimeter/nodes/{}/node_interfaces/{}/show'.format(
            node.id,
            node_interface.id,
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/ip_addresses/edit.dtl.html')
        
        ip_address_types = IP_ADDRESS_TYPES
        
        context = {
            'node': node,
            'node_interface': node_interface,
            'ip_address_types': ip_address_types,
            'ip_address': node_interface_ip_address,
            'services': services,
        }

        return HttpResponse(template.render(context, request))

def show_node_interface_ip_address(request, node_id, node_interface_id, node_interface_ip_address_id):
    node = Node.objects.get(
        id=node_id,
    )

    node_interface = NodeInterface.objects.get(
        id=node_interface_id,
    )

    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=node_interface_ip_address_id,
    )

    service_mappings = NodeInterfaceIPAddressServiceMapping.objects.filter(
        node_interface_ip_address=node_interface_ip_address,
    ).values("service_id")

    services = Service.objects.filter(id__in=service_mappings)
    services.annotate(mapped_port=F('port'))
    
    for service in services:
        service.mapped_port=NodeInterfaceIPAddressServiceMapping.objects.get(service_id=service.id).port

    
    template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/ip_addresses/show.dtl.html')
        
    ip_address_types = IP_ADDRESS_TYPES
    
    context = {
        'node': node,
        'node_interface': node_interface,
        'ip_address_types': ip_address_types,
        'ip_address': node_interface_ip_address,
        'services': services,
    }

    return HttpResponse(template.render(context, request))

def remove_node_interface_ip_address(request, node_id, node_interface_id, node_interface_ip_address_id):
    id = node_interface_ip_address_id

    node = Node.objects.get(
        id=node_id,
    )

    node_interface = NodeInterface.objects.get(
        id=node_interface_id,
    )

    parameters = {
        'id': id,
    }

    success = nodes.remove_node_interface_ip_address(**parameters)

    redirect_url = '/perimeter/nodes/{}/node_interfaces/{}/show'.format(
        node.id,
        node_interface.id,
    )

    return redirect(redirect_url)

def add_node_interface_ip_address_service_mapping(request, node_id, node_interface_id, node_interface_ip_address_id):
    node = Node.objects.get(
        id=node_id,
    )

    node_interface = NodeInterface.objects.get(
        id=node_interface_id,
    )

    node_interface_ip_address = NodeInterfaceIPAddress.objects.get(
        id=node_interface_ip_address_id,
    )

    service_mappings = NodeInterfaceIPAddressServiceMapping.objects.filter(
        node_interface_ip_address=node_interface_ip_address,
    ).values('service_id')

    services = Service.objects.exclude(
        id__in=service_mappings,
    )

    mapped_services = Service.objects.filter(
        id__in=service_mappings,
    )

    template = loader.get_template('perimeter_crud/module_blocks/nodes/interfaces/ip_addresses/services/add_mapping.dtl.html')
         
    context = {
        'node': node,
        'node_interface': node_interface,
        'ip_address': node_interface_ip_address,
        'services': services,
        'mapped_services': mapped_services,
    }

    return HttpResponse(template.render(context, request))

def edit_node_interface_ip_address_service(request, node_id, node_interface_id, node_interface_ip_address_id, node_interface_ip_address_service_id):
    pass

def delete_node_interface_ip_address_service(request, node_id, node_interface_id, node_interface_ip_address_id, node_interface_ip_address_service_id):
    pass
