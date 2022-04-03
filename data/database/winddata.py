import sqlalchemy
from data.Standart.db_session import SqlAlchemyBase


class Winddata(SqlAlchemyBase):
    __tablename__ = 'Winddata'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    speed = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
