from sqlalchemy import create_engine, Column, Integer, Boolean, String, Date, ForeignKey
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
        return f'DimDate(date="{date_str}")'


class DimTime(Base):
    __tablename__ = "dim_time"

    id = Column(Integer, primary_key=True)
    hour = Column(Integer, nullable=False)


class DimDuration(Base):
    __tablename__ = "dim_duration"

    id = Column(Integer, primary_key=True)
    duration_type = Column(String, nullable=False)    # 'HOURLY', 'DIARY'
    duration_hours = Column(Integer, nullable=False)  # 1 or 24


class DimStation(Base):
    __tablename__ = "dim_station"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    name = Column(String, nullable=False)
    latitude = Column(String)
    longitude = Column(String)
    altitude = Column(String)


class DimMeasurementType(Base):
    __tablename__ = "dim_measurement_type"

    id = Column(Integer, primary_key=True)
    short_measure_name = Column(String, nullable=False)
    measure_name = Column(String, nullable=False)
    unit = Column(String, nullable=False)


class FactMeasure(Base):
    __tablename__ = "fact_measure"

    id = Column(Integer, primary_key=True)
    date_id = Column(Integer, ForeignKey('dim_date.id'))
    time_id = Column(Integer, ForeignKey('dim_time.id'))
    duration_id = Column(Integer, ForeignKey('dim_duration.id'))
    source_id = Column(Integer, ForeignKey('dim_station.id'))
    measurement_type_id = Column(
        Integer, ForeignKey('dim_measurement_type.id'))
    value = Column(Integer)


Base.metadata.create_all(engine)
