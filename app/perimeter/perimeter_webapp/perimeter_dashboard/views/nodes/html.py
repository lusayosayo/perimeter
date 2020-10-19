from django.shortcuts import loader
from django.http import HttpResponse

from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.nodes import Node

from perimeter.perimeter_core.models.network_providers import NetworkProvider
from perimeter.perimeter_core.models.networks import Network

def index(request):
    template = loader.get_template('perimeter_dashboard/module_blocks/nodes/index.dtl.html')

    clusters = Cluster.objects.all()
    nodes = Node.objects.all()

    network_providers = NetworkProvider.objects.all()
    networks = Network.objects.all()

    context = {
        'clusters': clusters,
        'nodes': nodes,
        'network_providers': network_providers,
        'networks': networks,
    }

    return HttpResponse(
        template.render(context, request)
    )