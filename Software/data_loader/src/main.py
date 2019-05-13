from models import (DimDate, DimDuration, DimMeasurementType, DimStation,
                    DimTime, FactMeasure, Session)
from parse import read_month_csvs


def insert_month_data_to_warehouse(data_path):
    """
        TODO: 
            - Do the same for PM2.5, O3, SO2 & NO2
            - Take the station name from the folder name
            - Define a function that returns the duration_hours based on the
            station
    """
    data_frame = read_month_csvs(data_path)
    session = Session()

    for series_name, series in data_frame.items():
        if 'PM10' in series_name:
            for date, value in series.iteritems():
                date_row = session.query(DimDate).filter_by(date=date).first()
                hour_row = session.query(DimTime).filter_by(
                    hour=date.hour).first()
                duration_row = session.query(
                    DimDuration).filter_by(duration_hours=1).first()
                station_row = session.query(
                    DimStation).filter_by(name="TOME CANO").first()
                measurement_type_row = session.query(
                    DimMeasurementType).filter_by(short_measure_name="PM10").first()

                fact_row = FactMeasure(
                    date_id=date_row.id,
                    time_id=hour_row.id,
                    duration_id=duration_row.id,
                    source_id=station_row.id,
                    measurement_type_id=measurement_type_row.id,
                    value=value
                )

                session.add(fact_row)
                session.commit()


if __name__ == "__main__":
    path = './Software/pollution_data_downloader/downloads/tome_cano/2019_01'
    insert_month_data_to_warehouse(path)
