function show_div_hire(){
    document.getElementById("div-hire").style.display = "block";
    window.scrollBy(0,150);
}

function show_date_error(error) {
    alert(error);
    show_div_hire()
}