from django.core import serializers
from django.db import models

from perimeter.perimeter_core.models.contacts import Contact

class NetworkProvider(models.Model):
    name = models.CharField(
        max_length=256,
    )

    street_address = models.TextField()
    
    description = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.network_provider_name.__str__()

    def get_contacts(self):
        from perimeter.perimeter_core.models.contacts import Contact

        contact_ids = NetworkProviderContactMapping.objects.filter(
            contact=self,
        ).values('contact_id')

        contacts = Contact.objects.filter(
            id__in=contact_ids,
        )

        return contacts

    def get_networks(self):
        from perimeter.perimeter_core.models.networks import Network
        
        networks = Network.objects.get(
            network_provider=self,
        )

        return networks

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'name': self.name,
            'street_address': self.street_address,
            'description': self.description,
        }

class NetworkProviderContactMapping(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )

    network_provider = models.ForeignKey(
        NetworkProvider,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        contact = self.contact.name.__str__()
        network_provider = self.network_provider.name.__str__()

        return '{} at {}'.format(contact, network_provider)

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding
    
    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'contact': self.conctact.to_dict(),
            'network_provider': self.network_provider.to_dict(),
        }
