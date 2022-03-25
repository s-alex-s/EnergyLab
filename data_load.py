from data.Standart import db_session

from data.database.winddata import Winddata
from data.database.airtemp import AirTemp


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
