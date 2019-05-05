from sqlalchemy import create_engine, Column, Integer, Boolean, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class DimDate(Base):
    __tablename__ = "dim_date"

    id = Column(Integer, primary_key=True)
    sql_date = Column(Date, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    week_of_year = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    day_of_week = Column(Integer, nullable=False)
    day_of_year = Column(Integer, nullable=False)
    is_tenerife_holiday = Column(Boolean, nullable=False)
    tenerife_holiday_name = Column(String, nullable=False)
    is_weekend = Column(Boolean, nullable=False)

    def __repr__(self):
        return f'<DimDate {self.sql_date}>'


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
