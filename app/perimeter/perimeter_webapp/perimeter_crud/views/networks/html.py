from django.shortcuts import loader, render
from django.http import HttpResponse

from perimeter.perimeter_core.models import Network
from perimeter.perimeter_core.controllers import networks

def index(request):
    template = loader.get_template('perimeter_crud/module_blocks/networks/index.dtl.html')
    
    networks = Network.objects.all()
    
    context = {
        'networks': networks,
    }

    return HttpResponse(template.render(context, request))

def create(request):
    
    if request.POST.get('network_name'):
        parameters = {
            'name': request.POST.get('network_name'),
            'description': request.POST.get('network_description'),
            'gateway': request.POST.get()
        }

        cluster = clusters.create(**parameters)

        redirect_url = '/perimeter/clusters/{}/show'.format(
            cluster.id,
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/clusters/create.dtl.html')
        
        context = {}

        return HttpResponse(template.render(context, request))

def edit(request, cluster_id):
    if request.POST.get('cluster_name'):
        parameters = {
            'id': cluster_id,
            'name': request.POST.get('cluster_name'),
            'description': request.POST.get('cluster_description'),
        }

        cluster = clusters.modify(**parameters)

        redirection_url = '/perimeter/clusters/{}/show'.format(
            cluster.id,
        )
        
        return redirect(redirection_url)
    else:
        template = loader.get_template('perimeter_crud/module_blocks/clusters/edit.dtl.html')
        
        cluster = Cluster.objects.get(
            id=cluster_id,
        )

        node_cluster_mappings = NodeClusterMapping.objects.filter(
            cluster_id=cluster_id,
        ).values('node_id')
        
        nodes = Node.objects.filter(
            id__in=node_cluster_mappings,
        )

        context = {
            'cluster': cluster,
            'nodes': nodes,
        }

        return HttpResponse(template.render(context, request))

def show(request, cluster_id):
    template = loader.get_template('perimeter_crud/module_blocks/clusters/show.dtl.html')
    
    cluster = clusters.get(cluster_id)

    node_cluster_mappings = NodeClusterMapping.objects.filter(
        cluster_id=cluster_id,
    ).values('node_id')
    
    nodes = Node.objects.filter(
        id__in=node_cluster_mappings,
    )

    context = {
        'cluster': cluster,
        'nodes': nodes,
    }

    return HttpResponse(template.render(context, request))

def add_node_cluster_mapping(request, cluster_id):
    template = loader.get_template('perimeter_crud/module_blocks/clusters/nodes/add_mapping.dtl.html')
    
    cluster = clusters.get(cluster_id)

    nodes = Node.objects.all()

    node_cluster_mappings = NodeClusterMapping.objects.filter(
        cluster=cluster,
    ).values('node_id')

    mapped_nodes = Node.objects.filter(
        id__in=node_cluster_mappings,
    )

    context = {
        'cluster': cluster,
        'nodes': nodes,
        'mapped_nodes': mapped_nodes,
    }

    return HttpResponse(template.render(context, request))