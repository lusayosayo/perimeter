from perimeter.perimeter_core.models.network_providers import NetworkProvider, NetworkProviderContactMapping
from perimeter.perimeter_core.models.contacts import Contact

def create(name, description, street_address=None):
    network_provider = NetworkProvider.objects.get_or_create(
        name=name,
        description=description,
    )[0]

    return network_provider

def modify(id, name=None, description=None, street_address=None): 
    network_provider = NetworkProvider.objects.get(
        id=id
    )

    network_provider.name = name if name is not None else network_provider.name
    network_provider.street_address = street_address if street_address is not None else network_provider.street_address
    network_provider.description = description if description is not None else network_provider.description

    network_provider.save()

    return network_provider

def delete(id):
    network_provider = NetworkProvider.objects.get(
        id=id
    )

    response = network_provider.delete()

    return network_provider, response

def get(id):
    network_provider = NetworkProvider.objects.get(
        id=id
    )

    return network_provider

def map_contact_to_network_provider(network_provider, contact):
    assert isinstance(network_provider, NetworkProvider) and isinstance(contact, Contact)

    contact_entry = NetworkProviderContactMapping.objects.create(
        network_provider=network_provider,
        contact=contact,
    )

    return contact_entry

def unmap_contact_from_network_provider(network_provider, contact):
    assert isinstance(network_provider, NetworkProvider) and isinstance(contact, Contact)
    
    contact_entry = NetworkProviderContactMapping.objects.get(
        network_provider=network_provider,
        contact=contact,
    )

    contact_entry.delete()

    return contact_entry

def get_network_provider_contacts(network_provider):
    assert isinstance(network_provider, NetworkProvider)

    contact_entries = NetworkProviderContactMapping.objects.filter(
        network_provider=network_provider,
    ).values('contact')

    contacts = NetworkProviderContactMapping.objects.filter(
        id__in=contact_entries,
    )

    return contacts
