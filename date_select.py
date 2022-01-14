#!/usr/bin/env python
# coding: utf-8

""" This program/module takes as input dates and returns datetime
objects. Default start/stop is 2021-10-01 to 2021-10-31.
For custom stop date, default is today """

import pandas as pd
import sys
from pandas.tseries.offsets import MonthEnd

def date_maker ():
	print (' Select START date' )

	while True:
		try:
			start = input() or "2021-10"
			start = pd.to_datetime(start)
			break
		except:
			print('Not a date. Enter a START date')

	#stop = start + MonthEnd(1)
	stop = today
	print(f'START:\t {start}')
	print(f'STOP:\t {stop}')

	custom = input ('Select custom STOP date? (y/n)  ' )

	if custom == 'y':
		# User is given 5 attempts
		for n in range (5):
			n = n+1
			try:
				stop = input('Enter a STOP date  ') or pd.to_datetime("today")
				stop = pd.to_datetime(stop)
				break
			except:
				print('Not a date. Enter a STOP date  ')

	print()
	print(f'START:\t {start}')
	print(f'STOP:\t {stop}')
	return start, stop

def main ():
	date_maker()


if __name__ == "__main__":
	main()
