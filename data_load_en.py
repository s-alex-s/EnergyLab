from data.Standart import db_session

from data.database.station_en import StationEN
from data.database.boiler_en import BoilerEN
from data.database.objects_en import ObjectsEN
from data.database.accounting_water_en import AccountingWaterEN
from data.database.accounting_warm_en import AccountingWarmEN
from data.database.accounting_energy_en import AccountingEnergyEN

db_session.global_init('db/database.db')

db_sess = db_session.create_session()

stations_main_p_en = []
stations_main_p2_en = dict()
for i in db_sess.query(StationEN).all():
    stations_main_p_en.append({
        'name': i.station_name,
        'address': i.address,
        'boilers': list(map(lambda x: x.boiler_name, i.boiler_unit_type)),
        'id': str(i.id)
    })
    stations_main_p2_en[i.station_name] = {'address': i.address,
                                           'boilers': list(map(lambda x: x.boiler_name, i.boiler_unit_type)),
                                           'id': i.id}
