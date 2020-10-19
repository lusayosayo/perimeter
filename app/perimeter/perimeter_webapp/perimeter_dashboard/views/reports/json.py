from django.http import JsonResponse

from perimeter.perimeter_core.models.networks import Network
from perimeter.perimeter_core.models.clusters import Cluster

from perimeter.perimeter_daemon.infrastructure_monitoring_api.views.probes import py_dict


def cluster_probe_summaries(request):
    clusters = Cluster.objects.all()

    cluster_summaries = list()

    for cluster in clusters:
        cluster_summaries.append(py_dict.cluster_probe(cluster.id, check_services=False))

    return JsonResponse(
        cluster_summaries,
        safe=False,
    )

def network_probe_summaries(request):
    networks = Network.objects.all()
    
    network_summaries = list()

    for network in networks:
        network_summaries.append(py_dict.network_probe(network.id, check_nodes=True))

    return JsonResponse(
        network_summaries,
        safe=False
    )

def probe_node(request, node_id):
    pass