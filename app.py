from flask import Flask, render_template
from data.Standart import db_session
from data_load import winddata_json, airtemp_json, winddata_max_min, airtemp_max_min

from data.database.winddata import Winddata
from data.database.airtemp import AirTemp


db_session.global_init('db/database.db')

app = Flask(__name__)

stations = [('ТЭЦ-1', 'ул. Ондирис, 4/4'),
            ('ТЭЦ-2', 'ул. Александра Пушкина'),
            ('п. Пригородный (резерв)', 'ул. Беласар'),
            ('п. Железнодородный', 'ул. Екибастуз'),
            ('п. Промышленный', 'ул. Шарбакты'),
            ('п. Интернациональный', 'ул. Нурлыжол'),
            ('КГ КНБ п. Пригородный', 'ул. Беласар'),
            ('п. УПТК', 'ул. Атырау'),
            ('п. Мичурино', 'ул. Песчаная')]


@app.route('/')
def main_page():
    return render_template('main-page.html',
                           winddata=winddata_json,
                           airtemp=airtemp_json,
                           winddata_max_min=winddata_max_min,
                           airtemp_max_min=airtemp_max_min,
                           stations=stations)


@app.route('/analytics')
def analytics_page():
    return render_template('analytics.html')


if __name__ == '__main__':
    app.run()
