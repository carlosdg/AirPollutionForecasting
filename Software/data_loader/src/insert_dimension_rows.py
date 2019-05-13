import datetime as dt

from models import (DimDate, DimDuration, DimMeasurementType, DimStation,
                    DimTime, Session)


def daterange(start_date, end_date):
    """Iterator through a range of dates, day by day

    Arguments:
        start_date {dt.datetime} -- Start date (included)
        end_date {dt.datetime} -- End date (not included)
    """
    date_diff = end_date - start_date
    days_diff = int(date_diff.days)

    for i in range(days_diff):
        yield start_date + dt.timedelta(i)


def _get_date_rows():
    start_date = dt.datetime(2015, 1, 1)
    end_date = dt.datetime(2019, 3, 1)
    return [DimDate(date) for date in daterange(start_date, end_date)]


def _get_time_rows():
    return [DimTime(i) for i in range(0, 24)]


def _get_duration_rows():
    return [
        DimDuration(1),
        DimDuration(24)
    ]


def _get_measurement_type_rows():
    return [
        DimMeasurementType(
            'TMIN', 'MINIMUM TEMPERATURE', 'CELSIUS DEGREES'),
        DimMeasurementType('TMINHOUR', 'HOUR OF MINIMUM TEMPERATURE', 'h'),
        DimMeasurementType(
            'TMAX', 'MAXIMUM TEMPERATURE', 'CELSIUS DEGREES'),
        DimMeasurementType('TMAXHOUR', 'HOUR OF MAXIMUM TEMPERATURE', 'h'),
        DimMeasurementType('WSMAX', 'MAXIMUM WIND SPEED', 'm/s'),
        DimMeasurementType(
            'WSMAXDIR', 'DIRECTION OF MAXIMUM WIND SPEED', 'DEGREES'),
        DimMeasurementType('WSMAXHOUR', 'HOUR OF MAXIMUM WIND SPEED', 'h'),
        DimMeasurementType('SUN', 'HOURS OF SUN', 'h'),
        DimMeasurementType('PMIN', 'MINIMUM PRESSURE', 'mb'),
        DimMeasurementType('PMINHOUR', 'HOUR OF MINIMUM PRESSURE', 'h'),
        DimMeasurementType('PMAX', 'MAXIMUM PRESSURE', 'mb'),
        DimMeasurementType('PMAXHOUR', 'HOUR OF MAXIMUM PRESSURE', 'h'),
        DimMeasurementType('T', 'TEMPERATURE', 'CELSIUS DEGREES'),
        DimMeasurementType('P', 'ATMOSPHERIC PRESSURE', 'mb'),
        DimMeasurementType('WD', 'WIND DIRECTION', 'DEGREES'),
        DimMeasurementType('WS', 'WIND SPEED', 'm/s'),
        DimMeasurementType('RH', 'RELATIVE HUMIDITY', '%'),
        DimMeasurementType('PP', 'PRECIPITATION', 'l/m2'),
        DimMeasurementType('SR', 'SOLAR RADIATION', 'W/m2'),
        DimMeasurementType(
            'PM10', 'PARTICULATE MATTER LESS THAN 10 MICROMETERS', 'µg/m3'),
        DimMeasurementType(
            'PM2.5', 'PARTICULATE MATTER LESS THAN 2.5 MICROMETERS', 'µg/m3'),
        DimMeasurementType(
            'PM1', 'PARTICULATE MATTER LESS THAN 1 MICROMETER', 'µg/m3'),
        DimMeasurementType('O3', 'OZONE', 'µg/m3'),
        DimMeasurementType('CO', 'CARBON MONOXIDE', 'mg/m3'),
        DimMeasurementType('H2S', 'HYDROGEN SULFIDE', 'µg/m3'),
        DimMeasurementType('NO', 'NITROGEN MONOXIDE', 'µg/m3'),
        DimMeasurementType('NO2', 'NITROGEN DIOXIDE', 'µg/m3'),
        DimMeasurementType('NOX', 'NITROGEN OXIDES', 'µg/m3'),
        DimMeasurementType('SH2', 'HYDROGEN SULFIDE', 'µg/m3'),
        DimMeasurementType('SO2', 'SULFUR DIOXIDE', 'µg/m3'),
        DimMeasurementType('TRS', 'TOTAL REDUCED SULPHUR', 'µg/m3'),
        DimMeasurementType('BC', 'BLACK CARBON', 'µg/m3'),
        DimMeasurementType('BEN', 'BENCENE', 'µg/m3'),
        DimMeasurementType('TOL', 'TOLUENE', 'µg/m3'),
        DimMeasurementType('XIL', 'XYLENE', 'µg/m3'),
        DimMeasurementType('M-P XIL', 'M-P XYLENE', 'µg/m3')

    ]


def _get_station_rows():
    return [
        DimStation('CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA',
                   'CASA CUNA', -16.27769219311504, 28.45103088037192, 0),
        DimStation('CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA',
                   'DEPOSITO DE TRISTAN', -16.27877561502283, 28.45815968532356, 0),
        DimStation('CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA',
                   'GARCIA ESCAMEZ', -16.27184954317193, 28.45664139423877, 0),
        DimStation('CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA',
                   'PARQUE LA GRANJA', -16.26487493264499, 28.46300210751911, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'TOME CANO', -16.26186591001509, 28.4621688991889, 0),
        DimStation('CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA',
                   'VUELTA LOS PAJAROS', -16.27697222222222, 28.462, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'PISCINA MUNICIPAL', -16.26340423894506, 28.45791579546199, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'TENA ARTIGAS', -16.27685561780176, 28.45537560999706, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'TIO PINO', -16.27012462756456, 28.45925503570103, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'PALMETUM', -16.25852644443512, 28.452545726989584, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'COMANDANCIA', -16.2456057616887, 28.47720124167907, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'HACIENDA', -16.24870801361327, 28.46323011938556, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'BOMBEROS', -16.26097493125278, 28.45828864775618, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA',
                   'COMISARIA', -16.25866186061195, 28.45912395381277, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN',
                   'SANTA CRUZ - LA LAGUNA', 'LOS GLADIOLOS', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN',
                   'SANTA CRUZ - LA LAGUNA', 'MERCATENERIFE', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA',
                   'PUERTA LITORAL - REFINERIA', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA',
                   'PUERTA PRINCIPAL - REFINERIA', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN',
                   'SANTA CRUZ - LA LAGUNA', 'REFINERIA', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA',
                   'REFINERIA - TORRE METEOROLOGICA', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN',
                   'SANTA CRUZ - LA LAGUNA', 'VIEJA Y CLAVIJO', 0, 0, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'TENERIFE NORTH',
                   'LA ZAMORA', -16.57072474718117, 28.3831334121515, 0),
        DimStation('CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'TENERIFE SOUTH',
                   'LA HIDALGA - ARAFO', -16.39991556602504, 28.33734903726858, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'BARRANCO HONDO', -16.3581166775973, 28.39342430257058, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'LA BUZANADA', -16.65275205038472, 28.07264560673482, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'CALETILLAS', -16.36193673089008, 28.37672185381682, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'LA GUANCHA - CANDELARIA', -16.36833427699988, 28.38016131594777, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'EL RIO', -16.52369883375512, 28.14507452830099, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'LAS GALLETAS', -16.65582224157534, 28.00778986209971, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'GRANADILLA', -16.57757403405965, 28.11249291171923, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'IGUESTE', -16.37197069941999, 28.38054612249282, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'EL MEDANO', -16.53603007019015, 28.04732410738179, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'SAN ISIDRO', -16.55983699771885, 28.08003389965855, 0),
        DimStation('CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH',
                   'SAN MIGUEL DE TAJAO', -16.47161086862779, 28.11139253073869, 0),
        DimStation('CANARY GOVERNMENT', 'UNKNOWN', 'TENERIFE SOUTH',
                   'TORRE METEOROLOGICA DE CANDELARIA', 0, 0, 0),
        DimStation('AEMET', 'AEMET', 'SANTA CRUZ - LA LAGUNA',
                   'SANTA CRUZ DE TENERIFE', 28.46333333, -16.25527778, 35),
        DimStation('AEMET', 'AEMET', 'TENERIFE NORTH',
                   'AEROPUERTO NORTE', 28.4775, -16.329444444444444, 632),
        DimStation('AEMET', 'AEMET', 'TENERIFE SOUTH', 'AEROPUERTO SUR',
                   28.047500000000003, -16.560833333333335, 64),
        DimStation('AEMET', 'AEMET', 'TENERIFE SOUTH', 'IZANA',
                   28.30888888888889, -16.499444444444446, 2371),
        DimStation('AEMET', 'AEMET', 'TENERIFE SOUTH', 'GUIMAR',
                   28.31833333333333, -16.38222222222222, 115),
        DimStation('AEMET', 'AEMET', 'TENERIFE NORTH', 'PUERTO DE LA CRUZ',
                   28.418055555555558, -16.548055555555557, 25)

    ]


def insert_dimension_defaults(session):
    """Inserts into a database all default values for the dimension tables

    Arguments:
        session {} -- sqlalchemy session
    """
    row_collection = [
        _get_date_rows(),
        _get_time_rows(),
        _get_duration_rows(),
        _get_measurement_type_rows(),
        _get_station_rows()
    ]

    for rows in row_collection:
        try:
            session.add_all(rows)
            session.commit()
        except:
            session.rollback()


if __name__ == "__main__":
    session = Session()
    insert_dimension_defaults(session)
