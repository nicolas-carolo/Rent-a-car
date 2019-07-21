from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import User, UserSession
from rent_a_car.db_manager.result_set import queryset2list
import uuid


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


def generate_session(username):
    session_id = str(uuid.uuid1())
    session = start_session()
    user_session = UserSession(session_id, username)
    session.add(user_session)
    session.commit()
    session.close()
    return session_id

