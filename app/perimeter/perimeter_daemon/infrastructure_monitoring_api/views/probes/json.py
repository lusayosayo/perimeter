from datetime import datetime

from django.http import JsonResponse

from perimeter.perimeter_daemon.infrastructure_monitoring_api.views.probes import py_dict as api

def network_probe(request, network_id, check_nodes=False, check_services=False):
    return JsonResponse(
        api.network_probe(
            network_id=network_id,
            check_nodes=check_nodes,
            check_services=check_services
        ),
        safe=False
    )

def cluster_probe(request, cluster_id, check_services=False):
    response = api.cluster_probe(
        cluster_id=cluster_id,
        check_services=check_services,
    )
    
    return JsonResponse(
        response,
        safe=False,
    )

def node_probe(request, node_id, check_services=False):
    response = api.node_probe(
        node_id=node_id,
        check_services=check_services
    )
    return JsonResponse(
        response,
        safe=False,
    )

def interface_probe(request, interface_id, check_services=False):
    return JsonResponse(
        api.interface_probe(
            interface_id=interface_id,
            check_services=check_services
        ),
        safe=False,
    )

def ip_address_probe(request, ip_address_id, check_services=False):
    return JsonResponse(
        api.ip_address_probe(
            ip_address_id=ip_address_id,
            check_services=check_services
        ),
        safe=False
    )

def service_probe(request, interface_service_mapping_id):
    return JsonResponse(
        api.service_probe(
            interface_service_mapping_id=interface_service_mapping_id
        )
    )

def check_connectivity(request, node_id):
    return JsonResponse(
        api.check_connectivity(
            node_id=node_id,
        )
    )