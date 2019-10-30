from app import db

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    provincy = db.Column(db.String())
    census_date = db.Column(db.Integer())
    pib = db.Column(db.Float())
    population = db.Column(db.Integer())
    population_date = db.Column(db.Integer())
    pib_per_capita = db.Column(db.Float())

    def __init__(self, name, provincy, census_date, pib, population, population_date, pib_per_capita):
        self.name = name
        self.provincy = provincy
        self.census_date = census_date
        self.pib = pib
        self.population = population
        self.population_date = population_date
        self.pib_per_capita = pib_per_capita

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'provincy': self.provincy,
            'census_date': self.census_date,
            'pib': self.pib,
            'population': self.population,
            'population_date': self.population_date,
            'pib_per_capita': self.pib_per_capita
        }