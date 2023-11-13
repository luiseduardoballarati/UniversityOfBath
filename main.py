from flask import Flask
from database import db
from flask_migrate import Migrate
from pilots import bp_pilots
from flask import redirect
from aircraft import bp_aircraft
from airports import bp_airports
from route import bp_routes
from flights import bp_flights
from flight_details import bp_flightDetails
from menu import bp_menu


app = Flask(__name__)

# Name of the database (using sqlite)
connection = 'sqlite:///flights.sqlite'
# Database password - would be used for criptograhy"
app.config['SECRET_KEY'] = 'password321'
# Database URL
app.config['SQLALCHEMY_DATABASE_URI'] = connection
# To not be tracked all the time
app.config['SQLAlCHEMY_TRACKMODIFICATIONS'] = False 
# To use 'https' protocol, much more safe
app.config['PREFERRED_URL_SCHEME'] = 'https'  

app.config['STATIC_FOLDER'] = 'static'

# Calling my database
db.init_app(app)

# Associating our app with our database
migrate = Migrate(app, db)

app.register_blueprint(bp_pilots, url_prefix='/pilots')
app.register_blueprint(bp_aircraft, url_prefix='/aircrafts')
app.register_blueprint(bp_airports, url_prefix='/airports')
app.register_blueprint(bp_routes, url_prefix='/routes')
app.register_blueprint(bp_flights, url_prefix='/flights')
app.register_blueprint(bp_flightDetails, url_prefix='/flightDetails')
app.register_blueprint(bp_menu, url_prefix='/menu')

@app.route('/')
def index():
    return redirect('/menu/menu')


app.run(host='0.0.0.0', port=8080)
