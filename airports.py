from flask import Blueprint
from flask import render_template, request, redirect
from models import Airport
from database import db
from datetime import datetime

bp_airports = Blueprint("airports", __name__, template_folder="templates/airports")


@bp_airports.route("/create", methods=['GET', 'POST'])
def create_airport():
  if request.method == 'GET':
    return render_template("airport_create.html")
  if request.method == 'POST':
    airport_name = request.form.get('airport_name')
    city = request.form.get('city')
    country = request.form.get('country')

    airport = Airport(airport_name, city, country)
    db.session.add(airport)
    db.session.commit()

    return redirect('/airports/list')


@bp_airports.route('/list')
def list():
  airport = Airport.query.all()
  return render_template("airport_list.html", airport=airport)


@bp_airports.route('/update/<airport_id>', methods=['GET', 'POST'])
def update_airport(airport_id):
  airport = Airport.query.get(airport_id)
  if request.method == 'GET':
    return render_template("airport_update.html", airport=airport)
  if request.method == 'POST':
    airport.airport_name = request.form.get('airport_name')
    airport.city = request.form.get('city')
    airport.country = request.form.get('country')
    db.session.add(airport)
    db.session.commit()
    return redirect('/airports/list')

@bp_airports.route('/delete/<airport_id>', methods=['GET', 'POST'])
def delete_airport(airport_id):
  airport = Airport.query.get(airport_id)
  if request.method=='GET':
    return render_template("airport_delete.html", airport=airport)
  if request.method=='POST':
    db.session.delete(airport)
    db.session.commit()
    return redirect('/airports/list')


