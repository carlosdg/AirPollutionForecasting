import datetime as dt
import logging
import os
from glob import glob

import pandas as pd

from models import (DimDate, DimDuration, DimMeasurementType, DimStation,
                    DimTime, FactMeasure, Session)


def parse_ending_datetime(datetime_str):
    """Returns a datetime object representing the start of the given datetime

    Problem: the timestamps that we have represent when the measures were done.
    Also the hours go from 1 to 24 and the datetime module expects hours ranging
    from 0 to 23.

    This function takes a datetime in the format 'YYYY-MM-DD hh:mm' being hh the
    hours from 1 to 24 and the datetime representing a finish datetime. And
    returns a datetime object representing the beginning datetime of the measure
    (1 hour before the given datetime)


    Arguments: 
        date_str {str} -- String representing the datetime to parse

    Returns:
        datetime.datetime -- Datetime object representing the start time of the
        given string
    """
    hour = datetime_str[11:13]
    hour = int(hour) - 1

    if hour < 0:
        raise ValueError(
            f'Invalid hour. After getting the previous hour we got a negative number: {hour}')

    hour = str(hour).zfill(2)
    date = f'{datetime_str[:11]}{hour}{datetime_str[13:]}'
    date = dt.datetime.strptime(date, '%d-%m-%Y %H:%M')

    return date


def read_csvs(csv_file_paths, options):
    """Read CSVs from the given paths and returns a list of DataFrames

    Arguments:
        csv_file_paths {list<str>} -- List of file paths where
            the CSVs are located
        read_csv_options {obj} -- Parameters to pass to `pandas.read_csv`

    Returns:
        list<obj> -- List of DataFrames representing each CSV
    """
    return [pd.read_csv(filePath, **options)
            for filePath in csv_file_paths]


def read_month_csvs(folder_path):
    """Parses a month of Pollution data

    The given folder path have to have inside subfolders where the CSVs
    are located, those are the CSV files that are read. These CSVs contain
    data for the same month but there are multiple of them because there
    are a lot of parameters (PM10, PM2.5, Ozone, etc)

    Arguments:
        folder_path {str} -- Path to the folder with the month data

    Returns:
        obj -- DataFrame representing the month's data
    """
    csvs_paths_pattern = os.path.join(folder_path, '**/*.csv')
    csv_file_paths = glob(csvs_paths_pattern)
    data_frames = read_csvs(csv_file_paths, {
        'encoding': 'latin5',
        'parse_dates': [['Fecha', 'Hora']],
        'index_col': 0,
        'date_parser': parse_ending_datetime
    })
    result_data_frame = pd.DataFrame()

    for data_frame in data_frames:
        result_data_frame = pd.concat([result_data_frame, data_frame], axis=1)

    return result_data_frame
