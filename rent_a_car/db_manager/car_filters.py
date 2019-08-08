from rent_a_car.db_manager.models import Car


def filter_cars_by_brand(queryset, filter):
    queryset = queryset.filter(Car.brand.__eq__(filter))
    return queryset


def filter_cars_by_type(queryset, filter):
    queryset = queryset.filter(Car.car_type.__eq__(filter))
    return queryset


def filter_cars_by_n_seats(queryset, filter):
    queryset = queryset.filter(Car.n_seats.__eq__(filter))
    return queryset
