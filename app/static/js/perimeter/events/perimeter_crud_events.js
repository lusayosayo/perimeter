/** 
 * AUTHOR: Lusayo Nyondo
 * VERSION: 0.1
 * DESCRIPTION:
 *  This script uses jquery to register events to DOM elements with particular attributes.
 * 
 *  Generally speaking, it focuses on generating URLs for
 *  api calls and page redirects, as well as orchestrating
 *  presentation changes by calling the relevant presentation
 *  functions which are defined in yet another script that focuses
 *  solely on presentation logic.
 * 
 *  It is an effort to minimize the scripting done for event handling by
 *  allowing the HTML elements themselves to define their own behavior
 *  and subscribe to events, providing the necessary information to properly
 *  construct the event.
 * 
 *  It couples pretty well with the DTL (Django Templating Language) to
 *  provide minimal, robust, clean code.
 * 
*/

function reload_previous_page() {
	var timestamp = $.now();
	var previous_page = document.referrer;

	var url = previous_page;

	location.assign(url);
}

$(document).ready(function() {
    $('[data-toggle="popover"]').popover();

    $('[data-action="create"]').on('click', function(event) {
        var src = event.currentTarget;
        var perimeter_module = src.getAttribute('data-module');

        var url = '/perimeter/' + perimeter_module + '/create';

        window.location.assign(url);
    });

    $('[data-action="show"]').on('click', function(event) {
        var src = event.currentTarget;
        var instance_id = src.getAttribute('data-instance-id');
        var perimeter_module = src.getAttribute('data-module');

        var url = '/perimeter/' + perimeter_module + '/' + instance_id + '/show';

        window.location.assign(url);
    });

    $('[data-action="edit"]').on('click', function(event) {
        var src = event.currentTarget;
        var instance_id = src.getAttribute('data-instance-id');
        var perimeter_module = src.getAttribute('data-module');

        var url = '/perimeter/' + perimeter_module + '/' + instance_id + '/edit';

        window.location.assign(url);
    });

    $('[data-action="add_child"]').on('click', function(event) {
        var src = event.currentTarget;
        
        var parent_module = src.getAttribute('data-parent-module');
        var parent_instance_id = src.getAttribute('data-parent-instance-id');
        var child_module = src.getAttribute('data-child-module');

        var url = '/perimeter/' + parent_module + '/' + parent_instance_id + '/' + child_module + '/add';

        window.location.assign(url);
    });

    $('[data-action="remove_child"]').on('click', function(event) {
        var src = event.currentTarget;

        var parent_module = src.getAttribute('data-parent-module');
        var parent_instance_id = src.getAttribute('data-parent-instance-id');
        var child_module = src.getAttribute('data-child-module');
        var child_instance_id = src.getAttribute('data-child-instance-id');

        var url = '/perimeter/' + parent_module + '/' + parent_instance_id + '/' + child_module + '/' + child_instance_id + '/remove';
    
        window.location.assign(url);
    });

    $('[data-action="edit_child"]').on('click', function(event) {
        var src = event.currentTarget;

        var parent_module = src.getAttribute('data-parent-module');
        var parent_instance_id = src.getAttribute('data-parent-instance-id');
        var child_module = src.getAttribute('data-child-module');
        var child_instance_id = src.getAttribute('data-child-instance-id');

        var url = '/perimeter/' + parent_module + '/' + parent_instance_id + '/' + child_module + '/' + child_instance_id +'/edit';
    
        window.location.assign(url);
    });

    $('[data-action="show_child"]').on('click', function(event) {
        var src = event.currentTarget;

        var parent_module = src.getAttribute('data-parent-module');
        var parent_instance_id = src.getAttribute('data-parent-instance-id');
        var child_module = src.getAttribute('data-child-module');
        var child_instance_id = src.getAttribute('data-child-instance-id');

        var url = '/perimeter/' + parent_module + '/' + parent_instance_id + '/' + child_module + '/' + child_instance_id +  '/show';
    
        window.location.assign(url);
    });

    $('[data-action="add_mapping"]').on('click', function(event) {
        var src = event.currentTarget;

        var parent_module = src.getAttribute('data-parent-module');
        var parent_instance_id = src.getAttribute('data-parent-instance-id');
        var child_module = src.getAttribute('data-child-module');

        var url = '/perimeter/' + parent_module + '/' + parent_instance_id + '/' + child_module + '/add_mapping';
    
        window.location.assign(url);
    });

    set_mapping_state = function(src) {
        var action = src.getAttribute('data-action');
        
        var mapping_state = action == 'map' ? 'unmapped' : action == 'unmap' ? 'mapped' : 'unknown';
        var alternative_state = mapping_state == 'mapped' ? 'unmapped': mapping_state == 'unmapped' ? 'mapped': 'unknown';

        var map_keyword = src.getAttribute('data-map-keyword');
        var unmap_keyword = src.getAttribute('data-unmap-keyword');
        
        var mapping_state_span = get_single_child_by_class_name(src, 'mapping_state');
        mapping_state_span.classList.add(mapping_state);
        mapping_state_span.classList.remove(alternative_state);

        if (mapping_state == "mapped") {
            mapping_state_span.innerHTML = unmap_keyword;
        } else if (mapping_state == "unmapped") {
            mapping_state_span.innerHTML = map_keyword;
        } else {
            mapping_state_span.innerHTML = "Map/Unmap";
        }
    };

    $('[data-action="unmap"],[data-action="map"]').each(function(index) {
        var src = this;
        set_mapping_state(src);
    });

    $('[data-action="unmap"],[data-action="map"]').on('click', function(event) {
        var src = event.currentTarget;

        var action = src.getAttribute('data-action');
        var parent_module = src.getAttribute('data-parent-module');
        var parent_instance_id = src.getAttribute('data-parent-instance-id');
        var child_module = src.getAttribute('data-child-module');
        var child_instance_id = src.getAttribute('data-child-instance-id');

        var url = '/perimeter/' +
                        parent_module + '/' +
                        parent_instance_id + '/' +
                        child_module + '/' +
                        child_instance_id + '/' +
                        action;
    
        var show_client_message = src.getAttribute('data-show-client-message');

        $.ajax({
            url: url,
            success: function(response) {
                if (action == "map") {
                    src.setAttribute('data-action', 'unmap');
                    set_mapping_state(src);
                } else if (action == "unmap") {
                    src.setAttribute('data-action', 'map');
                    set_mapping_state(src);
                }
                if (show_client_message == "show") {
                    notify_with_popup('bottom', src, response['client_message']);
                }
            },
            error: function(response) {
                notify_with_popup('bottom', src, response.status);
            }
        });
    });

    $('[data-action="delete"]').on('click', function(event) {
        var src = event.currentTarget;
        var instance_id = src.getAttribute('data-instance-id');
        var perimeter_module = src.getAttribute('data-module');

        var url = '/perimeter/' + perimeter_module + '/' + instance_id + '/delete';

        window.location.assign(url);
    });
});