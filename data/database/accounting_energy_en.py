import sqlalchemy
from data.Standart.db_session import SqlAlchemyBase


class AccountingEnergyEN(SqlAlchemyBase):
    __tablename__ = 'AccountingEnergyEN'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    factory_PU = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    system_type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    calc_coefficient = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    accuracy_class = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    object_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('ObjectsEN.id'))
