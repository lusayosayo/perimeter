from django.http import JsonResponse

from perimeter.perimeter_core.models import networks, nodes

from perimeter.perimeter_daemon.infrastructure_monitoring_api import cache
from perimeter.perimeter_daemon.infrastructure_monitoring_api.views.probes import json as api

def cache_network_availability(request, network_id):
    network_availability = api.network_probe(
        request,
        network_id
    )

    cache.cache_network_availability(
        network_availability,
        networks.Network.objects.get(
            id=network_availability['network']['id']
        )
    )

    return JsonResponse(
        network_availability,
        safe=False
    )

def cache_node_availability(request, node_id):
    node_availability = api.node_probe(
        request,
        node_id
    )

    cache.cache_node_availability(
        node_availability,
        nodes.Node.object.get(
            id=node_availability['id']
        )
    )

    return JsonResponse(
        node_availability,
        safe=False
    )