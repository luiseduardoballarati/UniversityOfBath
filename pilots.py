from flask import Blueprint
from flask import render_template, request, redirect
from models import Pilot
from database import db
from datetime import datetime

bp_pilots = Blueprint("pilots", __name__, template_folder="templates/pilots")


@bp_pilots.route("/create", methods=['GET', 'POST'])
def create_pilot():
  if request.method == 'GET':
    return render_template("pilot_create.html")
  if request.method == 'POST':
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    born_date = request.form.get('born_date')
    born_date = datetime.strptime(born_date,"%Y-%m-%d")
    flown_hours = request.form.get('flown_hours')

    u = Pilot(first_name, last_name, born_date, flown_hours)
    db.session.add(u)
    db.session.commit()

    return redirect('/pilots/list')


@bp_pilots.route('/list')
def list():
  pilots = Pilot.query.all()
  return render_template("pilot_list.html", pilots=pilots)


@bp_pilots.route('/update/<pilot_id>', methods=['GET', 'POST'])
def update_pilot(pilot_id):
  pilot = Pilot.query.get(pilot_id)
  if request.method == 'GET':
    return render_template("pilot_update.html", pilot=pilot)
  if request.method == 'POST':
    pilot.first_name = request.form.get('first_name')
    pilot.last_name = request.form.get('last_name')
    pilot.born_date = request.form.get('born_date')
    pilot.born_date = datetime.strptime(pilot.born_date,"%Y-%m-%d")
    pilot.flown_hours = request.form.get('flown_hours')
    db.session.add(pilot)
    db.session.commit()
    return redirect('/pilots/list')

@bp_pilots.route('/delete/<pilot_id>', methods=['GET', 'POST'])
def delete_pilot(pilot_id):
  pilot = Pilot.query.get(pilot_id)
  if request.method=='GET':
    return render_template("pilot_delete.html", pilot=pilot)
  if request.method=='POST':
    db.session.delete(pilot)
    db.session.commit()
    return redirect('/pilots/list')


    