-- Definition of the dimension tables

CREATE TABLE dim_date(
  id SERIAL PRIMARY KEY,
  year INT NOT NULL,
  month INT NOT NULL,
  week_of_month INT NOT NULL,
  week_of_year INT NOT NULL,
  day INT NOT NULL,
  day_of_week INT NOT NULL,
  day_of_year INT NOT NULL,
  is_tenerife_holiday boolean NOT NULL,   -- Flag to know if the day is holiday (not counting weekend unless the holiday is on weekend of course)
  tenerife_holiday_name text NOT NULL,    -- Holiday name or 'NO HOLIDAY'
  is_weekend boolean NOT NULL             -- Flag to know whether the date is Saturday or Sunday
);

CREATE TABLE dim_time(
  id SERIAL PRIMARY KEY,
  hour INT NOT NULL         -- from 0 to 23
);

CREATE TABLE dim_duration(
  id SERIAL PRIMARY KEY,
  duration_type VARCHAR(15) NOT NULL,   -- 'HOURLY', 'DIARY'
  duration_hours INT NOT NULL           -- 1 or 24
);

CREATE TABLE dim_station(
  id SERIAL PRIMARY KEY,
  source VARCHAR(30) NOT NULL,    -- Where did the data come from
  owner VARCHAR(30) NOT NULL,     -- To who does the station belong
  zone VARCHAR(30) NOT NULL,      -- Where is located
  name VARCHAR(60) NOT NULL,      -- Station name
  latitude NUMERIC NOT NULL,
  longitude NUMERIC NOT NULL,
  altitude NUMERIC NOT NULL
);

CREATE TABLE dim_measurement_type(
  id SERIAL PRIMARY KEY,
  short_measure_name VARCHAR(10) NOT NULL,
  measure_name VARCHAR(60) NOT NULL,
  unit VARCHAR(30) NOT NULL
);


-- Definition of the fact tables

CREATE TABLE fact_measure(
  id SERIAL PRIMARY KEY,
  date SERIAL REFERENCES dim_date,
  time SERIAL REFERENCES dim_time,
  duration SERIAL REFERENCES dim_duration,
  source SERIAL REFERENCES dim_station,
  measurement_type SERIAL REFERENCES dim_measurement_type,
  value FLOAT
);


-- Insertion of static values to the dimension tables

INSERT INTO dim_time VALUES
(0, 0),
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20),
(21, 21),
(22, 22),
(23, 23);

INSERT INTO dim_duration VALUES 
(0, 'daily', 24), 
(1, 'hourly', 1);

INSERT INTO dim_station VALUES
(1, 'CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA', 'CASA CUNA', -16.27769219311504, 28.45103088037192, 0),
(2, 'CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA', 'DEPOSITO DE TRISTAN', -16.27877561502283, 28.45815968532356, 0),
(3, 'CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA', 'GARCIA ESCAMEZ', -16.27184954317193, 28.45664139423877, 0),
(4, 'CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA', 'PARQUE LA GRANJA', -16.26487493264499, 28.46300210751911, 0),
(5, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'TOME CANO', -16.26186591001509, 28.4621688991889, 0),
(6, 'CANARY GOVERNMENT', 'CEPSA', 'SANTA CRUZ - LA LAGUNA', 'VUELTA LOS PAJAROS', -16.27697222222222, 28.462, 0),
(7, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'PISCINA MUNICIPAL', -16.26340423894506, 28.45791579546199, 0),
(8, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'TENA ARTIGAS', -16.27685561780176, 28.45537560999706, 0),
(9, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'TIO PINO', -16.27012462756456, 28.45925503570103, 0),
(10, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'PALMETUM', -16.25852644443512, 28.452545726989584, 0),
(11, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'COMANDANCIA', -16.2456057616887, 28.47720124167907, 0),
(12, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'HACIENDA', -16.24870801361327, 28.46323011938556, 0),
(13, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'BOMBEROS', -16.26097493125278, 28.45828864775618, 0),
(14, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'SANTA CRUZ - LA LAGUNA', 'COMISARIA', -16.25866186061195, 28.45912395381277, 0),
(15, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'LOS GLADIOLOS', 0, 0, 0),
(16, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'MERCATENERIFE', 0, 0, 0),
(17, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'PUERTA LITORAL - REFINERIA', 0, 0, 0),
(18, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'PUERTA PRINCIPAL - REFINERIA', 0, 0, 0),
(19, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'REFINERIA', 0, 0, 0),
(20, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'REFINERIA - TORRE METEOROLOGICA', 0, 0, 0),
(21, 'CANARY GOVERNMENT', 'UNKNOWN', 'SANTA CRUZ - LA LAGUNA', 'VIEJA Y CLAVIJO', 0, 0, 0),
(22, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'TENERIFE NORTH', 'LA ZAMORA', -16.57072474718117, 28.3831334121515, 0),
(23, 'CANARY GOVERNMENT', 'CANARY GOVERNMENT', 'TENERIFE SOUTH', 'LA HIDALGA - ARAFO', -16.39991556602504, 28.33734903726858, 0),
(24, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'BARRANCO HONDO', -16.3581166775973, 28.39342430257058, 0),
(25, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'LA BUZANADA', -16.65275205038472, 28.07264560673482, 0),
(26, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'CALETILLAS', -16.36193673089008, 28.37672185381682, 0),
(27, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'LA GUANCHA - CANDELARIA', -16.36833427699988, 28.38016131594777, 0),
(28, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'EL RIO', -16.52369883375512, 28.14507452830099, 0),
(29, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'LAS GALLETAS', -16.65582224157534, 28.00778986209971, 0),
(30, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'GRANADILLA', -16.57757403405965, 28.11249291171923, 0),
(31, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'IGUESTE', -16.37197069941999, 28.38054612249282, 0),
(32, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'EL MEDANO', -16.53603007019015, 28.04732410738179, 0),
(33, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'SAN ISIDRO', -16.55983699771885, 28.08003389965855, 0),
(34, 'CANARY GOVERNMENT', 'ENDESA', 'TENERIFE SOUTH', 'SAN MIGUEL DE TAJAO', -16.47161086862779, 28.11139253073869, 0),
(35, 'CANARY GOVERNMENT', 'UNKNOWN', 'TENERIFE SOUTH', 'TORRE METEOROLOGICA DE CANDELARIA', 0, 0, 0),
(36, 'AEMET', 'AEMET', 'SANTA CRUZ - LA LAGUNA', 'SANTA CRUZ DE TENERIFE', 28.46333333, -16.25527778, 35),
(37, 'AEMET', 'AEMET', 'TENERIFE NORTH', 'AEROPUERTO NORTE', 28.4775, -16.329444444444444, 632),
(38, 'AEMET', 'AEMET', 'TENERIFE SOUTH', 'AEROPUERTO SUR', 28.047500000000003, -16.560833333333335, 64),
(39, 'AEMET', 'AEMET', 'TENERIFE SOUTH', 'IZANA', 28.30888888888889, -16.499444444444446, 2371),
(40, 'AEMET', 'AEMET', 'TENERIFE SOUTH', 'GUIMAR', 28.31833333333333, -16.38222222222222, 115),
(41, 'AEMET', 'AEMET', 'TENERIFE NORTH', 'PUERTO DE LA CRUZ', 28.418055555555558, -16.548055555555557, 25);


INSERT INTO dim_measurement_type VALUES
(0, 'TMIN', 'MINIMUM TEMPERATURE', 'CELSIUS DEGREES'),
(1, 'TMINHOUR', 'HOUR OF MINIMUM TEMPERATURE', 'h'),
(2, 'TMAX', 'MAXIMUM TEMPERATURE', 'CELSIUS DEGREES'),
(3, 'TMAXHOUR', 'HOUR OF MAXIMUM TEMPERATURE', 'h'),
(4, 'WSMAX', 'MAXIMUM WIND SPEED', 'm/s'),
(5, 'WSMAXDIR', 'DIRECTION OF MAXIMUM WIND SPEED', 'DEGREES'),
(6, 'WSMAXHOUR', 'HOUR OF MAXIMUM WIND SPEED', 'h'),
(7, 'SUN', 'HOURS OF SUN', 'h'),
(8, 'PMIN', 'MINIMUM PRESSURE', 'mb'),
(9, 'PMINHOUR', 'HOUR OF MINIMUM PRESSURE', 'h'),
(10, 'PMAX', 'MAXIMUM PRESSURE', 'mb'),
(11, 'PMAXHOUR', 'HOUR OF MAXIMUM PRESSURE', 'h'),
(12, 'T', 'TEMPERATURE', 'CELSIUS DEGREES'),
(13, 'P', 'ATMOSPHERIC PRESSURE', 'mb'),
(14, 'WD', 'WIND DIRECTION', 'DEGREES'),
(15, 'WS', 'WIND SPEED', 'm/s'),
(16, 'RH', 'RELATIVE HUMIDITY', '%'),
(17, 'PP', 'PRECIPITATION', 'l/m2'),
(18, 'SR', 'SOLAR RADIATION', 'W/m2'),
(19, 'PM10', 'PARTICULATE MATTER LESS THAN 10 MICROMETERS', 'µg/m3'),
(20, 'PM2.5', 'PARTICULATE MATTER LESS THAN 2.5 MICROMETERS', 'µg/m3'),
(21, 'PM1', 'PARTICULATE MATTER LESS THAN 1 MICROMETER', 'µg/m3'),
(22, 'O3', 'OZONE', 'µg/m3'),
(23, 'CO', 'CARBON MONOXIDE', 'mg/m3'),
(24, 'H2S', 'HYDROGEN SULFIDE', 'µg/m3'),
(25, 'NO', 'NITROGEN MONOXIDE', 'µg/m3'),
(26, 'NO2', 'NITROGEN DIOXIDE', 'µg/m3'),
(27, 'NOX', 'NITROGEN OXIDES', 'µg/m3'),
(28, 'SH2', 'HYDROGEN SULFIDE', 'µg/m3'),
(29, 'SO2', 'SULFUR DIOXIDE', 'µg/m3'),
(30, 'TRS', 'TOTAL REDUCED SULPHUR', 'µg/m3'),
(31, 'BC', 'BLACK CARBON', 'µg/m3'),
(32, 'BEN', 'BENCENE', 'µg/m3'),
(33, 'TOL', 'TOLUENE', 'µg/m3'),
(34, 'XIL', 'XYLENE', 'µg/m3'),
(35, 'M-P XIL', 'M-P XYLENE', 'µg/m3');