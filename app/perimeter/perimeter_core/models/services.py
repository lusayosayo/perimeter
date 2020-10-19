from django.core import serializers
from django.db import models

from perimeter.perimeter_core.models.nodes import NodeInterfaceIPAddress
from perimeter.perimeter_core.models.service_handlers import ServiceHandler

MAX_PORTS = range(255 * 255)

POSSIBLE_PORTS = zip(MAX_PORTS, MAX_PORTS)
KNOWN_PROTOCOLS = [
    ('HTTP', 'HTTP'),
    ('POP3','POP3'),
    ('SNMP','SNMP'),
    ('SSH', 'SSH'),
    ('TELNET','TELNET'),
]


class Service(models.Model):
    port = models.IntegerField(
        choices=POSSIBLE_PORTS,
    )
    
    protocol = models.CharField(
        max_length=100,
        choices=KNOWN_PROTOCOLS,
    )

    name = models.CharField(
        max_length=100,
    )

    display_name = models.CharField(
        max_length=100,
    )

    process = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    process_description = models.TextField(
        null=True,
        blank=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    handler = models.ForeignKey(
        ServiceHandler,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return '{}:{}'.format(
            self.service_owner.__str__(),
            self.port.__str__(),
        )

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding
      
    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'port': self.port,
            'protocol': self.protocol,
            'name': self.name,
            'display_name': self.display_name,
            'process': self.process,
            'process_description': self.process_description,
            'handler': self.handler.to_dict(),
        }
    
class NodeInterfaceIPAddressServiceMapping(models.Model):
    node_interface_ip_address = models.ForeignKey(
        NodeInterfaceIPAddress,
        on_delete=models.CASCADE,
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    port = models.IntegerField(
        choices=POSSIBLE_PORTS,
        blank=True,
        null=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )
     
     
    def __str__(self):
        return '{} service on {}'.format(
            self.service.__str__(),
            self.node_interface_ip_address.__str__(),
        )

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding
      
    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'port': self.port,
            'ip_address': self.node_interface_ip_address.to_dict(),
            'service': self.service.to_dict(),
        }
    