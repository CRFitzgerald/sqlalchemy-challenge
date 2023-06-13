# sqlalchemy-challenge
In this challenge, I use Python, Pandas, and SQLAlchemy ORM queries to perform climate analysis and data exploration on a Hawaiian weather database. 

### Tools Used
* Python
* SQLAlchemy ORM 
* Pandas
* Matplotlib
* Flask

## Jupyter Notebook Database Connection
1. I used SQLAlchemy create_engine to connect to the SQLite database and automap_base to reflect the Measurement and Station tables into classes.
2. SQLAlchemy session is used to link Python to the database and session is closed.

## Precipitation Analysis
1. I queried the SQLite Hawaii database to find the most recent date in the dataset: 08/23/2017.
2. Using the 08/23/2017 date from the previous query, I queried the database to obtain all precipitation  measurements and their relative dates from the most recent year. 
3. I saved the results as a Pandas dataframe with the date column as the index.
4. I used Pandas Plotting with Matplotlib to plot the precipitation in inches relative to date.
5. I used Pandas to print summary statistics for the above dataframe/plot.

## Station Analysis

## API SQLite Connection & Landing Page

## API Static Routes

## API Dynamic Route
