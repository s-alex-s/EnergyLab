import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class ObjectsEN(SqlAlchemyBase):
    __tablename__ = 'ObjectsEN'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    object_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('StationEN.id'))
    accounting_energy = orm.relationship('AccountingEnergyEN', backref='object')
