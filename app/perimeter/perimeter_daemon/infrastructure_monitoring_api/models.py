from django.db import models

from perimeter.perimeter_core.models import networks, nodes, clusters, services

AVAILABILITY_CHOICES = [
    ('online', 'online'),
    ('offline', 'offline'),
    ('unknown', 'unknown')
]

class ClusterAvailabilityCache(models.Model):
    cluster = models.ForeignKey(
        clusters.Cluster,
        on_delete=models.CASCADE,
    )

    timestamp = models.DateTimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    total_number_of_nodes = models.IntegerField(
        default=0
    )
    
    number_of_nodes_online = models.IntegerField(
        default=0
    )

    number_of_nodes_offline = models.IntegerField(
        default=0
    )

class NetworkAvailabilityCache(models.Model):
    network = models.ForeignKey(
        networks.Network,
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )


class NodeAvailabilityCache(models.Model):
    node = models.ForeignKey(
        nodes.Node,
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

class NodeInterfaceAvailabilityCache(models.Model):
    node_interface = models.ForeignKey(
        nodes.NodeInterface,
        on_delete=models.CASCADE,
    )

    node_availability_cache = models.ForeignKey(
        NodeAvailabilityCache,
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

class NodeInterfaceIPAddressAvailabilityCache(models.Model):
    ip_address = models.ForeignKey(
        nodes.NodeInterfaceIPAddress,
        on_delete=models.CASCADE,
    )

    timestamp = models.DateTimeField()

    interface_availability_cache = models.ForeignKey(
        NodeInterfaceAvailabilityCache,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    status = models.CharField(
        default='unknown',
        max_length=10,
        choices=AVAILABILITY_CHOICES
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    details = models.TextField(
        blank=True,
        null=True
    )

class NodeInterfaceIPAddressServiceAvailabilityCache(models.Model):
    node_interface_ip_address_service_mapping = models.ForeignKey(
        services.NodeInterfaceIPAddressServiceMapping,
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    status = models.CharField(
        default='unknown',
        max_length=10,
        choices=AVAILABILITY_CHOICES
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    details = models.TextField(
        blank=True,
        null=True
    )
