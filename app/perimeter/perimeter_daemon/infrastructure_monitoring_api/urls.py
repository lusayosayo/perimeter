from django.urls import path

from .views.probes import json as api
from .views.probes import cacher

urlpatterns = [
    path('nodes/<int:node_id>/check_connectivity', api.check_connectivity),
    path('clusters/<int:cluster_id>/cluster_probe', api.cluster_probe),
    path('networks/<int:network_id>/network_probe', api.network_probe),
    path('nodes/<int:node_id>/node_probe', api.node_probe),
    path('nodes/<int:node_id>/services/<int:service_id>/service_probe', api.service_probe),

    path('networks/<int:network_id>/cache_network_availability', cacher.cache_network_availability)
]