#!/usr/bin/env python
# coding: utf-8

""" This program/module takes as input dates as strings and coverts them to
datetime objects. It returns them as the variables start and stop"""

import pandas as pd
import sys
from pandas.tseries.offsets import MonthEnd

def date_maker ():
	print (' Select START date' )

	while True:
		try:
			start = input()
			start = pd.to_datetime(start)
			break
		except:
			print('Not a date. Enter a START date')

	stop = start + MonthEnd(1)
	print(f'START:\t {start}')
	print(f'STOP:\t {stop}')

	custom = input ('Select custom STOP date? (y/n)  ' )

	if custom == 'y':
		for n in range (5):
			n = n+1
			try:
				stop = input('Enter a STOP date  ')
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
