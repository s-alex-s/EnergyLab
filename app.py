from flask import Flask, render_template

from data.Standart import db_session
from data_load import winddata_json, airtemp_json, winddata_max_min, airtemp_max_min, stations_main_p, stations_main_p2

from data.database.station import Station


db_session.global_init('db/database.db')

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main-page.html',
                           winddata=winddata_json,
                           airtemp=airtemp_json,
                           winddata_max_min=winddata_max_min,
                           airtemp_max_min=airtemp_max_min,
                           stations=stations_main_p,
                           stations2=stations_main_p2)


@app.route('/analytics')
def analytics_page():
    return render_template('analytics.html')


@app.route('/station-info/<int:station_id>')
def object_info(station_id):
    db_sess = db_session.create_session()
    station = db_sess.query(Station).get(station_id)

    json_data = dict()
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

    for n, i in enumerate(station.boiler_unit_type):
        if i.boiler_name not in json_data.keys():
            json_data[i.boiler_name] = {}
            json_data[i.boiler_name]['color'] = colors[n]

        json_data[i.boiler_name]['2019_gas'] = i.fuel2019_gas
        json_data[i.boiler_name]['2019_masut'] = i.fuel2019_masut
        json_data[i.boiler_name]['2019_ugol'] = i.fuel2019_ugol
        json_data[i.boiler_name]['2019_warm'] = i.warm2019

        json_data[i.boiler_name]['2020_gas'] = i.fuel2020_gas
        json_data[i.boiler_name]['2020_masut'] = i.fuel2020_masut
        json_data[i.boiler_name]['2020_ugol'] = i.fuel2020_ugol
        json_data[i.boiler_name]['2020_warm'] = i.warm2020

        json_data[i.boiler_name]['2021_gas'] = i.fuel2021_gas
        json_data[i.boiler_name]['2021_masut'] = i.fuel2021_masut
        json_data[i.boiler_name]['2021_ugol'] = i.fuel2021_ugol
        json_data[i.boiler_name]['2021_warm'] = i.warm2021

    return render_template('station-info.html', station=station, json_data=json_data)


if __name__ == '__main__':
    app.run()
