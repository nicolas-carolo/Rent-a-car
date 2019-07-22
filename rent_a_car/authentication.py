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
    session.query(UserSession).filter(UserSession.id_user.__eq__(username)).delete()
    user_session = UserSession(session_id, username)
    session.add(user_session)
    session.commit()
    session.close()
    return session_id


def delete_session(session_id):
    session = start_session()
    session.query(UserSession).filter(UserSession.id_session.__eq__(session_id)).delete()
    session.commit()
    session.close()


def check_authentication(username, session_id):
    session = start_session()
    queryset = session.query(UserSession).filter(UserSession.id_session.__eq__(session_id))
    try:
        session = queryset2list(queryset)[0]
        return True
    except IndexError:
        return False

