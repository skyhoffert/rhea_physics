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
from calculate_forces import calculate_forces

print('---------------- COM ----------------')
com_calc = calculate_COM()

com_calc.add_object(0, 10000)
com_calc.add_object(10, 1000)

print(com_calc.get_objects())
#print(com_calc.add_object.__doc__)
print('\n')

print('---------------- Forces ----------------')
f_calc = calculate_forces()

f_calc.mass_module =          3000 # kg
f_calc.mass_counterweight =   1000 # kg
f_calc.radius_module =        50   # m
f_calc.radius_module_inner =  48   # m

f_calc.run()

print(f_calc)
