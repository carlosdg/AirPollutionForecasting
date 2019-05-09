from sqlalchemy import create_engine, Column, Integer, Numeric, Boolean, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_holiday_name(date):
    """Returns the holiday name of the given date or "NO HOLIDAY"

    Arguments: date {Date} -- Date to get the holiday name

    Returns: str -- Holiday name or "NO HOLIDAY" if the given date isn't a
        holiday
    """
    year = date.year
    month = date.month
    day = date.day

    result = "NOT HOLIDAY"

    if month == 1 and day == 1:
        result = "NEW YEAR"
    elif month == 1 and day == 6:
        result = "EPIPHANY"
    elif month == 5 and day == 1:
        result = "LABOR DAY"
    elif month == 5 and day == 30:
        result = "DAY OF THE CANARY ISLANDS"
    elif month == 8 and day == 15:
        result = "ASSUMPTION OF MARY"
    elif month == 10 and day == 12:
        result = "HISPANIC DAY"
    elif month == 11 and day == 1:
        result = "ALL SAINTS"
    elif month == 12 and day == 6:
        result = "CONSTITUTION DAY"
    elif month == 12 and day == 8:
        result = "IMMACULATE CONCEPTION"
    elif month == 12 and day == 25:
        result = "CHRISTMAS DAY"

    elif year == 2015 and month == 2 and day == 17:
        result = "(CARNIVAL) SHROVE TUESDAY"
    elif year == 2015 and month == 4 and day == 2:
        result = "(HOLY WEEK) MAUNDY THURSDAY"
    elif year == 2015 and month == 4 and day == 3:
        result = "(HOLY WEEK) GOOD FRIDAY"

    elif year == 2016 and month == 2 and day == 9:
        result = "(CARNIVAL) SHROVE TUESDAY"
    elif year == 2016 and month == 3 and day == 24:
        result = "(HOLY WEEK) MAUNDY THURSDAY"
    elif year == 2016 and month == 3 and day == 25:
        result = "(HOLY WEEK) GOOD FRIDAY"

    elif year == 2017 and month == 2 and day == 28:
        result = "(CARNIVAL) SHROVE TUESDAY"
    elif year == 2017 and month == 4 and day == 13:
        result = "(HOLY WEEK) MAUNDY THURSDAY"
    elif year == 2017 and month == 4 and day == 14:
        result = "(HOLY WEEK) GOOD FRIDAY"

    elif year == 2018 and month == 2 and day == 13:
        result = "(CARNIVAL) SHROVE TUESDAY"
    elif year == 2018 and month == 3 and day == 29:
        result = "(HOLY WEEK) MAUNDY THURSDAY"
    elif year == 2018 and month == 3 and day == 30:
        result = "(HOLY WEEK) GOOD FRIDAY"

    elif year == 2019 and month == 3 and day == 5:
        result = "(CARNIVAL) SHROVE TUESDAY"
    elif year == 2019 and month == 4 and day == 18:
        result = "(HOLY WEEK) MAUNDY THURSDAY"
    elif year == 2019 and month == 4 and day == 19:
        result = "(HOLY WEEK) GOOD FRIDAY"

    return result


class DimDate(Base):
    """Date dimension table

    This table represent a date dimension table in a star schema

    Attributes:
        __tablename__: str
           Name of the generated Table in the database
        id: Column
            Unique, autogenerated identifier for each row
        date: Column
            Date object with all the date information
        year: Column
            Date's year
        month: Column
            Date's month
        day: Column
            Date's day
        day_of_week: Column
            Date's day of week. Monday to Sunday represented by numbers from 0 to 6
        day_of_year: Column
            Date's day of the year. Number from 1 to 365 or 366
        is_tenerife_holiday: Column
            Boolean indicating whether the date is a holiday day in Tenerife or not
        tenerife_holiday_name: Column
            Boolean indicating the holiday name if any or "NOT HOLIDAY"
        is_weekend: Column
            Boolean indicating whether it is a weekend day or not
    """

    __tablename__ = "dim_date"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    day_of_week = Column(Integer, nullable=False)
    day_of_year = Column(Integer, nullable=False)
    is_tenerife_holiday = Column(Boolean, nullable=False)
    tenerife_holiday_name = Column(String, nullable=False)
    is_weekend = Column(Boolean, nullable=False)

    def __init__(self, date):
        self.date = date
        self.year = date.year
        self.month = date.month
        self.day = date.day
        self.day_of_week = date.weekday()
        self.day_of_year = int(date.strftime("%j"))
        self.tenerife_holiday_name = get_holiday_name(date)
        self.is_tenerife_holiday = (
            self.tenerife_holiday_name != "NOT HOLIDAY")
        self.is_weekend = (self.day_of_week >= 6)

    def __repr__(self):
        date_str = str(self.date)
        return f'DimDate(date={date_str})'


class DimTime(Base):
    """Time dimension table

    This table represent a time dimension table in a star schema. It is used to
    represent the possible hours in a day. That being integers in range [0, 23]

    Note that this is separate from the Date dimension for a better memory
    management. Why? Having date and hours in the same table means that for each
    day we have 24 rows, while this way we only have one row per day in the date
    dimension and only 24 fixed rows in the time dimension. In reality the
    number of dates that we are going to use aren't that much and we could go
    with the other approach but if later we can add more granular measures
    (having measures each 15 minutes for example) then this strategy would be
    better for having less redundant rows

    Attributes:
        __tablename__: str
           Name of the generated Table in the database
        id: Column
            Unique, autogenerated identifier for each row
        hour: Column
            Hour value: integer in range [0, 23]
    """
    __tablename__ = "dim_time"

    id = Column(Integer, primary_key=True)
    hour = Column(Integer, nullable=False, unique=True)

    def __init__(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError(
                f'DimTime __init__: invalid argument hour={hour}; hour must be in range [0, 23]')

        self.hour = hour

    def __repr__(self):
        return f'DimHour(hour={self.hour})'


class DimDuration(Base):
    """Duration dimension table

    This table represent a duration dimension table in a star schema. It is used
    to represent the possible durations of the measures of pollution data. For
    example, if the PM10 data is generated each hour then there has to be a row
    in this table with a duration of 1.

    Attributes:
        __tablename__: str
           Name of the generated Table in the database
        id: Column
            Unique, autogenerated identifier for each row
        duration_type: Column
            String representation of the duration: "HOURLY" or "DIARY"
        duration_hours: Column
            Integer value representation of the duration in hours
        hour_representations: dict
            Dictionary mapping duration to their string representation
    """

    __tablename__ = "dim_duration"

    id = Column(Integer, primary_key=True)
    duration_type = Column(String, nullable=False)
    duration_hours = Column(Integer, nullable=False, unique=True)

    hour_representations = {
        1: "HOURLY",
        24: "DIARY"
    }

    def __init__(self, duration_hours):
        if duration_hours != 1 and duration_hours != 24:
            raise ValueError(
                f'DimDuration __init__: invalid argument duration_hours={duration_hours}; duration_hours must be either 1 or 24')

        self.duration_hours = duration_hours
        self.duration_type = DimDuration.hour_representations.get(
            duration_hours)

    def __repr__(self):
        return f'DimDuration(duration_hours={self.duration_hours})'


class DimStation(Base):
    """Station dimension table

    This table represent a station dimension table in a star schema. It is used
    to hold information about the data sources

    Attributes:
        __tablename__: str
           Name of the generated Table in the database
        id: Column
            Unique, autogenerated identifier for each row
        source: Column
            String with the name of the data source. i.e. from who did we get the
            data?
        owner: Column
            String with the name of the station owner where the data was generated
        zone: Column
            String with the name of the station zone
        name: Column
            String with the name of the station. Note that this is set to be unique
            even though it is not sufficient because it makes things easier right
            now for searching
        latitude: Column
            Optional real value with the latitude coordinate of the station
        longitude: Column
            Optional real value with the longitude coordinate of the station
        altitude: Column
            Optional real value with the altitude coordinate of the station
    """

    __tablename__ = "dim_station"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    name = Column(String, nullable=False, unique=True)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    altitude = Column(Numeric)

    def __init__(self, source, owner, zone, name, latitude=None, longitude=None, altitude=None):
        self.source = source.upper()
        self.owner = owner.upper()
        self.zone = zone.upper()
        self.name = name.upper()
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def __repr__(self):
        return f'DimStation(name={self.name})'


class DimMeasurementType(Base):
    """Measurement type dimension table

    This table represent a measurement type dimension table in a star schema. It
    is used to hold information about the measures (measure name & unit)

    Attributes:
        __tablename__: str
           Name of the generated Table in the database
        id: Column
            Unique, autogenerated identifier for each row
        short_measure_name: Column
            Unique string that represent a short name for the measure (e.g. O3 for
            ozone)
        measure_name: Column
            String that represent the measure name (e.g. Ozone, Particulate matter
            of less than 1 micrometer)
        unit: Column
            String representing the unit of the measure (e.g. h for hours, m/s for
            meters per second)
    """

    __tablename__ = "dim_measurement_type"

    id = Column(Integer, primary_key=True)
    short_measure_name = Column(String, nullable=False, unique=True)
    measure_name = Column(String, nullable=False)
    unit = Column(String, nullable=False)

    def __init__(self, short_name, full_name, unit):
        self.short_measure_name = short_name.upper()
        self.measure_name = full_name.upper()
        self.unit = unit.upper()

    def __repr__(self):
        return f'DimMeasurementType(short_measure_name={self.short_measure_name})'


class FactMeasure(Base):
    """Measure fact table

    This table represent a measure fact table in a star schema. It is used to
    hold information about the measures values (e.g. 3.2, 22) units and extra
    needed information is provided by the dimensions (what are the units, what
    is being measure, for how long, when...)

    Attributes:
        __tablename__: str
           Name of the generated Table in the database
        id: Column
            Unique, autogenerated identifier for each row
        date_id: Column
            Foreing key referencing the date dimension (what day did the measure
            take place?)
        time_id: Column
            Foreing key referencing the time dimension (at what hour did the measure
            take place?)
        duration_id: Column
            Foreing key referencing the duration dimension (for how long did the
            measure take place?)
        source_id: Column
            Foreing key referencing the source dimension (where did this data came
            from?)
        measurement_type_id: Column
            Foreing key referencing the measurement type dimension (what does this
            value mean?)
        value: Column
            Measurement value
    """

    __tablename__ = "fact_measure"

    id = Column(Integer, primary_key=True)
    date_id = Column(Integer, ForeignKey('dim_date.id'))
    time_id = Column(Integer, ForeignKey('dim_time.id'))
    duration_id = Column(Integer, ForeignKey('dim_duration.id'))
    source_id = Column(Integer, ForeignKey('dim_station.id'))
    measurement_type_id = Column(
        Integer, ForeignKey('dim_measurement_type.id'))
    value = Column(Numeric)

    def __init__(self, date_id, time_id, duration_id, source_id, measurement_type_id, value):
        self.date_id = date_id
        self.time_id = time_id
        self.duration_id = duration_id
        self.source_id = source_id
        self.measurement_type_id = measurement_type_id
        self.value = value

    def __repr__(self):
        return f'FactMeasure(value={self.value})'


Base.metadata.create_all(engine)
