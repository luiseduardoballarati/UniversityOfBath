from flask import Blueprint
from flask import render_template, request, redirect
from database import db
from models import Pilot
from models import Aircraft
from models import Airport
from models import Flight
from models import Route
from sqlalchemy import func
from sqlalchemy.sql import alias
from models import FlightDetail
from datetime import datetime
from sqlalchemy import extract
from collections import Counter
import calendar
from sqlalchemy import text 

bp_menu = Blueprint("menu", __name__, template_folder="templates/menu")

@bp_menu.route('/menu')
def menu():
  return render_template("menu.html")

@bp_menu.route('/pilots')
def pilots_flown_hours():
   try:
     max_flown_hours = db.session.query(func.max(Pilot.flown_hours)).scalar()
     top_pilots = Pilot.query.filter(Pilot.flown_hours == max_flown_hours).all()
     pilot_name = {top_pilots.pilot_id: top_pilots.first_name for top_pilots in Pilot.query.all()}
    
     return render_template("pilots_flown_hours.html", top_pilots=top_pilots, pilot_name=pilot_name)
   except:
     return render_template("error.html")
@bp_menu.route('/aircraft')
def biggest_aircraft():
  try:
    biggest_aircraft = db.session.query(func.max(Aircraft.passenger_capacity)).scalar()
    top_aircraft = Aircraft.query.filter(Aircraft.passenger_capacity == biggest_aircraft).all()
    aircraft_model = {top_aircraft.aircraft_id: top_aircraft.manufacturer for top_aircraft in Aircraft.query.all()}
  
    return render_template("biggest_aircraft.html", top_aircraft=top_aircraft, aircraft_model=aircraft_model)
  except:
   return render_template("error.html")


@bp_menu.route('/airport')
def most_common_place():
  try:
    arrival_ids = Route.query.with_entities(Route.arrival_airport_id).all()
    counter = {}
    for id in arrival_ids:
      if id not in counter:
        counter[id] = 0
      counter[id] += 1
  
    k = max(counter.values())
    value = {i for i in counter if counter[i]==k}
    list = []
    airports = []
    vt = type(value)
  
    for item in value:
      for number in item:
        list.append(number)
  
    top_airports = Airport.query.filter(Airport.airport_id.in_(list)).all()
  
    airport_infos = [(airport.airport_id, airport.airport_name, airport.city, airport.country) for airport in top_airports]
  
    return render_template("most_common_airport.html", airport_infos=airport_infos, k=k)
  except:
   return render_template("error.html")



@bp_menu.route('/aircraft2')
def most_used_aircraft():
  try:
    aircraft_ids = Flight.query.with_entities(Flight.aircraft_id).all()
    counter = {}
    for id in aircraft_ids:
      if id not in counter:
        counter[id] = 0
      counter[id] += 1
    
    k = max(counter.values())
    value = {i for i in counter if counter[i]==k}
    list = []
    aircrafts = []
    
    for item in value:
      for number in item:
        list.append(number)
    
    top_aircrafts = Aircraft.query.filter(Aircraft.aircraft_id.in_(list)).all()
    
    aircraft_infos = [(aircraft.aircraft_id, aircraft.manufacturer, aircraft.model, aircraft.passenger_capacity,
                       aircraft.cruising_range_miles) for aircraft in top_aircrafts]
    
    return render_template("most_used_aircraft.html", aircraft_infos=aircraft_infos, k=k)
  except:
   return render_template("error.html")


@bp_menu.route('/long_short_flight')
def find_long_short_flight():
  try:
    results = db.session.execute(text("""
      SELECT f.flight_id,
      (
      JULIANDAY(f.arrival_date || ' ' || f.arrival_time) * 24 - 
      JULIANDAY(f.departure_date || ' ' || f.departure_time)* 24)
      AS flight_duration
      FROM flight AS f 
      ORDER BY flight_duration DESC 
      LIMIT 1
      """
    ))
  
    results_short = db.session.execute(text("""
      SELECT f.flight_id,
      (
      JULIANDAY(f.arrival_date || ' ' || f.arrival_time) * 24 - 
      JULIANDAY(f.departure_date || ' ' || f.departure_time) * 24)
      AS flight_duration
      FROM flight AS f 
      ORDER BY flight_duration ASC 
      LIMIT 1
      """
    ))
    
    return render_template('long_short_flight.html', results=results, results_short=results_short)
  except:
    return render_template('error.html')

@bp_menu.route('/pilot')
def pilot_the_flew_the_most():
  try:
    pilot_ids = FlightDetail.query.with_entities(FlightDetail.pilot_id).all()
    counter = {}
    for id in pilot_ids:
      if id not in counter:
        counter[id] = 0
      counter[id] += 1

    k = max(counter.values())
    value = {i for i in counter if counter[i]==k}
    list = []
    pilots = []

    for item in value:
      for number in item:
        list.append(number)

    top_pilots = Pilot.query.filter(Pilot.pilot_id.in_(list)).all()

    pilot_infos = [(pilot.pilot_id, pilot.first_name, pilot.last_name, pilot.born_date,
                    pilot.flown_hours) for pilot in top_pilots]

    return render_template("pilot_that_flew_the_most.html", pilot_infos=pilot_infos, k=k)
  except:
   return render_template("error.html")


@bp_menu.route('/flightsper')
def flights_per_year():
    try:
      years, months, mon, year, day, days = [], [], [], [], [], []
      flight_ids = Flight.query.with_entities(Flight.departure_date).all()
                             
      for item in flight_ids:
        for n in item:
          years.append(n.year)
          months.append(n.month)
          days.append(n.day)
  
      x = Counter(years)
      y = Counter(months)
      z = Counter(days)
  
      ky = max(y.values())
      value = {i for i in y if y[i]==ky}

      kx = max(x.values())
      valuex = {j for j in x if x[j]==kx}

      kz = max(z.values())
      valuez = {p for p in z if z[p]==kz}
  
      for i in value:
        mon.append(calendar.month_name[i])

      for j in valuex:
        year.append(j)

      for p in valuez:
        day.append(p)
  
      return render_template("flights_per.html", ky=ky, mon=mon, kx=kx, year=year, kz=kz, day=day)
    except:
     return render_template("error.html")

@bp_menu.route('/flights_per_date', methods=['POST'])
def flights_per_date():
  try:
    date_format = request.form.get('date_format')
    if date_format == 'year':
      res = db.session.query(extract('year', Flight.departure_date), func.count(Flight.flight_id)).group_by(extract('year', Flight.departure_date)).all()
    elif date_format == 'month':
      res = db.session.query(extract('month', Flight.departure_date), func.count(Flight.flight_id)).group_by(extract('month', Flight.departure_date)).all()
    elif date_format == 'day':
      res = db.session.query(extract('day', Flight.departure_date), func.count(Flight.flight_id)).group_by(extract('day', Flight.departure_date)).all()
    else:
      return render_template("error.html")
    return render_template("flights_per_date.html", res=res) 
  except:
    return render_template("error.html")

@bp_menu.route('/flights_per_location')
def flights_per_location():
  top_routes = db.session.query(
    Route.departure_airport_id,
    Route.arrival_airport_id,
    func.count(Flight.route_id).label("flight_count")).join(Flight, Flight.route_id == Route.route_id).group_by(Route.departure_airport_id, Route.arrival_airport_id).order_by(func.count(Flight.flight_id).desc()).all()

  common_routes = []
  for departure_id, arrival_id, flight_count in top_routes:
    departure_airport = Airport.query.get(departure_id)
    arrival_airport = Airport.query.get(arrival_id)
    common_routes.append({
      'departure_city': departure_airport.city,
      'departure_country': departure_airport.country,
      'arrival_city': arrival_airport.city,
      'arrival_country': arrival_airport.country,
      'flight_count': flight_count
  })
  
  return render_template("flights_per_location.html", common_routes=common_routes) 

@bp_menu.route('/search', methods=['POST'])
def search():
  message = ""
  try:
    query = request.form.get('query', '')
    res = db.session.execute(text(query))
    columns = res.keys()
    rows = res.fetchall()
  
    return render_template("search.html", query=query, columns=columns, rows=rows)
  except:
    return render_template("error.html", message="Input a valid query!")
    
@bp_menu.route('/image')
def image():
  try:
    return render_template("image.html")
  except:
    return render_template("error.html")

