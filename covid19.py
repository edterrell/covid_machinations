#!/usr/bin/env python
# coding: utf-8

# this block is used for copying/moving files
import os
import shutil
import time
#shutil.copyfile('src', 'dst')
#shutil.move

# we want to ensure we are in the correct conda environment
import sys
print(sys.executable)

# provides ability to reload modules (wihtout leaving jupyter) if changes are made
#import importlib
#importlib.reload(scd)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs
# import regular expressions
import re

# This is a custom python module with dictionaries of states and countries;
# it also contains three functions repair_dict, reverse_dict, and custom_list
import state_country_dicts as scd

# get current date for use in creating filenames with embedded 'day'.
# convert datetime object to string
import datetime as dt
today  = dt.date.today()
day = today.strftime('%Y-%m-%d')
print(f'Today is {day}')

print ('If using Binder enter a timezone difference from UTC')
timezone = input(' Enter a number between 12 and -12:')
print(timezone)
if timezone:
    timezone = int(timezone)
    v = scd.tz_dict[timezone]
    t = pd.Timestamp.today(v)
    print (t)
    day = t.date().strftime('%Y-%m-%d')
print(f'Today is {day}')

# ensure a covid_data_update directory exists
new_dir = r'covid_data_update'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# ### Moves all files from covid_data_update to covid_data

# House keeping covid_data_update folder
# preparing the move of all files from covid_data_update to covid_data
# so that we are left with an empty covid_date_update folder
file_names = []
source_dir = 'covid_data_update'
target_dir = 'covid_data'
print("covid_data_update directory contents:")
file_names = os.listdir(source_dir)
print (file_names)
print ()
if file_names == []:
    print ('Directory is empty so no files available to move')

# The below will move and archive all files in covid_data_update to covid_data
# Move contents of source ('covid_data_update')to target ('covid_data')
for file_name in file_names:
    try:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
    except:
        print(f'{file_name} already exists in target dir')

print()
print("covid_data directory contents:")
file_names = os.listdir(target_dir)
print (file_names)
print()

def clean_up (number_str):
    '''This is a clean up routine so that only numeric characters remain'''
    number_str = number_str.replace(',', '').replace('null','0').rstrip(']').lstrip("'")
    return int(number_str)

# ### Custom state dictionaries
# creates a custom state dict
s_string = input('Enter state codes seperated by a space:') or 'ca ny il'
print()

slist = scd.custom_list (s_string)
state_dict = {key: value for key, value in scd.all_states.items() if value in slist}
print (state_dict)

# ### Add state and world population data
# create dataframes
all_state_pop = pd.read_csv('state_pop.csv').iloc[:,1:3].set_index('Code')
print (all_state_pop.head())

# create dataframes
world_pop = pd.read_csv('world_pop.csv').iloc[:,0:2].set_index('country')
temp = (world_pop.population/1000000).round(2)
world_pop['pop_millions'] = temp
print (world_pop.head())
print()

# ### State Scraping section
# The start dates for U.S.states and for countries are different so must be accounted for
st_start = pd.Timestamp('2020/3/13')
c_start = pd.Timestamp('2020/2/16')

# set end date to yesterday
#day == pd.Timestamp.today().strftime('%Y-%m-%d')
end = pd.Timestamp.today() - pd.Timedelta(days=1)
print(f"End date is set to yesterday: {end.strftime('%Y-%m-%d')}")

# set the index to the appropriate date range for states and countries
st_index = pd.date_range(st_start, end)
c_index = pd.date_range(c_start, end)
len(st_index)
len(c_index)

# list comprehension to extract just the state initials from the dict
st_list = list(state_dict.values())

# create an empty pandas df with column headers from state_dict
state = pd.DataFrame(columns = st_list,index=st_index)
state.sort_index(ascending = False).head()
#state.shape

state_url='https://www.worldometers.info/coronavirus/usa/'
# Here the keys are the state names and the values are the 2-letter abbreviation
for key, value in state_dict.items():
    url = state_url+key
    print(url)
    # scrape web page for state info and assign to soup
    response = requests.get(url)
    #response.status_code
    page = response.text
    soup = bs(page,"lxml")

    # Find block of text/data near 'graph-cases-daily'
    re_graph = re.compile('graph-cases')
    try:
        data = soup.find(text=re_graph).parent
    except:
        print(f'Unable to find {url}')
        print()
        break

    # Regex to pull out data chunk out of the larger soup like data
    myregex = re.compile (r'data:.*\]')
    mo = myregex.search(str(data))

    #mo.group() is a string so easy to get rid of the first entry
    #state_previous_cases is a list of daily new coronavirus cases
    state_previous_cases = mo.group().split(',')[1:]
    #len(state_previous_cases)

    # ensure match between length of the empty df and the new list
    if len(st_index)!= len(state_previous_cases):
        print (len(st_index))
        print (len(state_previous_cases))
        state_previous_cases = state_previous_cases[:-1]
        print (len(state_previous_cases))

    # merge states into the existing df and apply the function clean_up to convert strings to ints
    # state[value] where value is the 2-letter abreviation
    state[value] = state_previous_cases
    state[value] = state[value].fillna(0).apply(clean_up)

    time.sleep(2)
#print(state.sort_index(ascending = True).head())
print()

# Create df of new_cases/million population
cols = state.columns.to_list()
#print(cols)

# Extract just the poopulations for the states of interest
pop_series = all_state_pop.loc[cols].pop_millions
print (f'Population of selected states in millions is {pop_series}')

state_cases_by_million = (state/pop_series).round()
print (state_cases_by_million.tail(7))

# Plot 7-day moving averge per million population
plt.close('all')
fig,ax = plt.subplots(1,1,figsize=(18,8))
roll_data_all = state_cases_by_million.rolling(window=7).mean()
roll_data_all.plot(ax=ax, linewidth=3)
plt.title('US-Seven-day rolling averges per million population',fontsize=20)
plt.show()
#plt.savefig(f'./covid_data_update/us_rolling_avg_per_million_{day}.png');

def list2string(l):
    ''' This creates a a short string of state/country names
    used during file save
    '''
    str1 = "_"
    # return string
    return (str1.join(l))

# Allows user to select state for rolling average
s_available = list(state.columns)
print(f'States available: {s_available}')
print()

snames = (list2string(s_available))

select_state = input('Choose state for rolling averge:')or s_available[0]
select_state = select_state.upper()

if select_state not in s_available:
    select_state = s_available[0]

# Plot Daily New Cases and 7-day moving averge
fig,[ax1,ax2,ax3] = plt.subplots(3,1,figsize=(18,14))
roll_data = state.loc[:,[select_state]].rolling(window=7).mean()

roll_data.plot(ax=ax1, linewidth=3, color='r')
state.plot(kind='area',alpha=.4,ax=ax1,stacked=False);
ax1.set_title('Daily New Cases and 7-day moving average in RED',loc='left', fontsize=12,fontweight='bold')

# Plot 7-day moving averge
roll_data_all = state.rolling(window=7).mean()
roll_data_all.plot(ax=ax2, linewidth=3);
ax2.set_title('US-Seven-day rolling averges',loc='left',fontsize=12,fontweight='bold')

# Plot last 90 days
state_last90 = state.tail(90)

roll_data = state_last90.loc[:,[select_state]].rolling(window=7).mean()
roll_data.plot(ax=ax3, linewidth=3, color='r')
state_last90.plot(kind='area',alpha=.2,ax=ax3,stacked=False)
ax3.set_title('US Daily New Cases Last 90 Days',loc='left',fontsize=12,fontweight='bold')
plt.savefig(f'./covid_data_update/us_{snames}_{day}.png')
plt.show()

# ### Custom country dictionaries
# creates a custom country dict
print()
c_string = input('Enter country codes seperated by a space:') or 'fr it es'
clist = scd.custom_list (c_string)
country_dict = {key: value for key, value in scd.all_countries.items() if value in clist}
print(country_dict)
print()

# ### Scraping section
c_list = list(country_dict.values())
c_list

# create an empty pandas df with column headers from country_dict, using the starting dates for the country as index
country = pd.DataFrame(columns = c_list,index=c_index)
country.sort_index(ascending = False).head()

base_url='https://www.worldometers.info/coronavirus/country/'
# Here the keys are the country names and the values are the 2-letter abbreviation
for key, value in country_dict.items():
    url = base_url+key
    print(url)

    # scrape web page for country info and assign to soup
    response = requests.get(url)
    #response.status_code
    page = response.text
    #print(response.text[:400])
    soup = bs(page,"lxml")

    # Find block of text/data near 'graph-cases-daily'
    re_graph = re.compile('graph-cases')
    dat = soup.find(text=re_graph)

    try:
        data = soup.find(text=re_graph).parent
    except:
        print(f'Unable to find {url}')
        print()
        break

    # Regex to pull out data chunk out of the larger soup like data
    myregex = re.compile (r'data:.*\]')
    mo = myregex.search(str(data))

    #mo.group() is a string so easy to get rid of the first entry
    country_previous_cases = mo.group().split(',')[1:]

    # ensure match between length of the empty df and the new list
    if len(c_index)!= len(country_previous_cases):
        print (len(c_index))
        print (len(country_previous_cases))
        state_previous_cases = country_previous_cases[:-1]
        print (len(country_previous_cases))

    #print(country_previous_cases)
    previous_cases = ["0" if i == 'null' else i for i in country_previous_cases]
    len(previous_cases)
    # merge countries into the existing df and apply the function clean_up to convert strings to ints
    country[value] = previous_cases
    country[value] = country[value].fillna(0).apply(clean_up)
    time.sleep(2)

country.clip(lower=0,inplace=True) #large negative number removed for better graphic clarity
country.sort_index(ascending = False).head()
print()
print(f'country list: {clist}')

# create a reveresed iso3166 country-code dictionary
iso3166r = scd.reverse_dict(scd.iso3166)
country_dict = {key: value for key, value in scd.iso3166r.items() if value in clist}
w_cols = list(country_dict.keys())

# fix uk, us entries to match conventional country names
if 'uk' in w_cols:
    w_cols.remove('uk')
    w_cols.append('United Kingdom')
if 'US' in w_cols:
    w_cols.remove('US')
    w_cols.append('United States')
print (f'w_cols: {w_cols}')

# Extract just the populations for the states of interest
wpop_series = world_pop.loc[w_cols].pop_millions
wpop_series.rename(index=iso3166r, inplace=True)
print (wpop_series)

# repair issues with uk and us
wpop_series.rename({'United Kingdom':'UK','United States':'US'},inplace=True)
world_cases_by_million = (country/wpop_series).round()
world_cases_by_million.tail()

# Plot 7-day moving averge per million population
plt.close('all')
fig,ax = plt.subplots(1,1,figsize=(18,8))
roll_data_all = world_cases_by_million.rolling(window=7).mean()
roll_data_all.plot(ax=ax, linewidth=3);
plt.title('World-Seven-day rolling averges per million population',fontsize=20)
plt.show()

# Allows user to select the country for the rolling average
c_available = list(country.columns)
print(f'Countries available: {c_available}')
print()

snames = (list2string(c_available))
select_country = input('Choose country for rolling averge:') or c_available[0]
select_country = select_country.upper()

if select_country not in c_available:
    select_country = c_available[0]

# Plot Daily New Cases and 7-day moving averge
fig,[ax1,ax2,ax3] = plt.subplots(3,1,figsize=(18,14))
roll_data = country.loc[:,[select_country]].rolling(window=7).mean()
roll_data.plot(ax=ax1, linewidth=3, color='r')
country.plot(kind='area',alpha=.4,ax=ax1,stacked=False)
ax1.set_title('World New Cases and 7-day moving average in RED',loc='left', fontsize=12,fontweight='bold')

# Plot 7-day moving averge for all
roll_data_all = country.rolling(window=7).mean()
roll_data_all.plot(ax=ax2, linewidth=3)
ax2.set_title('World-Seven-day rolling averges',loc='left',fontsize=12,fontweight='bold')

# Plot 7-day moving averge last 90 days only
country_last90 = country.tail(90)
roll_data = country_last90.loc[:,[select_country]].rolling(window=7).mean()
roll_data.plot(ax=ax3, linewidth=3, color='r')
country_last90.plot(kind='area',alpha=.2,ax=ax3,stacked=False);
ax3.set_title('World Daily New Cases Last 90 Days',loc='left',fontsize=12,fontweight='bold')
plt.savefig(f'./covid_data_update/world_{snames}_{day}.png')
plt.show()

# Daily New Cases in tabular format
pd.set_option('display.max_rows', 300)
pd.set_option('display.min_rows', 300)
# Note that new cases provided for Spain and some states have a pattern of muliple days with exactly the same number

# ### Save merged dataframes to csv
# Merge state and country dfs into one
world = state.merge(country,left_index=True,right_index=True,how='outer')
world = world.fillna(0).astype(int)

# Sorting the table with recent dates on the top
world_table = world.sort_index(ascending = False)
world_table.to_csv(f'./covid_data/world_table_{day}.csv')

total_by_million = state_cases_by_million.merge(world_cases_by_million,left_index=True, right_index=True, how='outer')

# ### Weekly Sums
# Note that the last week may be only a partial unless this is executed on Mondays
df1 = world.resample('w').sum()
df1.sort_index(ascending = False).head(10)

# ### Custom graphs section
print()
print(world.tail(7))
print()
print(total_by_million.tail(7))
print()

start = input('Enter y to run custom graphs section: ')
while start == 'y':
    import date_select as ds
    start,stop = ds.date_maker()
    world_cols = world.columns.to_list()
    print (world_cols)

    default_str = ' '.join(world_cols)

    # ### Select custom states and countries
    s_string = input('Enter any codes from the above list:') or default_str
    print()

    slist = scd.custom_list (s_string)
    new_slist =[]
    for item in slist:
        if item in world_cols:
            new_slist.append(item)
    print (new_slist)

    if new_slist:
        df = world.loc[start:stop, new_slist]
        title ='Custom rolling averges'
        print (df.tail(14))
        print()
    else:
        print('custom codes not available')

    if new_slist:
        df1 = total_by_million.loc[start:stop, new_slist]
        title1 ='Custom rolling averges per million'
        print (df1.tail(14))
        print()
    else:
        print('custom codes not available')

    # Plot custom moving averge (default: 7 days)
    if new_slist:
        plt.close('all')
        fig,[ax1,ax2] = plt.subplots(2,1,figsize=(18,10))
        roll_data_all = df.rolling(window=7).mean()
        roll_data_all.plot(ax=ax1, linewidth=3)
        ax1.set_title(title,fontsize=12,fontweight='bold')

    # Plot custom moving averge (default: 7 days) per million population
        roll_data_all = df1.rolling(window=7).mean()
        roll_data_all.plot(ax=ax2, linewidth=3)
        ax2.set_title(title1,fontsize=12,fontweight='bold')
        plt.savefig(f'./covid_data_update/custom_date_range_{day}.png')
        plt.show()
    start = input('Enter q to quit or y to continue: ')

# Remove all png filenames

clean ='n'
clean = input('Enter y to clean-up the covid_data_update directory: ')
print()
if clean == 'y':
    file_names = os.listdir('covid_data_update')
    for fname in file_names:
        try:
            os.remove(f'covid_data_update/{fname}')
            print(f'Removing {fname}')
        except:
            print('There was a problem automatically cleaning the directory')


# ### Displays all updated graphs files
#!ls covid_data_update


# ### tabla rasa

# Ensure helper files used have been removed
#!rm -f covid_data/covid_text covid_data/flist_of_covid_png covid_data/temp.xlsx
#!rm -f flist_of_covid_png

#If todays files are not deleted, they will automatically be backed up to the covid_data directory, the next time this program is run
