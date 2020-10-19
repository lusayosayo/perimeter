from django.urls import path, include
from perimeter.perimeter_webapp.perimeter_crud.views.network_providers import json as network_providers

urlpatterns = [
    path(
        'network_providers/<int:network_provider_id>/contacts/<int:contact_id>/map',
        network_providers.map_contact_to_network_provider,
    ),
    path(
        'network_providers/<int:network_provider_id>/contacts/<int:contact_id>/unmap',
        network_providers.unmap_contact_from_network_provider,
    ),
]
