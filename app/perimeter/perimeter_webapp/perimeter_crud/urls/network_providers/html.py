from django.urls import path, include
from perimeter.perimeter_webapp.perimeter_crud.views.network_providers import html as network_providers

urlpatterns = [
    path('network_providers/', network_providers.index),
    path('network_providers/create', network_providers.create),
    path('network_providers/<int:network_provider_id>/edit', network_providers.edit),
    path('network_providers/index', network_providers.index),
    path('network_providers/<int:network_provider_id>/show', network_providers.show),

    path('network_providers/<int:network_provider_id>/networks/add', network_providers.add_network),
    path('network_providers/<int:network_provider_id>/networks/<int:network_id>/edit', network_providers.edit_network),
    path('network_providers/<int:network_provider_id>/networks/<int:network_id>/show', network_providers.show_network),

    path('network_providers/<int:network_provider_id>/contacts/add_mapping', network_providers.add_contact_mapping),
]
