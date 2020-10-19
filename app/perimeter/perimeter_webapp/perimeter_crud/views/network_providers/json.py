import json

from datetime import datetime
from django.http import JsonResponse

from perimeter.perimeter_core.controllers import network_providers

from perimeter.perimeter_core.models.network_providers import NetworkProvider, NetworkProviderContactMapping
from perimeter.perimeter_core.models.contacts import Contact

def map_contact_to_network_provider(request, network_provider_id, contact_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    network_provider = NetworkProvider.objects.get(
        id=network_provider_id,
    )

    parameters = {
        'contact': contact,
        'network_provider': network_provider,
    }

    try:
        contact_network_provider_mapping = network_providers.map_contact_to_network_provider(**parameters)

        response = {
            'status': 'success',
            'summary': 'No exceptions thrown.',
            'client_message': 'Contact has been mapped successfully to network provider {0}'.format(
                network_provider.name
            ),
        }
    except:
        response = {
            'status': 'failed',
            'summary': 'Exception thrown',
            'client_message': 'Contact has not been mapped to network provider {0} because an exceptional condition has occurred.'.format(
                network_provider.name
            ),
            'error_details': None,
        }

    return JsonResponse(response, safe=False)

def unmap_contact_from_network_provider(request, network_provider_id, contact_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    network_provider = NetworkProvider.objects.get(
        id=network_provider_id,
    )

    parameters = {
        'contact': contact,
        'network_provider': network_provider,
    }

    try:
        contact_network_provider_mapping = network_providers.unmap_contact_from_network_provider(**parameters)
        
        response = {
            'status': 'success',
            'summary': 'No exceptions thrown.',
            'client_message': 'Contact has been unmapped from network provider {0}'.format(
                network_provider.name
            ),
        }
    except:
        response = {
            'status': 'failed',
            'summary': 'Exception thrown',
            'client_message': 'Contact has not been unmapped from network provider {0} because an exceptional condition has occurred.'.format(
                network_provider.name
            ),
            'error_details': None,
        }

    return JsonResponse(response, safe=False)