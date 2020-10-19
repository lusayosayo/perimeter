function probe_all_nodes() {
    var nodes = document.getElementsByClassName('node_wrapper');

    var i = 0;
    var l = nodes.length;
    
    for (; i < l; i++) {
        var node = nodes[i];

        var node_id = nodes[i].id.split('_')[1];
        probe_node(node_id);
    }
}

function probe_node(node_id) {
    var url = '/perimeter/daemon/infrastructure_monitoring/nodes/' + node_id + '/check_connectivity'
    $.ajax({
        url: url,
        success: function(response) {
            update_device_connectivity_state(node_id, response);
        },
        error: function(response) {
            //alert(response);
        }
    });
}

function update_device_connectivity_state(node_id, response) {
    var node_wrapper_id = 'node_' + node_id;
    var node_wrapper = document.getElementById(node_wrapper_id);
    
    var status = response['status'];
    var timestamp = response['timestamp'];

    var status_span = node_wrapper.getElementsByClassName('connection_status')[0];
    status_span.classList.remove('status_loading');

    status_span.onclick = function(event) {
        notify_with_popup("bottom", event.currentTarget, response["details"]);
    };

    switch(status) {
        case 'online': {
            status_span.classList.add('status_online');
            clearNode(status_span);
            
            var span = createStatusIndicators('online', timestamp);
            status_span.appendChild(span);
        } break;
        case 'offline': {
            status_span.classList.add('status_offline');
            clearNode(status_span);

            var span = createStatusIndicators('offline', timestamp);
            status_span.appendChild(span);
        } break;
        default: {
            alert('Could not parse status response.');
        }
    }
}

function clearNode(node) {
    while(node.childNodes.length != 0) {
        node.removeChild(node.childNodes[0]);
    }
}

function createStatusIndicators(status, timestamp) {
    var span = document.createElement('span');

    var indicator = document.createElement('span');
    
    var descriptor = document.createElement('span');
    var timestamp_descriptor = document.createElement('span');

    var descriptors = document.createElement('span');

    switch(status) {
        case 'online': {
            
            indicator.className = 'connection_status_indicator fa fa-check-circle';
            
            descriptor.className = 'connection_status_descriptor';
            descriptor.innerHTML = 'Online';

            timestamp_descriptor.innerHTML = timestamp;
        } break;
        case 'offline': {
            indicator.className = 'connection_status_indicator fa fa-times-circle';

            descriptor.className = 'connection_status_descriptor';
            descriptor.innerHTML = 'Offline';

            timestamp_descriptor.innerHTML = timestamp;
        }
    }

    descriptors.appendChild(descriptor);
    descriptors.appendChild(timestamp_descriptor);

    span.appendChild(indicator);
    span.appendChild(descriptors);

    return span;
}

function handleDeviceAction(action, id) {

    switch(action) {
        case 'view': {
            window.location.assign('/nodes/' + id);
        } break;
        case 'connect_def': {
            window.location.assign('/nodes/' + id);
        }
        case 'delete': {
            if (confirm("Are you sure you want to delete this node. There is no reversing this...")) {
                
                var form = createDeleteForm("/nodes/" + id);
                alert("deleting node: " + id);
                var hidden = document.getElementById("hidden");
                hidden.appendChild(form);
                form.submit();
            } else {
                //doNothing();
            }

        }
    }
}

function createDeleteForm(action) {
    var form = document.createElement("form");
    form.method = "POST";
    form.action = action;

    var method = document.createElement("input");
    method.name ="_method";
    method.type = "hidden";
    method.value ="DELETE";

    var token = document.createElement("input");
    token.name ="_token";
    token.type = "hidden";
    token.value = '{% csrf_token %}';

    form.appendChild(method);
    form.appendChild(token);
    
    return form;
}