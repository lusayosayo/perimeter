from perimeter.perimeter_core.models.networks import Network

def create(
    name,
    description,
    public_gateway=None,
    local_gateway=None,
    network_provider=None,
    subnet_mask=None,
):
    network = Network.objects.get_or_create(
        name=name,
        description=description,
        public_gateway=public_gateway,
        local_gateway=local_gateway,
        network_provider=network_provider,
        subnet_mask=subnet_mask,
    )[0]

    return network

def modify(
    id,
    name=None,
    description=None,
    public_gateway=None,
    local_gateway=None,
    network_provider=None,
    subnet_mask=None,
):
    network = Network.objects.get(
        id=id,
    )

    network.name = name if name is not None else network.name
    network.description = description if description is not None else network.description
    network.local_gateway = local_gateway if local_gateway is not None else network.local_gateway
    network.public_gateway = public_gateway if public_gateway is not None else network.public_gateway
    network.network_provider = network_provider if network_provider is not None else network.network_provider
    network.subnet_mask = subnet_mask if subnet_mask is not None else network.subnet_mask

    network.save()
    
    return network

def delete(id):
    network = Network.objects.get(
        id=id,
    )

    response = network.delete()

    return network, response

def get(id):
    network = Network.objects.get(
        id=id,
    )

    return network
