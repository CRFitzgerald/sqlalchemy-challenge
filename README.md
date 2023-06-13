# sqlalchemy-challenge
In this challenge, I used Python, Pandas, and SQLAlchemy ORM queries to perform climate analysis and data exploration on a Hawaiian weather database. I then created a Flask application to connect to the same database and create a landing page diplaying various routes - both static and dynamic - to various datasets of interest. The Jupyter Notebook where I performed data analysis, app.py file containing my Flask code, and Resources folder with original data can call be found in the SurfsUp folder.

### Tools Used
* Python
* SQLAlchemy ORM 
* Pandas
* Matplotlib
* Flask

## Jupyter Notebook Database Connection
1. I used SQLAlchemy create_engine to connect to the SQLite database and automap_base to reflect the Measurement and Station tables into classes.
2. SQLAlchemy session is used to link Python to the database and session is closed after Station Analysis is completed.

## Precipitation Analysis
1. I queried the SQLite Hawaii database to find the most recent date in the dataset: 08/23/2017.
2. Using the 08/23/2017 date from the previous query, I queried the database to obtain all precipitation  measurements and their relative dates from the most recent year. 
3. I saved the results as a Pandas dataframe with the date column as the index.
4. I used Pandas Plotting with Matplotlib to plot the precipitation in inches relative to date.
5. I used Pandas to print summary statistics for the above dataframe/plot.

## Station Analysis
1. I queried the Station table to find the number of stations, which is 9.
2. I queried the Measurement table to find the number of measurements taken per station and order the stations from greatest to least activity with their measurement counts. 
3. For Station USC00519281 - the most active station with 2772 measurements - I retrieved the following temperature calculations: Minimum, 54.0. Highest, 85.0. Average, 71.66.
4. I also queried the most recent year's worth of temperature measurements from Station USC00519281.
5. I converted this data to a Pandas dataframe, which I used to plot a histogram of temperatures in a bin for each month.

## API SQLite Connection & Landing Page
My Flask application generates an engine to the SQLite database and automap_base to reflect the Measurement and Station tables. The landing page displays the routes listed in the next sections.

## API Static Routes
* Precipitation - returns jsonified precipitation data for only the last year in the database.
* Stations - returns jsonified data of all of the stations in the database.
* Tobs - returns jsonified data for only the last year's temperatures at Station USC00519281.

## API Dynamic Route
* Start Route - accepts the start date as a parameter from the URL to return the minimum, maximum, and average temperatures calculated from the given start date to the end of the dataset.
* Start/End Route - accepts the start and end dates as parameters from the URL and returns the min, max, and average temperatures calculated from the given start date to the given end date.



