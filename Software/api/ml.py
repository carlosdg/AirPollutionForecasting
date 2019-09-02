import pickle
import pandas as pd

def preprocess_data(data):
    # Put measure variables in columns
    measure_columns = data.pivot(columns="short_measure_name", values="value")
    feature_cols = [
        'date', 'hour',
        'PM2.5', 'PM10', 'O3', 'NO2', 'SO2',
        'WS', 'WD', 'P', 'RH', 'T', 'PP', 'SR'
    ]
    d2 = pd.concat([data, measure_columns], axis=1)
    df = d2.groupby(["date", "hour"]).mean().reset_index().loc[:, feature_cols]

    # Add a datetime column and remove the date & hour columns
    df["datetime"] = pd.to_datetime(
        df["date"]) + pd.to_timedelta(df["hour"], unit='h')
    df.drop(["date", "hour"], axis=1, inplace=True)
    df.set_index("datetime", inplace=True)

    # Fill any possible missing date
    # Fixme: We cannot trust min & max to be valid, we could have only 20 hours between them
    full_datetime_range = pd.date_range(
        start=df.index.min(), end=df.index.max(), freq="H")
    df = df.reindex(full_datetime_range)

    # Input missing data
    df_clean = df.interpolate(method="linear").fillna(0)

    # Create the features (put the values for the 24h in columns)
    def get_shifted_df(shift):
        return df_clean.iloc[shift:].reset_index(drop=True).add_suffix(f"__shift_{shift}")

    X = pd.concat([get_shifted_df(i) for i in range(24)], axis=1).iloc[0]

    return X.values.reshape(1, -1)


with open('forecast_24_model.pkl', 'rb') as f:
    forecast_model = pickle.load(f)
