#
# File: 		build_station.py
# Author:		Sky Hoffert
# Last Modified:	Nov 2, 2017
# Description:		This file runs a simple script to build a space station.
#			Uses the calculate_COM python object
#			WIP
#
# Python Version:	TODO -- determine py version
#

# WIP
# Started Nov 2, 2017

from calculate_COM import calculate_COM

# create the object
com_calc = calculate_COM()

com_calc.add_object(0, 10000)
com_calc.add_object(10, 1000)

print(com_calc.get_objects())
print(com_calc.add_object.__doc__)
