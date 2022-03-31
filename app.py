from flask import Flask, render_template
from data.Standart import db_session
from data_load import winddata_json, airtemp_json, winddata_max_min, airtemp_max_min

from data.database.winddata import Winddata
from data.database.airtemp import AirTemp


db_session.global_init('db/database.db')

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main-page.html',
                           winddata=winddata_json,
                           airtemp=airtemp_json,
                           winddata_max_min=winddata_max_min,
                           airtemp_max_min=airtemp_max_min)


@app.route('/analytics')
def analytics_page():
    return render_template('analytics.html')


if __name__ == '__main__':
    app.run()
