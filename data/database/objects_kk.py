import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class ObjectsKK(SqlAlchemyBase):
    __tablename__ = 'ObjectsKK'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    object_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('StationKK.id'))
    accounting_energy = orm.relationship('AccountingEnergyKK', backref='object')
