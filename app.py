from unicodedata import normalize
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
# import csv

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import City

@app.route("/load")
def load():
    load_data()

def load_data():
    PATH_DATA = './data/pib_data.csv'
    NAME_COLUMN = 3
    PROVINCY_COLUMN = 2
    CENSUS_COLUMN = 4
    PIB_COLUMN = 5
    POPULATION_COLUMN = 6
    PIB_PER_CAPITA_COLUMN = 7

    with open(PATH_DATA) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[1]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
                city=City(
                    name=normalize_name(row[NAME_COLUMN]),
                    provincy=normalize_name(row[PROVINCY_COLUMN]),
                    census_date=row[CENSUS_COLUMN], 
                    pib=row[PIB_COLUMN], 
                    population=row[POPULATION_COLUMN], 
                    population_date=2009, 
                    pib_per_capita=row[PIB_PER_CAPITA_COLUMN]
                )
                db.session.add(city)
                db.session.commit()
        print(f'Processed {line_count} lines.')

def normalize_name(txt):
    txt = txt.upper()
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')    

@app.route("/pib")
def getCityInfo():
    cityName = request.args.get('cidade').capitalize()
    try:
        city=City.query.filter_by(name=cityName).first()
        return jsonify(city.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()


# tutorial: https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc