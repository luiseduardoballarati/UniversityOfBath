from flask import Blueprint
from flask import render_template, request, redirect
from models import Aircraft
from database import db
from datetime import datetime

bp_aircraft = Blueprint("aircrafts", __name__, template_folder="templates/aircrafts")


@bp_aircraft.route("/create", methods=['GET', 'POST'])
def create_aircraft():
  try:
    if request.method == 'GET':
      return render_template("aircraft_create.html")
    if request.method == 'POST':
      manufacturer = request.form.get('manufacturer')
      model = request.form.get('model')
      passenger_capacity = request.form.get('passenger_capacity')
      cruising_range_miles = request.form.get('cruising_range_miles')
  
      aircraft = Aircraft(manufacturer, model, passenger_capacity, cruising_range_miles)
      db.session.add(aircraft)
      db.session.commit()
  
      return redirect('/aircrafts/list')
  except:
      return render_template("menu/error.html")


@bp_aircraft.route('/list')
def list():
  try:
    aircraft = Aircraft.query.all()
    return render_template("aircraft_list.html", aircraft=aircraft)
  except:
    return render_template("menu/error.html")

@bp_aircraft.route('/update/<aircraft_id>', methods=['GET', 'POST'])
def update_aircraft(aircraft_id):
  try:
    aircraft = Aircraft.query.get(aircraft_id)
    if request.method == 'GET':
      return render_template("aircraft_update.html", aircraft=aircraft)
    if request.method == 'POST':
      aircraft.manufacturer = request.form.get('manufacturer')
      aircraft.model = request.form.get('model')
      aircraft.passenger_capacity = request.form.get('passenger_capacity')
      aircraft.cruising_range_miles = request.form.get('cruising_range_miles')
      db.session.add(aircraft)
      db.session.commit()
      return redirect('/aircrafts/list')
  except:
    return render_template("menu/error.html")
    
@bp_aircraft.route('/delete/<aircraft_id>', methods=['GET', 'POST'])
def delete_aircraft(aircraft_id):
  try:
    aircraft = Aircraft.query.get(aircraft_id)
    if request.method=='GET':
      return render_template("aircraft_delete.html", aircraft=aircraft)
    if request.method=='POST':
      db.session.delete(aircraft)
      db.session.commit()
      return redirect('/aircrafts/list')
  except:
    return render_template("menu/error.html")

