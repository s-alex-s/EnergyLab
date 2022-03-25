from flask import Flask, render_template
from data.Standart import db_session
from pprint import pprint
from data_load import winddata_json

from data.database.winddata import Winddata
from data.database.airtemp import AirTemp


db_session.global_init('db/database.db')

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main-page.html', winddata=winddata_json)


if __name__ == '__main__':
    app.run()
