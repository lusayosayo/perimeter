from django.shortcuts import loader
from django.http import HttpResponse

from perimeter.perimeter_core.models.networks import Network
from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.nodes import Node

def index(request):
    template = loader.get_template('perimeter_dashboard/reports/index.dtl.html')

    networks = Network.objects.all()
    clusters = Cluster.objects.all()
    nodes = Node.objects.all()

    context = {
        'networks': networks,
        'clusters': clusters,
        'nodes': nodes,
    }

    return HttpResponse(
        template.render(context, request)
    )


