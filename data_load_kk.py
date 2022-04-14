from data.Standart import db_session

from data.database.station_kk import StationKK
from data.database.boiler_kk import BoilerKK
from data.database.objects_kk import ObjectsKK
from data.database.accounting_water_kk import AccountingWaterKK
from data.database.accounting_warm_kk import AccountingWarmKK
from data.database.accounting_energy_kk import AccountingEnergyKK

db_session.global_init('db/database.db')

db_sess = db_session.create_session()

stations_main_p_kk = []
stations_main_p2_kk = dict()
for i in db_sess.query(StationKK).all():
    stations_main_p_kk.append({
        'name': i.station_name,
        'address': i.address,
        'boilers': list(map(lambda x: x.boiler_name, i.boiler_unit_type)),
        'id': str(i.id)
    })
    stations_main_p2_kk[i.station_name] = {'address': i.address,
                                           'boilers': list(map(lambda x: x.boiler_name, i.boiler_unit_type)),
                                           'id': i.id}
