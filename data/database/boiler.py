import sqlalchemy
from data.Standart.db_session import SqlAlchemyBase


class Boiler(SqlAlchemyBase):
    __tablename__ = 'Boiler'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    boiler_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    power_passport = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    power_fact = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    fuel2019_gas = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    fuel2019_masut = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    fuel2019_ugol = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    fuel2020_gas = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    fuel2020_masut = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    fuel2020_ugol = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    fuel2021_gas = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    fuel2021_masut = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    fuel2021_ugol = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    warm2019 = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    warm2020 = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    warm2021 = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    station_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey('Station.id'))
