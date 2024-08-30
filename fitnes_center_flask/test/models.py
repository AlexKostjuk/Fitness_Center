from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db import main

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    birth_date = Column(DateTime, default='1940-01-01', nullable=False)
    phone = Column(String(50), nullable=False)
    funds = Column(Integer, nullable=False)


    def __init__(self, login, password, birth_date, phone):
        self.login = login
        self.password = password
        self.birth_date = birth_date
        self.phone = phone
        self.funds = 0

    def __repr__(self):
        return f'<User {self.name!r}>'