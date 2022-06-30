from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .models import User

Base = declarative_base()

engine = None
db_session = None


def init(host, username, password, db_name, recreate_tables=False):
    """Creates the db connection and the tables if does not exist
    :param host > host address including port 
    :param username
    :param password
    """
    global engine 
    global db_session
    engine = create_engine(
        f'mysql+pymysql://{username}:{password}@{host}/{db_name}', echo=False)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()

    # import all modules that might define models so that
    # they will be registered properly on the metadata.
    # the tables will only be created if they dont exist

    if(recreate_tables):
        Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine)


def clear_session():
    db_session.remove()


def commit_session():
    db_session.commit()
# -------------------notification_request-------------------------


def get_user(cubis_profile_id)->User:

     return  db_session.query(User)\
            .filter(User.cubis_user_id == cubis_profile_id)\
            .first()


def add_user(cubis_profile_id):
    user = User(cubis_user_id=cubis_profile_id)
    db_session.add(user)
    db_session.commit()


def save_notification_request(voice_message=None, teams_message=None, teams_verification=False, voice_verification=False, severity=None, on_shift_analyst=None, requested_time=datetime.now()):
    # req = NoitificationRequest(voice_message=voice_message,
    #                            teams_message=teams_message,
    #                            teams_verification=teams_verification,
    #                            voice_verification=voice_verification,
    #                            severity=severity,
    #                            on_shift_analyst=on_shift_analyst,
    #                            created_time=requested_time)
    # db_session.add(req)
    db_session.commit()
    # return req
