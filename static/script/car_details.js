function hire(user) {
    if (user != "") {
        show_div_hire();
    } else {
        alert("Please login before continuing!")
    }
}


function show_div_hire(){
    document.getElementById("div-hire").style.display = "block";
    window.scrollBy(0,150);
    document.getElementById("hire-button").disabled = true;
    document.getElementById("hire-button").style.background = "gray";
    document.getElementById("hire-button").style.borderColor = "gray";

    document.getElementById("date-from").valueAsDate = new Date;
    document.getElementById("date-to").valueAsDate = new Date;
}

function show_date_error(error) {
    alert(error);
    show_div_hire();
}

function show_div_confirm_hire(isAvailable, strDateFrom, strDateTo) {
    // show_div_hire();
    document.getElementById("div-hire").style.display = "block";
    document.getElementById("div-confirm-hire").style.display = "block";
    document.getElementById("hire-button").disabled = true;
    document.getElementById("hire-button").style.background = "gray";
    document.getElementById("hire-button").style.borderColor = "gray";
    document.getElementById("date-from").value = strDateFrom;
    document.getElementById("date-to").value = strDateTo;
    window.scrollBy(0,500);
    if (isAvailable == "True") {
        document.getElementById("msg-confirm-hire").style.color = "black";
    } else {
        document.getElementById("msg-confirm-hire").style.color = "red";
    }
}

function hidden_div_confirm_hire() {
    document.getElementById("div-confirm-hire").style.display = 'none'
}