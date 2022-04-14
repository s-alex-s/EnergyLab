import sqlalchemy
from data.Standart.db_session import SqlAlchemyBase


class AccountingWaterEN(SqlAlchemyBase):
    __tablename__ = 'AccountingWaterEN'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('StationEN.id'))
