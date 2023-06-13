import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
db_path = "Resources/hawaii.sqlite"
engine = create_engine(f"sqlite:///{db_path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dictionary of date keys with precipitation values for only the last 12 months"""
    # Query precipitation
    previous_year = dt.date(2017,8,23)-dt.timedelta(days=365)
    precipitation_date = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > previous_year).all()
    
    results = {date :prcp for date,prcp in precipitation_date}

    session.close()

    # Return the JSON representation of dictionary
    return jsonify(results)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all stations
    stations = session.query(Station.station).all()
    results = list(np.ravel(stations))
    session.close()
    
    # Return list as JSON 
    return jsonify(results)

@app.route("/api/v1.0/temp/<start>")
def temp(start=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    station_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date>=start).all()
    
    results = list(np.ravel(station_temp))

    session.close()

    # Return the JSON representation of dictionary
    return jsonify(results)

@app.route("/api/v1.0/temp/<start>/<end>")
def temp_end(start=None,end=None):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    station_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    
    results = list(np.ravel(station_temp))

    session.close()

    # Return the JSON representation of dictionary
    return jsonify(results)





if __name__ == '__main__':
    app.run(debug=True)
