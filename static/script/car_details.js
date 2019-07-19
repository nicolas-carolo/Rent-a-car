function show_div_hire(){
    document.getElementById("div-hire").style.display = "block";
    window.scrollBy(0,150);
    document.getElementById("hire-button").disabled = true;
    document.getElementById("hire-button").style.background = "gray"
    document.getElementById("hire-button").style.borderColor = "gray"
}

function show_date_error(error) {
    alert(error);
    show_div_hire();
}