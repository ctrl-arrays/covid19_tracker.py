This project is a practice tool built in Python to visualize COVID-19 data for any country using real-world datasets. It demonstrates key skills in data analysis, visualization, and secure coding practices, and is designed to be modular, readable, and beginner-friendly.
===============================================================================================================================================================================================================================================================================
* Features
Downloads COVID-19 data from Our World in Data

Filters and visualizes data for a user-specified country

Generates static plots using matplotlib and seaborn

Creates interactive charts with plotly

Optional export of filtered data to CSV

Robust error handling and clean documentation
=======================================================================
* Learning Focus
This project was created for educational purposes to practice:

Working with real-world datasets

Building command-line interfaces with argparse

Writing modular, secure, and well-documented code

Visualizing time-series data with multiple libraries

Handling edge cases and user input gracefully
=====================================================================
* Known Issue
The script attempts to download COVID-19 data from https://covid.ourworldindata.org/data/owid-covid-data.csv However, this URL may be deprecated or blocked by some networks/firewalls. You may encounter a Max retries exceeded with URL error.

Workaround: You can manually download the dataset from the COVID-19 Data Explorer and place it in the data/ folder. The script will detect and use the local file automatically.
==========================================================================================================================================================================================
 * bash
            python covid_tracker.py --country "Pick country, Enter it here" --save
--country: Name of the country to track 

--save: Optional flag to export filtered data to CSV
========================================================================================
* TODO
Investigate alternative data sources or APIs

Add fallback logic for manual download

Improve user feedback when data is missing or blocked
