# Air Pollution Forecasting

This is my project done for my degree thesis. 

The main goal was to build a system to predict air pollution in Tenerife. In particular the concentration of suspended particulate matter of less than 2.5 micrometers using Machine Learning models.

## Project Overview

### Data Extraction

The first step was to extract the data from the source and for that I had to build a program to do it automatically. It can be found in the folder `Software/pollution_data_downloader`. This program spawns a browser, navigates to the web form to download the data, fills it according to the given parameters and downloads the data in a `downloads` folder.

### Data Warehouse

Docker has been used in this project so it is easier to reproduce by others.

For storing the data locally I used PostgreSQL as a data warehouse inside a Docker container whose configuration can be found in `Software/docker-compose.yml`. And the schema was defined using the SQLAlchemy ORM in the `Software/data_loader/src/models.py` file.

### Insert Data

After the data was downloaded and the warehouse model defined the next step was to insert the data into the warehouse applying the right transformations so it conforms to the schema. The code for that can be found in the `Software/data_loader` folder. 

### Data Exploration and Machine Learning

The notebooks can be found in the `Software/jupyter/notebooks` folder. The best model trained was <span style="color:forestgreen">Gradient Boosting</span> using <span style="color:forestgreen">PCA</span> to reduce the dimensionality of the data and applying power transformations to reduce the effect of skewness, having the distributions look more like a normal and reduce the impact of outliers.

The jupyter server is run inside a Docker container, the configuration can be found in `Software/docker-compose.yml`

### Web application

Finally an API (`Software/api`) and a web page (`Software/webapp`) were built to show the latest measures in the system and see the forecasts using the best machine learning model trained.

The API is also run from inside a Docker container and it is also defined in `Software/docker-compose.yml`.

You can see [the app deployed in Heroku](https://tfg-apf-web.herokuapp.com) with part of the data because it didn't fit in the free PostgreSQL database that they provide.