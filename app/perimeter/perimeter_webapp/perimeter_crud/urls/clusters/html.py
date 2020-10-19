from django.urls import path
from perimeter.perimeter_webapp.perimeter_crud.views.clusters import html as clusters

urlpatterns = [
    path('clusters/', clusters.index),
    path('clusters/create', clusters.create),
    path('clusters/<int:cluster_id>/edit', clusters.edit),
    path('clusters/index', clusters.index),
    path('clusters/<int:cluster_id>/show', clusters.show),

    path('clusters/<int:cluster_id>/nodes/add_mapping', clusters.add_node_cluster_mapping),
]
