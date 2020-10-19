/** 
 * AUTHOR: Lusayo Nyondo
 * VERSION: 0.1
 * DESCRIPTION:
 *  This script strictly defines functions that are used to create DOM elements.
 *
 *  It does not and should not include any code that can initiate execution of anything
 *  within this script.
 * 
*/
function create_dismissible_popup(message, dismissal_text, dismiss_function) {
    var popover_content = document.createElement("div");
    popover_content.className = "d-flex flex-column align-content-center align-items-center justify-content-center justify-items-center";
    
    var message_span = document.createElement("span");
    message_span.className = "w-100 text-center d-block";
    message_span.innerHTML = message;

    var dismiss_button = document.createElement("button");
    dismiss_button.className = "btn btn-outline-dark text-dark";

    var dismiss_button_text = document.createElement("span");
    dismiss_button_text.innerHTML = "&nbsp;&nbsp;" + dismissal_text;

    var dismiss_button_icon = document.createElement("i");
    dismiss_button_icon.className = "fa fa-thumbs-up";

    dismiss_button.appendChild(dismiss_button_icon);
    dismiss_button.appendChild(dismiss_button_text);
    
    dismiss_button.addEventListener("click", function() {
        dismiss_function();
    });

    popover_content.appendChild(message_span);
    popover_content.appendChild(dismiss_button);

    return popover_content;
}

function notify_with_popup(position, element, message) {
    var id = "#" + element.id;
    
    var dismiss_function = function() {
        $(id).popover('hide');
    };

    var popover_content = create_dismissible_popup(message, "Ok, got it!", dismiss_function);

    $(id).popover({
        content: popover_content,
		html: true,
		placement: position,
        trigger: "manual",
    });

    $(id).popover("show");
}