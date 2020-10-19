import json

from datetime import datetime
from django.http import JsonResponse

from perimeter.perimeter_core.controllers import clusters

from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.nodes import Node, NodeClusterMapping

def map_node_to_cluster(request, cluster_id, node_id):
    node = Node.objects.get(
        id=node_id,
    )

    cluster = Cluster.objects.get(
        id=cluster_id,
    )

    parameters = {
        'node': node,
        'cluster': cluster,
    }

    try:
        node_cluster_mapping = clusters.map_node_to_cluster(**parameters)

        response = {
            'status': 'success',
            'summary': 'No exceptions thrown.',
            'client_message': 'Node has been mapped successfully to cluster {}'.format(
                cluster.name
            ),
        }
    except:
        response = {
            'status': 'failed',
            'summary': 'Exception thrown',
            'client_message': 'Node has not been mapped to cluster {} because an exceptional condition has occurred.'.format(
                cluster.name
            ),
            'error_details': None,
        }

    return JsonResponse(response, safe=False)

def unmap_node_from_cluster(request, cluster_id, node_id):
    node = Node.objects.get(
        id=node_id,
    )

    cluster = Cluster.objects.get(
        id=cluster_id,
    )

    parameters = {
        'node': node,
        'cluster': cluster,
    }

    try:
        node_cluster_mapping = clusters.unmap_node_from_cluster(**parameters)
        
        response = {
            'status': 'success',
            'summary': 'No exceptions thrown.',
            'client_message': 'Node has been unmapped from cluster {}'.format(
                cluster.name
            ),
        }
    except:
        response = {
            'status': 'failed',
            'summary': 'Exception thrown',
            'client_message': 'Node has not been unmapped from cluster {} because an exceptional condition has occurred.'.format(
                cluster.name
            ),
            'error_details': None,
        }

    return JsonResponse(response, safe=False)