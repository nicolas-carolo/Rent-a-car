from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import User, UserSession
from rent_a_car.db_manager.result_set import queryset2list
import uuid


def authenticate(username, inserted_password):
    """
    Authenticate a user checking his credentials
    :param username: the username inserted by the user
    :param inserted_password: the password inserted by the user
    :return: True if the credentials are valid, False if not
    """
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
    """
    Generate a new user session for the user identified by the username
    :param username: the user's email address
    :return: the session ID that identifies the user session just created
    """
    session_id = str(uuid.uuid1())
    session = start_session()
    session.query(UserSession).filter(UserSession.id_user.__eq__(username)).delete()
    user_session = UserSession(session_id, username)
    session.add(user_session)
    session.commit()
    session.close()
    return session_id


def edit_session(session_id, new_username):
    """
    Edit the username associated to a user session
    :param session_id: the ID of the session to edit
    :param new_username: the new username for the session
    :return: None
    """
    session = start_session()
    user_session = session.query(UserSession).get(session_id)
    user_session.id_user = new_username
    session.commit()
    session.close()


def delete_session(session_id):
    """
    Delete the user session identified by session_id
    :param session_id: the ID of the session we want to delete
    :return: None
    """
    session = start_session()
    session.query(UserSession).filter(UserSession.id_session.__eq__(session_id)).delete()
    session.commit()
    session.close()


def check_authentication(session_id, username):
    """
    Check if session_id and username can uniquely identified a user session previously created in oredr
    to authenticate a user
    :param session_id: the ID of the user session
    :param username: the user's email address
    :return: True if the user can authenticate, otherwise False
    """
    session = start_session()
    queryset = session.query(UserSession).filter(UserSession.id_session.__eq__(session_id))
    try:
        user_session = queryset2list(queryset)[0]
        if user_session.id_user == username:
            return True
        else:
            return False
    except IndexError:
        return False


def get_user_by_session_id(session_id):
    """
    Get the the user associated to the user session identified by session_id
    :param session_id: the ID of the session
    :return: the username of the user associated to the user session
    """
    session = start_session()
    queryset = session.query(UserSession).filter(UserSession.id_session.__eq__(session_id))
    try:
        user_session = queryset2list(queryset)[0]
        return user_session.id_user
    except IndexError:
        return None

