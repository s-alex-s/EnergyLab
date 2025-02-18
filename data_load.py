from data.Standart import db_session

from data.database.winddata import Winddata
from data.database.airtemp import AirTemp
from data.database.station import Station
from data.database.boiler import Boiler
from data.database.objects import Objects
from data.database.accounting_water import AccountingWater
from data.database.accounting_warm import AccountingWarm
from data.database.accounting_energy import AccountingEnergy

db_session.global_init('db/database.db')

db_sess = db_session.create_session()
winddata = db_sess.query(Winddata).all()
winddata_json = dict()

for i in list(sorted(list(set([j.date.year for j in winddata])))):
    winddata_json[str(i)] = []

for i in [i for i in range(1, 13)]:
    for j in winddata_json.keys():
        if j.isdigit():
            winddata2 = list(map(lambda y: y.speed,
                                 filter(lambda x: x.date.month == i and x.date.year == int(j), winddata)))
            winddata_json[j].append(sum(winddata2) // len(winddata2))

for year in list(winddata_json.keys()):
    key = str(year) + '_in'
    winddata_json[key] = {}

    month_m = list(filter(lambda x: x.date.year == int(year), winddata))
    for month in range(1, 13):
        formated_month = month
        if month < 10:
            formated_month = f'0{month}'

        winddata_json[key][str(formated_month)] = {}
        day_m = list(filter(lambda y: y.date.month == int(formated_month), month_m))
        for day in range(1, max(list(map(lambda x: x.date.day, day_m))) + 1):
            formated_day = day
            if day < 10:
                formated_day = f'0{day}'

            winddata_json[key][str(formated_month)][str(formated_day)] = []
            time_m = list(filter(lambda z: z.date.day == int(formated_day), day_m))
            for time in time_m:
                winddata_json[key][str(formated_month)][str(formated_day)].append((str(time.date.time()), time.speed))

airtemp = db_sess.query(AirTemp).all()
airtemp_json = dict()

for i in list(sorted(list(set([j.date.year for j in airtemp])))):
    airtemp_json[str(i)] = []

for i in [i for i in range(1, 13)]:
    for j in airtemp_json.keys():
        if j.isdigit():
            airtemp2 = list(map(lambda y: y.temp,
                                filter(lambda x: x.date.month == i and x.date.year == int(j), airtemp)))
            airtemp_json[j].append(sum(airtemp2) // len(airtemp2))

for year in list(airtemp_json.keys()):
    key = str(year) + '_in'
    airtemp_json[key] = {}

    month_m = list(filter(lambda x: x.date.year == int(year), airtemp))
    for month in range(1, 13):
        formated_month = month
        if month < 10:
            formated_month = f'0{month}'

        airtemp_json[key][str(formated_month)] = {}
        day_m = list(filter(lambda y: y.date.month == int(formated_month), month_m))
        for day in range(1, max(list(map(lambda x: x.date.day, day_m))) + 1):
            formated_day = day
            if day < 10:
                formated_day = f'0{day}'

            airtemp_json[key][str(formated_month)][str(formated_day)] = []
            time_m = list(filter(lambda z: z.date.day == int(formated_day), day_m))
            for time in time_m:
                airtemp_json[key][str(formated_month)][str(formated_day)].append((str(time.date.time()), time.temp))

winddata_max_min = [max([int(i) for i in winddata_json.keys() if '_in' not in i]),
                    min([int(i) for i in winddata_json.keys() if '_in' not in i])]
airtemp_max_min = [max([int(i) for i in airtemp_json.keys() if '_in' not in i]),
                   min([int(i) for i in airtemp_json.keys() if '_in' not in i])]

stations_main_p = []
stations_main_p2 = dict()
for i in db_sess.query(Station).all():
    stations_main_p.append({
        'name': i.station_name,
        'address': i.address,
        'boilers': list(map(lambda x: x.boiler_name, i.boiler_unit_type)),
        'id': str(i.id)
    })
    stations_main_p2[i.station_name] = {'address': i.address,
                                        'boilers': list(map(lambda x: x.boiler_name, i.boiler_unit_type)),
                                        'id': i.id}

stations = db_sess.query(Station).all()
json_data_id_ru = dict()
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
    json_data_id_ru[st.id] = {}
    for n, i in enumerate(st.boiler_unit_type):
        if i.boiler_name not in json_data_id_ru.keys():
            json_data_id_ru[st.id][i.boiler_name] = {}
            json_data_id_ru[st.id][i.boiler_name]['color'] = colors[n]

        json_data_id_ru[st.id][i.boiler_name]['2019_gas'] = i.fuel2019_gas
        json_data_id_ru[st.id][i.boiler_name]['2019_masut'] = i.fuel2019_masut
        json_data_id_ru[st.id][i.boiler_name]['2019_ugol'] = i.fuel2019_ugol
        json_data_id_ru[st.id][i.boiler_name]['2019_warm'] = i.warm2019

        json_data_id_ru[st.id][i.boiler_name]['2020_gas'] = i.fuel2020_gas
        json_data_id_ru[st.id][i.boiler_name]['2020_masut'] = i.fuel2020_masut
        json_data_id_ru[st.id][i.boiler_name]['2020_ugol'] = i.fuel2020_ugol
        json_data_id_ru[st.id][i.boiler_name]['2020_warm'] = i.warm2020

        json_data_id_ru[st.id][i.boiler_name]['2021_gas'] = i.fuel2021_gas
        json_data_id_ru[st.id][i.boiler_name]['2021_masut'] = i.fuel2021_masut
        json_data_id_ru[st.id][i.boiler_name]['2021_ugol'] = i.fuel2021_ugol
        json_data_id_ru[st.id][i.boiler_name]['2021_warm'] = i.warm2021
