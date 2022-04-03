import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class Station(SqlAlchemyBase):
    __tablename__ = 'Station'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    station_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    boiler_unit_type = orm.relationship('Boiler', backref='station')
    objects = orm.relationship('Objects', backref='station')
    accounting_water = orm.relationship('AccountingWater', backref='station')
    accounting_warm = orm.relationship('AccountingWarm', backref='station')
