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