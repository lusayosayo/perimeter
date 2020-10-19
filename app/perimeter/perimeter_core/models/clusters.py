from django.core import serializers
from django.db import models

class Cluster(models.Model):
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

    def __str__(self):
        return self.name.__str__()

    def get_nodes(self):
        from perimeter.perimeter_core.models.nodes import Node, NodeClusterMapping

        nodes = NodeClusterMapping.objects.filter(
            cluster=self,
        ).values('node_id')

        nodes = Node.objects.filter(
            id__in=nodes,
        )

        return nodes

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

