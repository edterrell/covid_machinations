#!/usr/bin/env python
# coding: utf-8


#import requests
#import dateutil.parser
#import time


import datetime as dt
import os
import sys
import urllib
import requests
import re
from bs4 import BeautifulSoup as bs

url = 'https://covid19.colorado.gov/data/outbreak-data'


# 'get_date' extracts the list of covid_reports in the covid_data directory 
# and ouputs the datetime of the latest report
def get_date ():
	'''	   '''
	ttt=[]
	date_list= []
	l = [f for f in os.listdir('covid_data') if f.startswith('covid_report')]
	for file in l:	
		ttt.append(file.split('.')[0].split('_')[2])
	for string in ttt:
		date_list.append(dt.datetime.strptime(string,'%Y-%m-%d'))

	# assigns the datetime of the latest report to 'previous'
	previous = sorted(date_list)[-1]
	str = previous.strftime('%Y-%m-%d')
	print(f'latest saved spreadsheet is {str}')
	return previous

def compare (previous):
	# compares the date of the previous xlsx link and the date
	# of the current xlsx link
	# returns a tuple: 
	# 	the page url (link) 
	# 	the date of the link (current)
	
	with urllib.request.urlopen(url) as response:
		html = response.read()
		soup = bs(html,features="lxml")

	# using regex to look for xlsx file on the page and extract the link
	re_xlsx = re.compile('xlsx')
	link = soup.find(text = re_xlsx).parent['href']
	
	# date comparison
	# find and extract the xlsx date; assign to 'current' 
	# compare 'current' to 'previous'
	x_date = re.compile(r'\d\d?(?:-|_|\s)\d\d?(?:_|-|\s)\d{4}')
	xlsx_date = re.findall(x_date,link)[0]
	

	# handles various possible formats for dates
	# assign to a datetime object 'current'
	if '_' in xlsx_date:
		current = dt.datetime.strptime(xlsx_date,'%m_%d_%Y')
	elif '-' in xlsx_date:
		current = dt.datetime.strptime(xlsx_date,'%m-%d-%Y')
	elif ' ' in xlsx_date:
		current = dt.datetime.strptime(xlsx_date,'%m %d %Y')

	# reformat dates and assign to str
	str = current.strftime('%Y-%m-%d')

	if current != previous:
		# if TRUE: site has been updated; OK to continue
		print(f'Site UPDATED! current date of spreadsheet is {str}')
		print('OK to continue')
	else:
		print(f'Site NOT updated: current date of spreadsheet is {str}')
	return link, current

def main(previous):
	previous = get_date()
	compare(previous)


if __name__ == "__main__":
	main(*sys.argv)



