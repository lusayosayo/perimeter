from perimeter.perimeter_core.models.clusters import Cluster
from perimeter.perimeter_core.models.nodes import Node, NodeClusterMapping

def create(name, description):
    """ Creates a cluster with the mandatory fields name, and description.
        Accepts:
            'name': The name for the cluster.
            'description': The cluster's description.
        Returns a perimeter_core.models.cluster.Cluster object.
    """
    cluster = Cluster.objects.create(
        name=name,
        description=description,
    )

    return cluster

def modify(id, name=None, description=None):
    """ Modifies a cluster's name and description.
        Accepts:
            'id': The ID of the cluster object being modified.
            'name': The new name of the cluster object.
            'description': The new description of the cluster object.
        Returns a perimeter_core.models.Cluster object.
    """
    cluster = Cluster.objects.get(
        id=id,
    )

    cluster.name = name if name is not None else cluster.name
    cluster.description = description if description is not None else cluster.description

    cluster.save()

    return cluster

def delete(id):
    """ Deletes a cluster with a given Id.
        Accepts:
            'id': The cluster object's ID in the database.
        Returns:
            [ cluster, response ]
                'cluster': A perimeter_core.models.Cluster cluster object that has been removed from the database.
                'response': A boolean object that reports the success of the operation.
    """
    cluster = Cluster.objects.get(
        id=id,
    )

    response = cluster.delete()

    return cluster, response

def get(id):
    """ Fetches a particular cluster.
        Accepts:
            'id': A particular cluster object's id in the database.
        Returns:
            A perimeter_core.models.Cluster object.
    """
    cluster = Cluster.objects.get(
        id=id,
    )

    return cluster


def map_node_to_cluster(cluster, node):
    """ Maps a particular node to a particular cluster in the database.
        Accepts:
            'cluster': A perimeter_core.models.Cluster object.
            'node': A perimeter_core.models.Node object.
        Returns:
            A perimeter_core.models.NodeClusterMapping object.
    """
    
    assert isinstance(cluster, Cluster) and isinstance(node, Node)

    node_cluster_mapping = NodeClusterMapping.objects.get_or_create(
        node=node,
        cluster=cluster,
    )[0]

    return node_cluster_mapping

def unmap_node_from_cluster(cluster, node):
    """ Unmaps a particular node from a particular cluster and returns the mapping object.
        Accepts:
            'cluster': A perimeter_core.models.Cluster object.
            'node': A perimeter_core.models.Node object.
        Returns:
            A perimeter_core.models.NodeClusterMapping object.
    """

    assert isinstance(cluster, Cluster) and isinstance(node, Node)
    
    node_cluster_mapping = NodeClusterMapping.objects.get(
        node=node,
        cluster=cluster,
    )

    node_cluster_mapping.delete()

    return node_cluster_mapping
