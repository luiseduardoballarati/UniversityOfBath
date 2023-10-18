from flask import Blueprint
from flask import render_template, request, redirect
from models import Route
from database import db
from datetime import datetime

bp_routes = Blueprint("routes", __name__, template_folder="templates/routes")


@bp_routes.route("/create", methods=['GET', 'POST'])
def create_route():
  if request.method == 'GET':
    return render_template("route_create.html")
  if request.method == 'POST':
    departure_airport_id = request.form.get('departure_airport_id')
    arrival_airport_id = request.form.get('arrival_airport_id')

    route = Route(departure_airport_id, arrival_airport_id)
    db.session.add(route)
    db.session.commit()

    return redirect('/routes/list')


@bp_routes.route('/list')
def list():
  route = Route.query.all()
  return render_template("route_list.html", route=route)


@bp_routes.route('/update/<route_id>', methods=['GET', 'POST'])
def update_route(route_id):
  route = Route.query.get(route_id)
  if request.method == 'GET':
    return render_template("route_update.html", route=route)
  if request.method == 'POST':
    route.departure_airport_id = request.form.get('departure_airport_id')
    route.arrival_airport_id = request.form.get('arrival_airport_id')
    db.session.add(route)
    db.session.commit()
    return redirect('/routes/list')

@bp_routes.route('/delete/<route_id>', methods=['GET', 'POST'])
def delete_pilot(route_id):
  route = Route.query.get(route_id)
  if request.method=='GET':
    return render_template("route_delete.html", route=route)
  if request.method=='POST':
    db.session.delete(route)
    db.session.commit()
    return redirect('/routes/list')


