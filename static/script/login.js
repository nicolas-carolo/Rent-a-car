function badCredentials(error) {
    alert(error);
}

function validateSession(session_id, authjs) {
    if (session_id == "" && authjs == "True") {
        var session_id = getCookie("session_id");
        if (session_id != "") {
            window.location.href="/auth_session_id?session-id=" + session_id;
        }
    }
}

function getCookie(cookie_name) {
    var cookie_string = RegExp(""+cookie_name+"[^;]+").exec(document.cookie);
    return decodeURIComponent(!!cookie_string ? cookie_string.toString().replace(/^[^=]+./,"") : "");
}

function logout() {
    delete_cookie("session_id")
}

function delete_cookie(cookie_name) {
  document.cookie = cookie_name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}