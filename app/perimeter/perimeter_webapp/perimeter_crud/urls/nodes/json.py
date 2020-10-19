from django.urls import path, include
from perimeter.perimeter_webapp.perimeter_crud.views.nodes import json as nodes

urlpatterns = [
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/<int:node_interface_ip_address_id>/services/<int:service_id>/map', nodes.map_node_interface_ip_address_to_service),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/<int:node_interface_ip_address_id>/services/<int:service_id>/unmap', nodes.unmap_node_interface_ip_address_from_service),
]