from django.core import serializers
from django.db import models

from perimeter.perimeter_core.models.network_providers import NetworkProvider

class Network(models.Model):
    network_provider = models.ForeignKey(
        NetworkProvider,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=256,
    )

    description = models.TextField()

    public_gateway = models.GenericIPAddressField(
        blank=True,
        null=True,
    )

    local_gateway = models.GenericIPAddressField(
        blank=True,
        null=True,
    )

    subnet_mask = models.CharField(
        max_length=15,
        default="255.255.255.0",
    )

    def __str__(self):
        return '{} mask {} provided by {}. LAN {}'.format(
            self.public_gateway,
            self.subnet_mask,
            self.network_provider,
            self.local_gateway,
        )

    def get_valid_ip_addresses(self):
        prefix = '172.25.0.{0}'
        addresses = list()

        for i in range(1, 255):
            addresses.append(
                prefix.format(i)
            )
        return addresses

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding
    
    def to_dict(self):
       return {
            'id': self.id,
            'name': self.name,
            'description': description,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'public_gateway': self.public_gateway,
            'local_gateway': self.local_gateway,
            'subnet_mask': self.subnet_mask,
            'network_provider': self.network_provider.to_dict(),
        }
        