/** 
 * AUTHOR: Lusayo Nyondo
 * VERSION: 0.1
 * DESCRIPTION:
 *  This script includes random utilities for examining the DOM.
 *
 *  It does not and should not include any code that can initiate execution of anything
 *  within this script.
 *
*/

//$(document).ready(function(){
// Only for debugging purposes.
//	onerror=function(a, b, c) {
//		alert(a + b + c);
//	};
//});

function follow_external_page(url) {
	window.location.assign(url);
}

function get_child_by_id(element, child_id) {
	var childNodes = element.childNodes;

	if (childNodes.length == 0) {
		return null;
	} else {
		var i = 0, l = childNodes.length;

		for(; i < l; i++) {
			var child_node = childNodes[i];

			if (child_node.id == child_id) {
				return child_node;
			} else {
				child_node = get_child_by_id(child_node, child_id);

				if (child_node == null) {
					continue;
				} else {
					return child_node;
				}
			}
		}
	}
}

function get_single_child_by_class_name(element, child_class) {
	var childNodes = element.childNodes;
	
	if (childNodes.length == 0) {
		return null;
	} else {
		var i = 0, l = childNodes.length;

		for(; i < l; i++) {
			var child_node = childNodes[i];

			if (child_node.classList &&
				child_node.classList.contains(child_class)) {
				return child_node;
			} else {
				child_node = get_single_child_by_class_name(child_node, child_class);

				if (child_node == null) {
					continue;
				} else {
					return child_node;
				}
			}
		}
	}
}
