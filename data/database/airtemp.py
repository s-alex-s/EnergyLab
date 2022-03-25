import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class AirTemp(SqlAlchemyBase):
    __tablename__ = 'AirTemp'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    temp = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
