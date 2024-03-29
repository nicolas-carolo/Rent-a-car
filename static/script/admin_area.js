function hide_show_reservation_items() {
    var items = document.getElementsByName("reservation-item");
    if (document.getElementById("all-reservations").style.display == "block") {
        for (var i = 0; i < items.length; i++) {
                items[i].style.display = "none"
        }
    } else {
        for (var i = 0; i < items.length; i++) {
                items[i].style.display = "block"
        }
    }
}

function hide_show_news_items() {
    var items = document.getElementsByName("news-item");
    if (document.getElementById("all-news").style.display == "block") {
        for (var i = 0; i < items.length; i++) {
                items[i].style.display = "none"
        }
    } else {
        for (var i = 0; i < items.length; i++) {
                items[i].style.display = "block"
        }
    }
}

function hide_show_cars_items() {
    var items = document.getElementsByName("cars-item");
    if (document.getElementById("all-cars").style.display == "block") {
        for (var i = 0; i < items.length; i++) {
                items[i].style.display = "none"
        }
    } else {
        for (var i = 0; i < items.length; i++) {
                items[i].style.display = "block"
        }
    }
}

function show_div_change_password() {
    document.getElementById("div-user-info").style.display = "none";
    document.getElementById("div-change-pwd").style.display = "block";
    disable_div_reservations();
}

function edit_user_info(session_id, user) {
    window.location.href = '/admin_user_area?session-id=' + session_id + '&user-id=' + user + '&edit=true';
}

function cancel_edit(session_id, user) {
    window.location.href = '/admin_user_area?session-id=' + session_id + '&user-id=' + user + '&edit=false';
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
    if (input) {
        window.location.href = '/delete_reservation?session-id=' + session_id + '&user-id=' + user + '&reservation-id=' + reservation_id;
    }
}

function delete_account(session_id, user) {
    var input = confirm("Do you really want to delete your account?");
    if (input) {
        window.location.href = '/delete_user?session-id=' + session_id + '&user-id=' + user;
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

function delete_car(car_id, brand, model, session_id, user) {
    var input = confirm("Do you really want to delete the car " + brand + " " + model + "?");
    if (input) {
        window.location.href = '/delete_car?car-id=' + car_id + '&session-id=' + session_id +'&user-id=' + user;
    }
}

function delete_news(news_id, news_description, session_id, user) {
    var input = confirm("Do you really want to delete the news \'" + news_description + "\'?");
    if (input) {
        window.location.href = '/delete_news?news-id=' + news_id + '&session-id=' + session_id +'&user-id=' + user;
    }
}

function update_account_type(user_id_to_update, account_type, session_id, user) {
    if (account_type == 'admin') {
        var input = confirm("Do you really want to grant admin privileges to the user " + user_id_to_update + "?");
    } else {
        var input = confirm("Do you really want to revoke admin privileges to the user " + user_id_to_update + "?");
    }
    if (input) {
        window.location.href = '/update_account_type?user-id-to-update=' + user_id_to_update + '&account-type=' + account_type + '&session-id=' + session_id +'&user-id=' + user;
    }
}

