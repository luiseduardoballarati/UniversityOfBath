from flask import Blueprint
from flask import render_template, request, redirect
from models import Flight
from models import FlightDetail
from database import db
from datetime import datetime
from models import Pilot
from models import Aircraft
from models import Route

bp_flights = Blueprint("flights", __name__, template_folder="templates/flights")

@bp_flights.route("/create", methods=['GET', 'POST'])
def create_flight():
  try:
    
    if request.method == 'GET':
      return render_template("flight_create.html")
    if request.method == 'POST':

      aircraft_id = request.form.get('aircraft_id')
      route_id = request.form.get('route_id')

      aircraft_id = int(aircraft_id)
      route_id = int(route_id)

      valid_aircraft_ids = [row[0] for row in db.session.query(Aircraft.aircraft_id).all()]
      valid_route_ids = [row[0] for row in db.session.query(Route.route_id).all()]

      
      if aircraft_id not in valid_aircraft_ids:
            return render_template("error.html", message="Invalid aircraft ID")
    
      if route_id not in valid_route_ids:
          return render_template("error.html", message="Invalid route ID")

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
      return redirect('/flights/list')
  except:
    return render_template("menu/error.html")


@bp_flights.route('/list')
def list():
  try:
    flights = Flight.query.all()
    flightDetails = FlightDetail.query.all()
    return render_template("flight_list.html", flights=flights, flightDetails=flightDetails)
  except:
   return render_template("menu/error.html")
  
@bp_flights.route('/update/<flight_id>', methods=['GET', 'POST'])
def update_flight(flight_id):
  try:
  
    flight = Flight.query.get(flight_id)
    flightDetail = FlightDetail
    
    if request.method == 'GET':
      return render_template("flight_update.html", flight=flight)
      
    if request.method == 'POST':

      #aircraft_ids = Aircraft.query(Aircraft.aircraft_id).all()
      #routes_ids = Route.query(Route.route_id).all()

      aircraft_id = request.form.get('aircraft_id')
      route_id = request.form.get('route_id')
      
      aircraft_id = int(aircraft_id)
      route_id = int(route_id)

      valid_aircraft_ids = [row[0] for row in db.session.query(Aircraft.aircraft_id).all()]
      valid_route_ids = [row[0] for row in db.session.query(Route.route_id).all()]


      if aircraft_id not in valid_aircraft_ids:
            return render_template("error.html", message="Invalid aircraft ID")

      if route_id not in valid_route_ids:
          return render_template("error.html", message="Invalid route ID")

      flight.aircraft_id = aircraft_id
      flight.route_id = route_id

      flight.departure_date = request.form.get('departure_date')
      flight.departure_date = datetime.strptime(flight.departure_date,"%Y-%m-%d")
  
      flight.departure_time = request.form.get('departure_time')
      flight.departure_time = datetime.strptime(flight.departure_time,"%H:%M").time()
  
      flight.arrival_date = request.form.get('arrival_date')
      flight.arrival_date = datetime.strptime(flight.arrival_date,"%Y-%m-%d")
  
      flight.arrival_time = request.form.get('arrival_time')
      flight.arrival_time = datetime.strptime(flight.arrival_time,"%H:%M").time()
  
      pilots_available = [row[0] for row in db.session.query(Pilot.pilot_id).all()]

      pilot_ids = request.form.getlist('pilot_ids')
      pilot_ids = pilot_ids.pop(-1)
      pilot_ids = [int(x) for x in pilot_ids if x.isnumeric()]
      
      for pilot_id in pilot_ids:
        if pilot_id not in pilots_available:
          return render_template("error.html",message="Invalid Pilot ID")
        else:
          flightDetail = FlightDetail(flight_id=flight.flight_id, pilot_id=pilot_id)
          db.session.add(flightDetail)
      
      #db.session.add(flightDetail)
      db.session.add(flight)
      db.session.commit()
      return redirect('/flights/list')
  except:
   return render_template("menu/error.html")
    
@bp_flights.route('/pilots_assigned/<flight_id>', methods=['GET'])
def pilots_assigned(flight_id):
  #try:
    message = ""
    flight = Flight.query.get(flight_id)
    pilots_assigned = db.session.query(FlightDetail.pilot_id).filter(FlightDetail.flight_id == flight_id).all()
    empty_return = len(pilots_assigned)
    selected_pilots = []
    if empty_return == 0:
      message = "No pilots assigned yet!"
    else:
      for row in pilots_assigned:
        infos = db.session.query(Pilot.pilot_id, Pilot.first_name, Pilot.last_name).filter(Pilot.pilot_id.in_(row)).all()
        selected_pilots.append(infos)

    return render_template("pilots_assigned.html", pilots_assigned=pilots_assigned, flight=flight, message=message, selected_pilots=selected_pilots)
  #except:
   #return render_template("menu/error.html")

@bp_flights.route('/delete/<flight_id>', methods=['GET', 'POST'])
def delete_flight(flight_id):
  message = "You cant delete this flight! First you need to delete its Flight Details!"
  try:
    flight = Flight.query.get(flight_id)
    if request.method=='GET':
      return render_template("flight_delete.html", flight=flight)
    if request.method=='POST':
      db.session.delete(flight)
      db.session.commit()
      return redirect('/flights/list')
  except:
   return render_template("menu/error.html", message=message)
