from database import db
from datetime import datetime


# Creating the table pilot
class Pilot(db.Model):
  __tablename__ = 'pilot'
  pilot_id = db.Column(db.Integer, primary_key=True, auto_incremenet=True)
  first_name = db.Column(db.String(100), nullable=False)
  last_name = db.Column(db.String(100), nullable=False)
  born_date = db.Column(db.Date, nullable=False)
  flown_hours = db.Column(db.Integer, nullable=False)
  flight_detail = db.relationship('FlightDetail', backref='pilot')

  def __init__(self, first_name, last_name, born_date, flown_hours):
    self.first_name = first_name
    self.last_name = last_name
    self.born_date = born_date
    self.flown_hours = flown_hours

  def __repr__(self):
    return "Pilot: {}".format(self.pilot_id)


# Table aircraft
class Aircraft(db.Model):
  __tablename__ = 'aircraft'
  aircraft_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
  manufacturer = db.Column(db.String(100), nullable=False)
  model = db.Column(db.String(100), nullable=False)
  passenger_capacity = db.Column(db.Integer, nullable=False)
  cruising_range_miles = db.Column(db.Integer, nullable=False)
  flight = db.relationship('Flight', backref='aircraft')

  def __init__(self, manufacturer, model, passenger_capacity,
               cruising_range_miles):
    self.manufacturer = manufacturer
    self.model = model
    self.passenger_capacity = passenger_capacity
    self.cruising_range_miles = cruising_range_miles

  def __repr__(self):
    return "Aircraft: {}".format(self.aircraft_id)


# Table airport
class Airport(db.Model):
  __tablename__ = "airport"
  airport_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
  airport_name = db.Column(db.String(100), nullable=False)
  city = db.Column(db.String(100), nullable=False)
  country = db.Column(db.String(100), nullable=False)

  def __init__(self, airport_name, city, country):
    self.airport_name = airport_name
    self.city = city
    self.country = country

  def __repr__(self):
    return "Airport: {}".format(self.airport_id)


# Table route
class Route(db.Model):
  __tablename__ = 'route'
  route_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
  departure_airport_id = db.Column(db.Integer,
                                   db.ForeignKey('airport.airport_id'),
                                   nullable=False)
  arrival_airport_id = db.Column(db.Integer,
                                 db.ForeignKey('airport.airport_id'),
                                 nullable=False)

  dep_ref = db.relationship('Airport',
                            backref='route_dep',
                            uselist=False,
                            foreign_keys=[departure_airport_id])
  arr_ref = db.relationship('Airport',
                            backref='route_arr',
                            uselist=False,
                            foreign_keys=[arrival_airport_id])

  def __init__(self, departure_airport_id, arrival_airport_id):
    self.departure_airport_id = departure_airport_id
    self.arrival_airport_id = arrival_airport_id

  def __repr__(self):
    return "Route: {}".format(self.route_id)


# Table Flight
class Flight(db.Model):
  __tablename__ = 'flight'
  flight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  aircraft_id = db.Column(db.Integer,
                          db.ForeignKey('aircraft.aircraft_id'),
                          nullable=False)
  route_id = db.Column(db.Integer,
                       db.ForeignKey('route.route_id'),
                       nullable=False)
  departure_date = db.Column(db.Date, nullable=False)
  departure_time = db.Column(db.Time, nullable=False)
  arrival_date = db.Column(db.Date, nullable=False)
  arrival_time = db.Column(db.Time, nullable=False)
  flight_detail = db.relationship('FlightDetail', backref='flight')

  def __init__(self, aircraft_id, route_id, departure_date, departure_time,
               arrival_date, arrival_time):
    self.aircraft_id = aircraft_id
    self.route_id = route_id
    self.departure_date = departure_date
    self.departure_time = departure_time
    self.arrival_date = arrival_date
    self.arrival_time = arrival_time


def __repr__(self):
  return "Flight: {}".format(self.flight_id)


# Table Flight Details
class FlightDetail(db.Model):
  __tablename__ = 'flight_detail'
  flight_detail_id = db.Column(db.Integer,
                               primary_key=True,
                               autoincrement=True)
  flight_id = db.Column(db.Integer,
                        db.ForeignKey('flight.flight_id'),
                        nullable=False)
  pilot_id = db.Column(db.Integer,
                       db.ForeignKey('pilot.pilot_id'),
                       nullable=False)


def __init__(self, flight_id, pilot_id):
  self.flight_id = flight_id
  self.pilot_id = pilot_id


def __repr__(self):
  return "Flight Detail: {}".format(self.flight_detail_id)
