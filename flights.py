from flask import Blueprint
from flask import render_template, request, redirect
from models import Flight
from database import db
from datetime import datetime
from models import FlightDetail


bp_flights = Blueprint("flights", __name__, template_folder="templates/flights")


@bp_flights.route("/create", methods=['GET', 'POST'])
def create_flight():
  if request.method == 'GET':
    return render_template("flight_create.html")
  if request.method == 'POST':
    aircraft_id = request.form.get('aircraft_id')
    route_id = request.form.get('route_id')
    
    departure_date = request.form.get('departure_date')
    departure_date = datetime.strptime(departure_date,"%Y-%m-%d")
    
    departure_time = request.form.get('departure_time')
    departure_time = datetime.strptime(departure_time,"%H:%M").time()
    
    arrival_date = request.form.get('arrival_date')
    arrival_date = datetime.strptime(arrival_date,"%Y-%m-%d")

    arrival_time = request.form.get('arrival_time')
    arrival_time = datetime.strptime(arrival_time,"%H:%M").time()


    flight = Flight(aircraft_id, route_id, departure_date, departure_time, arrival_date, arrival_time)
    db.session.add(flight)
    db.session.commit()

#    for pilot_id in request.form.getlist('pilot_id'):
#      flight_detail = FlightDetail(flight_id=flight_id, pilot_id=pilot_id)
#      db.session.add(flight_detail)
    
    return redirect('/flightDetails/list')


@bp_flights.route('/list')
def list():
  flights = Flight.query.all()
  return render_template("flight_list.html", flights=flights)


@bp_flights.route('/update/<flight_id>', methods=['GET', 'POST'])
def update_flight(flight_id):
  flight = Flight.query.get(flight_id)
  if request.method == 'GET':
    return render_template("flight_update.html", flight=flight)
  if request.method == 'POST':
    aircraft_id = request.form.get('aircraft_id')
    route_id = request.form.get('route_id')

    departure_date = request.form.get('departure_date')
    departure_date = datetime.strptime(departure_date,"%Y-%m-%d")

    departure_time = request.form.get('departure_time')
    departure_time = datetime.strptime(departure_time,"%H:%M").time()

    arrival_date = request.form.get('arrival_date')
    arrival_date = datetime.strptime(arrival_date,"%Y-%m-%d")

    arrival_time = request.form.get('arrival_time')
    arrival_time = datetime.strptime(arrival_time,"%H:%M").time()
    db.session.add(flight)
    db.session.commit()
    return redirect('/flights/list')

@bp_flights.route('/delete/<flight_id>', methods=['GET', 'POST'])
def delete_flight(flight_id):
  flight = Flight.query.get(flight_id)
  if request.method=='GET':
    return render_template("flight_delete.html", flight=flight)
  if request.method=='POST':
    db.session.delete(flight)
    db.session.commit()
    return redirect('/flights/list')
