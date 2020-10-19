from django.urls import path, include
from perimeter.perimeter_webapp.perimeter_crud.views.clusters import json as clusters

urlpatterns = [
    path(
        'clusters/<int:cluster_id>/nodes/<int:node_id>/map',
        clusters.map_node_to_cluster,
    ),
    path(
        'clusters/<int:cluster_id>/nodes/<int:node_id>/unmap',
        clusters.unmap_node_from_cluster,
    ),
]
