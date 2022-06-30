from sqlalchemy import Column, Integer, String, DateTime, Boolean, SmallInteger, ForeignKey, TypeDecorator
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    cubis_user_id = Column(String(40))
    user_companies = relationship("UserCompany")
    def __init__(self, cubis_user_id=None):
        self.cubis_user_id = cubis_user_id

    def __repr__(self):
        return f'<user {self.id!r}>'
    
class UserCompany(Base):
    __tablename__ = 'user_company'
    id = Column(Integer, primary_key=True)
    notification_id = Column(Integer, ForeignKey('user.id'))
    provider_account_id = Column(Integer)
    

    def __init__(self, notification_id=None,provider_account_id=None):
        self.notification_id = notification_id
        self.provider_account_id = provider_account_id
        
    def __repr__(self):
        return f'<user_company {self.id!r}>'

