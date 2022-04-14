import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class StationEN(SqlAlchemyBase):
    __tablename__ = 'StationEN'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    station_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    boiler_unit_type = orm.relationship('BoilerEN', backref='station')
    objects = orm.relationship('ObjectsEN', backref='station')
    accounting_water = orm.relationship('AccountingWaterEN', backref='station')
    accounting_warm = orm.relationship('AccountingWarmEN', backref='station')
