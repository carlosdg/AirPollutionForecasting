import logging
import os
from datetime import date
from glob import glob

import pandas as pd

from models import DimDate, Session


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
        'index_col': 0
    })
    result_data_frame = pd.DataFrame()

    for data_frame in data_frames:
        result_data_frame = pd.concat([result_data_frame, data_frame], axis=1)

    return result_data_frame


if __name__ == "__main__":
    session = Session()
    test = DimDate(date.today())

    try:
        session.add(test)
        session.commit()
    except:
        logging.warn(f"Row '{test}' not added")
