from flask import Blueprint
from flask import render_template, request, redirect
from models import FlightDetail
from database import db
from datetime import datetime

bp_flightDetails = Blueprint("flight_details", __name__, template_folder="templates/flight_details")
    
@bp_flightDetails.route('/list')
def list():
  try:
    flight_details = FlightDetail.query.all()
    return render_template("flight_detail_list.html", flight_details=flight_details)
  except:
   return render_template("menu/error.html")

"""
# Used this for tests
@bp_flightDetails.route("/create", methods=['GET', 'POST'])
def create_flightDetails():
  try:
    if request.method == 'GET':
      return render_template("flight_detail_create.html")
    if request.method == 'POST':
      flight_id = request.form.get('flight_id')
      pilot_id = request.form.get('pilot_id')
  
      flightDetail = FlightDetail(flight_id=flight_id, pilot_id=pilot_id)
      db.session.add(flightDetail)
      db.session.commit()
  
      return redirect('/flightDetails/list')
  except:
   return render_template("menu/error.html")
"""
@bp_flightDetails.route('/delete/<flight_detail_id>', methods=['GET', 'POST'])
def delete_flightDetail(flight_detail_id):
  try:
    flight_detail = FlightDetail.query.get(flight_detail_id)
    if request.method=='GET':
      return render_template("flightDetail_delete.html", flight_detail=flight_detail)
    if request.method=='POST':
      db.session.delete(flight_detail)
      db.session.commit()
      return redirect('/flightDetails/list')
  except:
   return render_template("menu/error.html")
"""
@bp_flightDetails.route('/update/<flight_detail_id>', methods=['GET', 'POST'])
def update_flightDetail(flight_detail_id):
  try:
    flight_detail = FlightDetail.query.get(flight_detail_id)
  
    if request.method == 'GET':
      return render_template("flightDetail_update.html", flight_detail=flight_detail)
    if request.method == 'POST':
      flight_detail.flight_id = request.form.get('flight_id')
      flight_detail.pilot_id = request.form.get('pilot_id')
  
      db.session.add(flightDetail)
      db.session.commit()
      return redirect('/flightDetail/list')
  except:
   return render_template("menu/error.html")
   """