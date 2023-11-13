from flask import Blueprint
from flask import render_template, request, redirect
from models import Route
from database import db
from datetime import datetime
from models import Airport

bp_routes = Blueprint("routes", __name__, template_folder="templates/routes")


@bp_routes.route("/create", methods=['GET', 'POST'])
def create_route():
  try:
    if request.method == 'GET':
      return render_template("route_create.html")
    if request.method == 'POST':
      
      airports_available = [row[0] for row in db.session.query(Airport.airport_id).all()]
      
      departure_airport_id = request.form.get('departure_airport_id')
      arrival_airport_id = request.form.get('arrival_airport_id')
      departure_airport_id = int(departure_airport_id)
      arrival_airport_id = int(arrival_airport_id)
      
      if departure_airport_id not in airports_available:
        return render_template("error.html", message="Invalid Route ID")
      if arrival_airport_id not in airports_available:
       return render_template("error.html", message="Invalid Route ID")
  
      route = Route(departure_airport_id, arrival_airport_id)
      db.session.add(route)
      db.session.commit()
  
      return redirect('/routes/list')
  except:
    return render_template('/menu/error.html')
  

@bp_routes.route('/list')
def list():
  try:
    route = Route.query.all()
    airport_names = {airport.airport_id: airport.airport_name for airport in Airport.query.all()}
    return render_template("route_list.html", route=route, airport_names=airport_names)
  except:
    return render_template("menu/error.html")

@bp_routes.route('/update/<route_id>', methods=['GET', 'POST'])
def update_route(route_id):
  try:
    route = Route.query.get(route_id)
    if request.method == 'GET':
      return render_template("route_update.html", route=route)
      
    if request.method == 'POST':

      airports_available = [row[0] for row in db.session.query(Airport.airport_id).all()]
  
      departure_airport_id = request.form.get('departure_airport_id')
      arrival_airport_id = request.form.get('arrival_airport_id')
      departure_airport_id = int(departure_airport_id)
      arrival_airport_id = int(arrival_airport_id)
  
    if departure_airport_id not in airports_available:
      return render_template("error.html", message="Invalid Route ID")
    if arrival_airport_id not in airports_available:
      return render_template("error.html", message="Invalid Route ID")
  
    route.departure_airport_id = departure_airport_id
    route.arrival_airport_id = arrival_airport_id
          
    db.session.add(route)
    db.session.commit()
    return redirect('/routes/list')
  except:
    return render_template("menu/error.html")
    
@bp_routes.route('/delete/<route_id>', methods=['GET', 'POST'])
def delete_pilot(route_id):
  try:
    route = Route.query.get(route_id)
    if request.method=='GET':
      return render_template("route_delete.html", route=route)
    if request.method=='POST':
      db.session.delete(route)
      db.session.commit()
      return redirect('/routes/list')
  except:
    return render_template("menu/error.html")


