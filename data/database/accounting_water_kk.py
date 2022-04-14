import sqlalchemy
from data.Standart.db_session import SqlAlchemyBase


class AccountingWaterKK(SqlAlchemyBase):
    __tablename__ = 'AccountingWaterKK'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('StationKK.id'))
