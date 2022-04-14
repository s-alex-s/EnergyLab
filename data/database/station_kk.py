import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class StationKK(SqlAlchemyBase):
    __tablename__ = 'StationKK'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    station_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    boiler_unit_type = orm.relationship('BoilerKK', backref='station')
    objects = orm.relationship('ObjectsKK', backref='station')
    accounting_water = orm.relationship('AccountingWaterKK', backref='station')
    accounting_warm = orm.relationship('AccountingWarmKK', backref='station')
