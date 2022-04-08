from flask import Flask, render_template

from data.Standart import db_session
from data_load import winddata_json, airtemp_json, winddata_max_min, airtemp_max_min, stations_main_p, stations_main_p2

from data.database.station import Station
from data.database.boiler import Boiler
from data.database.objects import Objects
from data.database.accounting_water import AccountingWater
from data.database.accounting_warm import AccountingWarm
from data.database.accounting_energy import AccountingEnergy


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

    return render_template('station-info.html', station=station)


if __name__ == '__main__':
    app.run()
