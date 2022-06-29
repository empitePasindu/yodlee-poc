from sqlalchemy import Column, Integer, String, DateTime, Boolean, SmallInteger, ForeignKey, TypeDecorator
from sqlalchemy.orm import relationship
from .db_manager import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    cubis_user_id = Column(String(40))
    notification_id = Column(Integer, ForeignKey('teams_notification.id'))

    def __init__(self, cubis_user_id=None):
        self.cubis_user_id = cubis_user_id

    def __repr__(self):
        return f'<user {self.id!r}>'
    
class UserCompany(Base):
    __tablename__ = 'user_company'
    id = Column(Integer, primary_key=True)
    cubis_user_id = Column(String(40))
    provider_account_id = Column(Integer)
    

    def __init__(self, cubis_user_id=None):
        self.cubis_user_id = cubis_user_id

    def __repr__(self):
        return f'<user {self.id!r}>'