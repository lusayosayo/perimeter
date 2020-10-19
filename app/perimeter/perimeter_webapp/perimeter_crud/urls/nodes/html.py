from django.urls import path, include
from perimeter.perimeter_webapp.perimeter_crud.views.nodes import html as nodes

urlpatterns = [
    path('nodes/', nodes.index),
    path('nodes/create', nodes.create),
    path('nodes/<int:node_id>/edit', nodes.edit),
    path('nodes/index', nodes.index),
    path('nodes/<int:node_id>/show', nodes.show),
    
    path('nodes/<int:node_id>/node_interfaces/add', nodes.add_node_interface),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/edit', nodes.edit_node_interface),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/remove', nodes.remove_node_interface),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/show', nodes.show_node_interface),

    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/add', nodes.add_node_interface_ip_address),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/<int:node_interface_ip_address_id>/edit', nodes.edit_node_interface_ip_address),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/<int:node_interface_ip_address_id>/remove', nodes.remove_node_interface_ip_address),
    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/<int:node_interface_ip_address_id>/show', nodes.show_node_interface_ip_address),

    path('nodes/<int:node_id>/node_interfaces/<int:node_interface_id>/ip_addresses/<int:node_interface_ip_address_id>/services/add_mapping', nodes.add_node_interface_ip_address_service_mapping),
]