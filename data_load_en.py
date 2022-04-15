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

stations = db_sess.query(StationEN).all()
json_data_id_en = dict()
colors = [
    '#FB5156',
    '#FBCB51',
    '#77DDE7',
    '#8579E2',
    '#89E279',
    '#919192',
    '#E279CF',
    '#003153',
    '#8CCB5E',
    '#79C7E2',
    '#FFDB8B',
    '#8A7F8E',
    '#CED23A',
    '#AC7580'
]

for st in stations:
    json_data_id_en[st.id] = {}
    for n, i in enumerate(st.boiler_unit_type):
        if i.boiler_name not in json_data_id_en.keys():
            json_data_id_en[st.id][i.boiler_name] = {}
            json_data_id_en[st.id][i.boiler_name]['color'] = colors[n]

        json_data_id_en[st.id][i.boiler_name]['2019_gas'] = i.fuel2019_gas
        json_data_id_en[st.id][i.boiler_name]['2019_masut'] = i.fuel2019_masut
        json_data_id_en[st.id][i.boiler_name]['2019_ugol'] = i.fuel2019_ugol
        json_data_id_en[st.id][i.boiler_name]['2019_warm'] = i.warm2019

        json_data_id_en[st.id][i.boiler_name]['2020_gas'] = i.fuel2020_gas
        json_data_id_en[st.id][i.boiler_name]['2020_masut'] = i.fuel2020_masut
        json_data_id_en[st.id][i.boiler_name]['2020_ugol'] = i.fuel2020_ugol
        json_data_id_en[st.id][i.boiler_name]['2020_warm'] = i.warm2020

        json_data_id_en[st.id][i.boiler_name]['2021_gas'] = i.fuel2021_gas
        json_data_id_en[st.id][i.boiler_name]['2021_masut'] = i.fuel2021_masut
        json_data_id_en[st.id][i.boiler_name]['2021_ugol'] = i.fuel2021_ugol
        json_data_id_en[st.id][i.boiler_name]['2021_warm'] = i.warm2021
