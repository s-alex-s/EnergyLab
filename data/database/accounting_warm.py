import sqlalchemy
from data.Standart.db_session import SqlAlchemyBase


class AccountingWarm(SqlAlchemyBase):
    __tablename__ = ' AccountingWarm'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    device_type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    factory_number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    placement = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('Station.id'))
