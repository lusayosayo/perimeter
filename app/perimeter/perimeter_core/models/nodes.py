from django.core import serializers
from django.db import models

from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.networks import Network

IPV4_ADDRESS_TYPE = 'IPV4'
IPV6_ADDRESS_TYPE = 'IPV6'

IP_ADDRESS_TYPES = [
    IPV4_ADDRESS_TYPE,
    IPV6_ADDRESS_TYPE,
]

IP_ADDRESS_TYPES_CHOICES = zip(IP_ADDRESS_TYPES, IP_ADDRESS_TYPES)

WIFI_INTERFACE_TYPE = 'WIFI'
ETHERNET_INTERFACE_TYPE = 'ETHERNET'

INTERFACE_TYPES = [
    ETHERNET_INTERFACE_TYPE,
    WIFI_INTERFACE_TYPE,
]

INTERFACE_TYPES_CHOICES = zip(INTERFACE_TYPES, INTERFACE_TYPES)

class Node(models.Model):
    name = models.CharField(
        max_length=256,
    )

    description = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def get_default_ip_address(self):
        interfaces = NodeInterface.objects.filter(
            node=self,
        )

        for interface in interfaces:
            interface_addresses = NodeInterfaceIPAddress.objects.filter(
                node_interface=interface,
            )

            for ip_address in interface_addresses:
                if ip_address.is_default == True:
                    return ip_address

        return None

    def get_bindable_ip_address(self):
        ip_address = self.get_default_ip_address()

        if ip_address == None:
            node_interfaces = NodeInterface.objects.filter(
                node=self,
            )

            ip_addresses = NodeInterfaceIPAddress.objects.filter(
                node_interface__in=node_interfaces,
            )

            if len(ip_addresses) > 0:
                ip_address = ip_addresses[0].ip_address

        return ip_address

    def __str__(self):
        return self.name.__str__()

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def get_interfaces(self):
        interfaces = NodeInterface.objects.filter(
            node=self,
        )

        return interfaces

    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'name': self.name,
            'description': self.description,
        }

class NodeClusterMapping(models.Model):
    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
    )

    cluster = models.ForeignKey(
        Cluster,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        node = self.node.name.__str__()
        cluster = self.cluster.name.__str__()

        return '{} in {}'.format(node, cluster)

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'node': self.node.to_dict(),
            'cluster': self.cluster.to_dict(),
        }

class NodeInterface(models.Model):
    global INTERFACE_TYPES_CHOICES

    node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
    )

    interface_type = models.CharField(
        max_length=12,
        choices=INTERFACE_TYPES_CHOICES,
        default=ETHERNET_INTERFACE_TYPE,
    )

    interface_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    mac_address = models.CharField(
        max_length=18,
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
        return '{} interface {} at {} on device {}'.format(
            self.interface_type.__str__(),
            self.interface_name.__str__(),
            self.mac_address.__str__(),
            self.node.__str__(),
        )
    
    def get_bound_ip_address(self):
        pass
    
    def get_ip_addresses(self):
        ip_addresses = NodeInterfaceIPAddress.objects.filter(
            node_interface=self,
        )

        return ip_addresses

    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'interface_type': self.interface_type,
            'interface_name': self.interface_name,
            'mac_address': self.mac_address,
        }

class NodeInterfaceIPAddress(models.Model):
    global IPV4_ADDRESS_TYPE
    global IPV6_ADDRESS_TYPE

    global IP_ADDRESS_TYPES_CHOICES

    node_interface = models.ForeignKey(
        NodeInterface,
        on_delete=models.CASCADE,
    )

    subnet_mask = models.GenericIPAddressField(
        default='255.255.255.0'
    )

    gateway = models.GenericIPAddressField()

    ip_address_type = models.CharField(
        max_length=4,
        choices=IP_ADDRESS_TYPES_CHOICES,
        default=IPV4_ADDRESS_TYPE,
    )

    ip_address = models.GenericIPAddressField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.ip_address.__str__()

    def get_services(self):
        # When the class is first loaded, the services module is still unavailable,
        # thus we import it as it is being used to make sure it's there when we need it.
        
        from perimeter.perimeter_core.models.services import Service, NodeInterfaceIPAddressServiceMapping

        services = NodeInterfaceIPAddressServiceMapping.objects.filter(
            node_interface=self,
        ).values('service_id')

        services = Service.objects.filter(
            id__in=services,
        )

        return services

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'ip_address_type': self.ip_address_type,
            'ip_address': self.ip_address,
            'subnet_mask': self.subnet_mask,
            'gateway': self.gateway,
            'node_interface': self.node_interface.to_dict(),
        }