function submit_form_filter() {
    var date_from = document.getElementById("rent-date-from").value;
    var date_to = document.getElementById("rent-date-to").value;
    if (date_from > date_to) {
        alert("Please insert a valid date interval for the rent period!");
        return 0;
    }

    var str_min_power = document.getElementById("car-min-power").value;
    var str_max_power = document.getElementById("car-max-power").value;
    var min_power = parseInt(str_min_power);
    var max_power = parseInt(str_max_power);
    if (min_power > max_power) {
        alert("Minimum power value must be less than the maximum power value!");
        return 0;
    }

    var str_car_year_from = document.getElementById("car-year-from").value;
    var str_car_year_to = document.getElementById("car-year-to").value;
    var car_year_from = parseInt(str_car_year_from);
    var car_year_to = parseInt(str_car_year_to);
    if (car_year_from > car_year_to) {
        alert("Please insert a valid interval of years for the car!");
        return 0;
    }

    var str_min_price = document.getElementById("min-price-day").value;
    var str_max_price = document.getElementById("max-price-day").value;
    var min_price = parseInt(str_min_price);
    var max_price = parseInt(str_max_price);
    if (min_price > max_price) {
        alert("Please insert a valid price interval!");
        return 0;
    }

    document.getElementById("form-cars-filter").submit();
}