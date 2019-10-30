from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
import csv

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
                    name=row[NAME_COLUMN], 
                    provincy=row[PROVINCY_COLUMN], 
                    census_date=row[CENSUS_COLUMN], 
                    pib=row[PIB_COLUMN], 
                    population=row[POPULATION_COLUMN], 
                    population_date=2009, 
                    pib_per_capita=row[PIB_PER_CAPITA_COLUMN]
                )
                db.session.add(city)
                db.session.commit()
        print(f'Processed {line_count} lines.')

# @app.route("/")
# def home():
#     return "HELLO WORLD"

@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)


@app.route("/details")
def get_book_details():
    author=request.args.get('author')
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()