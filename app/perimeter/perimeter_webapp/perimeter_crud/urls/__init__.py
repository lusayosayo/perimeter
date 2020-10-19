from django.urls import path, include

from .clusters.html import urlpatterns as clusters_html
from .clusters.json import urlpatterns as clusters_json

from .nodes.html import urlpatterns as nodes_html
from .nodes.json import urlpatterns as nodes_json

from .network_providers.html import urlpatterns as network_providers_html
from .network_providers.json import urlpatterns as network_providers_json

from .contacts.html import urlpatterns as contacts_html

urlpatterns = []

urlpatterns += clusters_html
urlpatterns += clusters_json

urlpatterns += nodes_html
urlpatterns += nodes_json

urlpatterns += network_providers_html
urlpatterns += network_providers_json

urlpatterns += contacts_html

