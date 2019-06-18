# Helper Program To Transform & Load Data into the Warehouse

## Arguments

### Environment variables

- **VERBOSE**: Whether SQLAlchemy `echo` is set to true or not. The only value allowed to set it to true is: `True`
- **CONNECTION_STRING**: Connection string that SQLAlchemy uses to connect to the database, the default is `postgresql://user:pass@localhost:5432/warehouse_db`

### `insert_data.py` arguments

```
USAGE: python insert_data.py <path_to_data> <station_name> <measure_duration>
e.g: python insert_data.py tome_cano/2019_01 "TOME CANO" 1
```

1. The path to the data to insert
2. Station name as expected in the database model (See `Software/data_loader/src/insert_dimension_rows.py`)
3. The number of hours that the measures took (e.g. 1 means that each measure was taken in a span of 1 hour)
