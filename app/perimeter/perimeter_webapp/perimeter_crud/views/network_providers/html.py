from django.shortcuts import loader, redirect
from django.http import HttpResponse

from perimeter.perimeter_core.models.network_providers import NetworkProvider, NetworkProviderContactMapping
from perimeter.perimeter_core.models.networks import Network
from perimeter.perimeter_core.models.contacts import Contact

from perimeter.perimeter_core.controllers import network_providers, networks

def index(request):
    template = loader.get_template('perimeter_crud/module_blocks/network_providers/index.dtl.html')

    network_providers = NetworkProvider.objects.all()

    context = {
        'network_providers': network_providers,
    }

    return HttpResponse(template.render(context, request))

def create(request):
    if request.POST.get('network_provider_street_address'):
        name = request.POST.get('network_provider_name')
        street_address = request.POST.get('network_provider_street_address')
        description = request.POST.get('network_provider_description')

        parameters = {
            'name':name,
            'street_address': street_address,
            'description': description,
        }

        network_provider = network_providers.create(**parameters)

        redirect_url = '/perimeter/network_providers/{}/show'.format(
            network_provider.id,
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/network_providers/create.dtl.html')
        context = {}

        return HttpResponse(template.render(context, request))

def edit(request, network_provider_id):
    network_provider = NetworkProvider.objects.get(
        id=network_provider_id,
    )

    network = Network.objects.filter(
        network_provider=network_provider,
    )

    if request.POST.get('network_provider_name'):
        name = request.POST.get('network_provider_name')
        street_address = request.POST.get('network_provider_street_address')
        description = request.POST.get('network_provider_description')

        parameters = {
            'id': network_provider.id,
            'name': name,
            'street_address': street_address,
            'description': description
        }

        network_provider = network_providers.modify(**parameters)

        return redirect('/perimeter/network_providers/{0}/show'.format(network_provider.id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/network_providers/edit.dtl.html')    
        
        network_provider = NetworkProvider.objects.get(
            id=network_provider_id,
        )

        networks = Network.objects.filter(
            network_provider=network_provider,
        )

        contact_mappings = NetworkProviderContactMapping.objects.filter(
            network_provider=network_provider,
        ).values('contact_id')
        
        contacts = Contact.objects.filter(
            id__in=contact_mappings,
        )

        context = {
            'network_provider': network_provider,
            'networks': networks,
            'contacts': contacts,
        }

        return HttpResponse(template.render(context, request))

def show(request, network_provider_id):
    template = loader.get_template('perimeter_crud/module_blocks/network_providers/show.dtl.html')
    
    network_provider = NetworkProvider.objects.get(
        id=network_provider_id,
    )

    networks = Network.objects.filter(
        network_provider=network_provider,
    )

    contact_mappings = NetworkProviderContactMapping.objects.filter(
        network_provider=network_provider,
    ).values('contact_id')
    
    contacts = Contact.objects.filter(
        id__in=contact_mappings,
    )

    context = {
        'network_provider': network_provider,
        'networks': networks,
        'contacts': contacts,
    }

    return HttpResponse(template.render(context, request))

def add_network(request, network_provider_id):
    if request.POST.get('name'):
        network_provider = NetworkProvider.objects.get(
            id=network_provider_id,
        )

        name = request.POST.get('name')
        description = request.POST.get('description')
        public_gateway = request.POST.get('public_gateway')
        local_gateway = request.POST.get('local_gateway')
        subnet_mask = request.POST.get('subnet_mask')

        parameters = {
            'network_provider': network_provider,
            'name': name,
            'description': description,
            'public_gateway': public_gateway,
            'local_gateway': local_gateway,
            'subnet_mask': subnet_mask,
        }

        network = networks.create(**parameters)

        return redirect('/perimeter/network_providers/{0}/show'.format(network_provider_id))
    
    else:
        template = loader.get_template('perimeter_crud/module_blocks/network_providers/networks/add.dtl.html')
        
        network_provider = NetworkProvider.objects.get(
            id=network_provider_id,
        )

        context = {
            'network_provider': network_provider,
        }

        return HttpResponse(template.render(context, request))

def edit_network(request, network_provider_id, network_id):
    if request.POST.get('name'):
        network_provider = NetworkProvider.objects.get(
            id=network_provider_id,
        )

        network = Network.objects.get(
            id=network_id,
        )

        name = request.POST.get('name')
        description = request.POST.get('description')
        public_gateway = request.POST.get('public_gateway')
        local_gateway = request.POST.get('local_gateway')
        subnet_mask = request.POST.get('subnet_mask')

        parameters = {
            'id': network.id,
            'network_provider': network_provider,
            'name': name,
            'description': description,
            'public_gateway': public_gateway,
            'local_gateway': local_gateway,
            'subnet_mask': subnet_mask,
        }

        network = networks.modify(**parameters)

        return redirect('/perimeter/network_providers/{0}/networks/{1}/show'.format(network_provider_id, network_id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/network_providers/networks/edit.dtl.html')
        
        network_provider = NetworkProvider.objects.get(
            id=network_provider_id,
        )

        network = Network.objects.get(
            id=network_id,
        )

        context = {
            'network_provider': network_provider,
            'network': network,
        }

        return HttpResponse(template.render(context, request))

def show_network(request, network_provider_id, network_id):
    template = loader.get_template('perimeter_crud/module_blocks/network_providers/networks/show.dtl.html')
    
    network_provider = NetworkProvider.objects.get(
        id=network_provider_id,
    )

    network = Network.objects.get(
        id=network_id,
    )

    context = {
        'network_provider': network_provider,
        'network': network,
    }

    return HttpResponse(template.render(context, request))

def add_contact_mapping(request, network_provider_id):
    template = loader.get_template('perimeter_crud/module_blocks/network_providers/contacts/add_mapping.dtl.html')
    
    network_provider = NetworkProvider.objects.get(
        id=network_provider_id
    )

    contact_mappings = NetworkProviderContactMapping.objects.filter(
        network_provider_id=network_provider.id
    ).values('contact_id')

    contacts = Contact.objects.exclude(
        id__in=contact_mappings,
    )

    mapped_contacts = Contact.objects.filter(
        id__in=contact_mappings,
    )

    context = {
        'network_provider': network_provider,
        'contacts': contacts,
        'mapped_contacts': mapped_contacts,
    }

    return HttpResponse(template.render(context, request))