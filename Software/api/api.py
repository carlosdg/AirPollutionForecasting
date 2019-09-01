import os
import datetime as dt
import pandas as pd
import simplejson
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from ml import preprocess_data, forecast_model

try:
    connection_string = os.environ["CONNECTION_STRING"]
except:
    connection_string = "postgresql://user:pass@localhost:5432/warehouse_db"

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db = SQLAlchemy(app)
db.reflect()

measures_query = """
    SELECT date, hour, value
    FROM fact_measure fm 
        JOIN dim_date dd
            ON dd.id = fm.date_id
        JOIN dim_time ddu 
            ON ddu.id = fm.time_id
        JOIN dim_measurement_type dmt 
            ON dmt.id = fm.measurement_type_id
        JOIN dim_station ds
            ON ds.id = fm.source_id
    WHERE ds.name = 'TOME CANO'
        AND dmt.short_measure_name = :variable
    ORDER BY date DESC, hour DESC
    LIMIT :limit
    OFFSET :offset
"""

variable_names_query = """
    SELECT DISTINCT dmt.short_measure_name as names
    FROM fact_measure fm 
        JOIN dim_measurement_type dmt 
            ON dmt.id = fm.measurement_type_id
        JOIN dim_station ds
            ON ds.id = fm.source_id
    WHERE ds.name = 'TOME CANO'
    GROUP BY names
"""

forecast_input_query = """
    SELECT date,
        hour,
        name,
        short_measure_name,
        value
    FROM fact_measure fm
        JOIN dim_date dd ON fm.date_id = dd.id
        JOIN dim_time dt ON fm.time_id = dt.id
        JOIN dim_station ds ON fm.source_id = ds.id
        JOIN dim_measurement_type dmt ON fm.measurement_type_id = dmt.id
    WHERE name = 'TOME CANO'
      AND (date + hour * '1 hour'::interval) >= (%(timestamp)s - interval '24 hour')
      AND (date + hour * '1 hour'::interval) <= (%(timestamp)s - interval '1 hour')
    ORDER BY name, date, hour
"""


@app.route('/apf/api/v1.0/meta', methods=['GET'])
def get_meta():
    names = db.session.execute(variable_names_query)
    names = [row[0] for row in names]

    return jsonify({ 'measure_names': names })


@app.route('/apf/api/v1.0/measures/<string:variable>/<string:last>/<string:offset>', methods=['GET'])
def get_measures(variable, last, offset):
    parameters = {
        'variable': variable,
        'limit': last,
        'offset': offset
    }
    results = db.session.execute(measures_query, parameters)
    output = [{
        'date': str(dt.datetime.combine(date=row[0], time=dt.time(hour=row[1]))),
        'value': float(row[2])
    } for row in results]

    return simplejson.dumps(output, ignore_nan=True)


@app.route('/apf/api/v1.0/forecast/24/<string:timestamp>', methods=['GET'])
def get_forecast(timestamp):
    # Fixme: if we don't have the previous 24h of the asked date to forecast it
    # throws a huge error

    timestamp = dt.datetime.strptime(timestamp, '%Y-%m-%d_%H')
    data = pd.read_sql(forecast_input_query,
                       con=db.engine,
                       params={'timestamp': timestamp})
    X = preprocess_data(data)
    y_preds = forecast_model.predict(X)

    return jsonify({'pred': y_preds[0]})


if __name__ == '__main__':
    app.run(debug=True)
