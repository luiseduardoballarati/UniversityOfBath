from flask import Blueprint
from flask import render_template, request, redirect
from models import FlightDetail
from database import db
from datetime import datetime

bp_flightDetails = Blueprint("flight_details", __name__, template_folder="templates/flight_details")
    
@bp_flightDetails.route('/list')
def list():
  flight_details = FlightDetail.query.all()
  return render_template("flight_detail_list.html", flight_details=flight_details)
