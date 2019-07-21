from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import User
from rent_a_car.db_manager.result_set import queryset2list


def authenticate(username, inserted_password):
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(username))
    session.close()
    try:
        user = queryset2list(queryset)[0]
        if user.password == inserted_password:
            return True
        else:
            return False
    except IndexError:
        return False

