from models import (DimDate, DimDuration, DimMeasurementType, DimStation,
                    DimTime, FactMeasure, Session)
from parse import read_month_csvs
from insert_dimension_rows import insert_dimension_defaults


def query(session, Dim, **kwargs):
    """Helper function that returns the first row from the given 
    dimension table given the keyword arg restrictions

    Arguments:
        session {} -- SQLAlchemy session
        Dim {} -- SQLAlchemy class representing a dimension table

    Returns:
        object -- First row in the table that fulfills the given
        restrictions
    """
    return session.query(Dim).filter_by(**kwargs).first()


def create_row(session, datetime, value, duration_hours, name, short_measure_name):
    """Creates a row to the fact table representing a measure taken

    Arguments:
        session {} -- SQLAlchemy session
        datetime {datetime.datetime} -- Start date of the measure
        value {float} -- Measure value
        duration_hours {int} -- Duration hours
        name {str} -- Station name
        short_measure_name {str} -- Measure name

    Returns:
        object -- Fact table row created
    """
    date_row = query(session, DimDate, date=datetime.date())
    hour_row = query(session, DimTime, hour=datetime.hour)
    duration_row = query(session, DimDuration, duration_hours=duration_hours)
    station_row = query(session, DimStation, name=name)
    measurement_type_row = query(
        session, DimMeasurementType, short_measure_name=short_measure_name)

    fact_row = FactMeasure(
        date_id=date_row.id,
        time_id=hour_row.id,
        duration_id=duration_row.id,
        source_id=station_row.id,
        measurement_type_id=measurement_type_row.id,
        value=value
    )

    return fact_row


def extract_measure_name(column_name):
    """Returns the short measurement name that the given column name represents

    This is needed because the column name can be different than just the
    measurement name, it can include the station name for example. If no
    appropriate measure name if found an empty string will be returned instead

    Arguments: column_name {str} -- Column name where to extract the measurement
    name from

    Returns: str -- Name of the measurement that the given column represents or
    an empty string if no measure could be found
    """
    column_name = column_name.upper()

    # Pollution data
    if ' PM10 ' in column_name:
        return "PM10"
    elif ' PM2.5 ' in column_name or ' PM2,5 ' in column_name:
        return "PM2.5"
    elif ' O3 ' in column_name:
        return "O3"
    elif ' SO2 ' in column_name:
        return "SO2"
    elif ' NO2 ' in column_name:
        return "NO2"

    # Weather data (wind speed & direction, relative humidity, precipitation,
    # pressure, temperature and solar radiation)
    elif ' VV ' in column_name:
        return 'WS'
    elif ' DD ' in column_name:
        return 'WD'
    elif ' HR ' in column_name:
        return 'RH'
    elif ' LL ' in column_name:
        return 'PP'
    elif ' PRB ' in column_name:
        return 'P'
    elif ' TMP ' in column_name:
        return 'T'
    elif ' RS ' in column_name:
        return 'SR'
    else:
        return ""


def insert_data(session, data_frame, station_name, measure_duration):
    """Inserts the data of the given data frame to the warehose 

    Arguments:
        session {} -- SQLAlchemy session connected to the data warehouse
        data_frame {} -- Pandas' data frame with the data to store
        station_name {str} -- Name of the station where the given data was
        retrieved
        measure_duration {int} -- Number of hours that the measure took (e.g.
        1h or 24h)
    """
    for series_name, series in data_frame.items():
        measure_name = extract_measure_name(series_name)
        if measure_name != "":
            for date, value in series.iteritems():
                fact_row = create_row(session, date, value, measure_duration,
                                      station_name, measure_name)
                session.add(fact_row)

            session.commit()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        raise RuntimeError("""
            USAGE: python insert_data.py <path_to_data> <station_name> <measure_duration>
            e.g: python insert_data.py tome_cano/2019_01 "TOME CANO" 1
        """)

    [path, station_name, measure_duration] = sys.argv[1:]

    print(f"""
        Path to the month data: {path}
        Station name: {station_name}
        Measure duration: {measure_duration}
    """)

    data_frame = read_month_csvs(path)
    session = Session()

    insert_dimension_defaults(session)
    insert_data(session, data_frame, station_name, measure_duration)
