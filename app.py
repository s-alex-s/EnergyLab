from flask import Flask, render_template, request, redirect
from flask_babel import Babel

from data.Standart import db_session
from data_load import winddata_json, airtemp_json, winddata_max_min, airtemp_max_min, stations_main_p, \
    stations_main_p2, json_data_id_ru
from data_load_en import stations_main_p_en, stations_main_p2_en, json_data_id_en
from data_load_kk import stations_main_p_kk, stations_main_p2_kk, json_data_id_kk

from data.database.station import Station
from data.database.station_en import StationEN
from data.database.station_kk import StationKK


db_session.global_init('db/database.db')

app = Flask(__name__)
babel = Babel(app)


BASE_URL = 'https://energylab.kz/'
current_lang = 'ru'


@app.context_processor
def utility_processor():
    def dec_lang():
        global current_lang

        LANGS = {
            'ru': 'none',
            'en': 'none',
            'kk': 'none',
            current_lang: 'underline'
        }

        return LANGS
    return dict(LANGS=dec_lang())


@babel.localeselector
def get_locale():
    global current_lang

    return current_lang


@app.route('/change_lang/ru')
def ru():
    global current_lang

    current_lang = 'ru'
    if request.referrer:
        return redirect(request.referrer)
    return redirect(BASE_URL)


@app.route('/change_lang/en')
def en():
    global current_lang

    current_lang = 'en'
    if request.referrer:
        return redirect(request.referrer)
    return redirect(BASE_URL)


@app.route('/change_lang/kz')
def kz():
    global current_lang

    current_lang = 'kk'
    if request.referrer:
        return redirect(request.referrer)
    return redirect(BASE_URL)


@app.route('/')
def main_page():
    if current_lang == 'ru':
        return render_template('main-page.html',
                               winddata=winddata_json,
                               airtemp=airtemp_json,
                               winddata_max_min=winddata_max_min,
                               airtemp_max_min=airtemp_max_min,
                               stations=stations_main_p,
                               stations2=stations_main_p2)
    elif current_lang == 'en':
        return render_template('main-page.html',
                               winddata=winddata_json,
                               airtemp=airtemp_json,
                               winddata_max_min=winddata_max_min,
                               airtemp_max_min=airtemp_max_min,
                               stations=stations_main_p_en,
                               stations2=stations_main_p2_en)
    elif current_lang == 'kk':
        return render_template('main-page.html',
                               winddata=winddata_json,
                               airtemp=airtemp_json,
                               winddata_max_min=winddata_max_min,
                               airtemp_max_min=airtemp_max_min,
                               stations=stations_main_p_kk,
                               stations2=stations_main_p2_kk)


@app.route('/analytics')
def analytics_page():
    db_sess = db_session.create_session()
    if current_lang == 'ru':
        stations = db_sess.query(Station).all()

        return render_template('analytics.html', stations=stations, json_data=json_data_id_ru)
    elif current_lang == 'en':
        stations = db_sess.query(StationEN).all()

        return render_template('analytics.html', stations=stations, json_data=json_data_id_en)
    elif current_lang == 'kk':
        stations = db_sess.query(StationKK).all()

        return render_template('analytics.html', stations=stations, json_data=json_data_id_kk)


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/station-info/<int:station_id>')
def object_info(station_id):
    db_sess = db_session.create_session()
    if current_lang == 'ru':
        station = db_sess.query(Station).get(station_id)
    elif current_lang == 'en':
        station = db_sess.query(StationEN).get(station_id)
    elif current_lang == 'kk':
        station = db_sess.query(StationKK).get(station_id)

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
