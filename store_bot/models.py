from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, create_engine

engine = create_engine('sqlite:///store_bot.db')


class Base(DeclarativeBase):
    pass


class Accounts(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(Integer)
    username = Column(Text)
    cart_id = Column(Text)


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    desc = Column(Text)
    price = Column(Integer)
    photo = Column(Text)
    type = Column(Text)
