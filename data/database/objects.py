import sqlalchemy
from sqlalchemy import orm
from data.Standart.db_session import SqlAlchemyBase


class Objects(SqlAlchemyBase):
    __tablename__ = 'Objects'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    object_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('Station.id'))
    accounting_energy = orm.relationship('AccountingEnergy', backref='object')
