# covid_machinations
# Covid programs summary
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/edterrell/covid_machinations.git/main)
.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/edterrell/covid_machinations.git/main
 
## There are two main notebooks: 
1. Covid.ipynb 
2. ColoradoOutbreaks.ipynb

Supporting modules: state_county_dicts.py, date_checker.py, and pie_dict.py
Supporting code: style-table.css,  style-notebook.css,

## Covid.ipynb
The main purpose of this COVID.ipynb is to create summary graphs of daily new cases using both Beautiful Soup and request to extract and parse the information from the web. Pandas is used throughout.

Covid.ipynb allows the user to choose which states/countries to be overlayed on top of each other in a graph, providing better insight into their relationship with respect to time. The program is divided into a section on states and into a section on countries. Eight graphs in total are generated and stored in a subdirectory: ‘covid_data_recent’. 

At the start of program, housekeeping occurs moving all files from ‘covid_data_recent’ to ‘covid_data’ for archival. All file names include the current date as part of the file name.

The graphs are: 
* Daily New Cases (solid colors) and moving average for one state/country
* Seven day rolling averages
* Daily New Cases - last 60 days
* Daily New Cases - last 90 days

### Supporting module: state_country_dicts: 
* This is imported as ‘scd’
* ‘scd’ is a python module with dictionaries of states and countries; It contains the names of the state/country as the keys and the abbreviation as the values.
* ‘scd’ also contains three functions repair_dict, reverse_dict, and custom_list

## ColoradoOutbreaks.ipynb
Colorado outbreak files are updated on the web once a week in the form of an updated spreadsheet, available for download. Before download we use the python module date_checker that compares the date of the
last saved outbreak.xlsx file (previous) to the date of the (current) outbreak.xlsx file on the web. If a newer file is available the user is prompted to continue.

The program outputs  a series of csv files sorted on COUNTY, DATE, TOTAL and TYPE. A Boulder county csv is also saved. In the visual realm, it outputs a graph of outbreaks per month and a piechart of current active sites.  All files are stored in the folder ‘covid_data_update’.

It also creates (and stores) a histogram of outbreak cases by month, using the pandas’ resampling method.

This program is not as robust as COVID.ipynb due to random formatting issues in the input data.

### Supporting module: date_checker
The can be run within ColoradoOutbreaks or as a standalone python executable. Checks to see if a newer xlsx file has been posted than the latest saved file. This is imported as ‘dc’.  

There are two functions: 
* get_date: examines the covid_data subdirectory, finds files starting with ‘covid_reports’ , extracts and coverts the date component of the filename into a datetime object for comparison with date of current outbreak file on the web. Returns the date of the latest saved spreadsheet.
* compare: compares the date of the previous xlsx link and the date of the current xlsx link.  ‘Compare’ returns a tuple: 
	1. the page url (link) 
	2. the date of the link (current)

### Supporting module: pie_dict:
* The pie_dict module contains only one function (pie) which reduces 
the number of types into only seven basic categories 
* This is used for creating piecharts
* This is imported as: ‘from pie_dict import pie’%  
