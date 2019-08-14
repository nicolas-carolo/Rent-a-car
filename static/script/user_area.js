function show_div_change_password() {
    document.getElementById("div-user-info").style.display = "none";
    document.getElementById("div-change-pwd").style.display = "block";
    disable_div_reservations();
}

function edit_user_info(session_id, user) {
    window.location.href = '/user_area?session-id=' + session_id + '&user-id=' + user + '&edit=true';
}

function disable_div_reservations() {
    var buttons = document.getElementsByName("view-details-button");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].style.background = "gray";
        buttons[i].style.borderColor = "gray";
    }
    var buttons = document.getElementsByName("delete-reservation-button");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].style.background = "gray";
        buttons[i].style.borderColor = "gray";
    }
    var nodes = document.getElementById("div-reservations").getElementsByTagName('*');
    for(var i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
    }
}

function assign_color_to_reservation_status() {
    var status = document.getElementsByName("reservation-status");
    for (var i = 0; i < status.length; i++) {
        if (status[i].innerText == 'Completed') {
            status[i].style.color = 'gray';
        } else if (status[i].innerText == 'In progress') {
            status[i].style.color = 'darkorange';
        } else {
            status[i].style.color = 'green';
        }
    }
}

function assign_color_to_delete_reservation_buttons() {
    var buttons = document.getElementsByName("delete-reservation-button");
    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i].disabled) {
            buttons[i].style.background = "gray";
            buttons[i].style.borderColor = "gray";
        }
    }
}

function delete_reservation(reservation_id, session_id, user) {
    var input = confirm("Do you really want to delete the reservation n° " + reservation_id + "?");
    if (input == true) {
        window.location.href = '/delete_reservation?session-id=' + session_id + '&user-id=' + user + '&reservation-id=' + reservation_id;
    }
}

function delete_account(session_id, user) {
    var input = confirm("Do you really want to delete your account?");
    if (input == true) {
        window.location.href = '/delete_user?session-id=' + session_id + '&user-id=' + user;
    }
}