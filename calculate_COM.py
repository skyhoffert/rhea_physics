#
# File: 		calculate_COM.py
# Author:		Sky Hoffert
# Last Modified:	Nov 1, 2017
# Description:		This file creates an object that is capable of calculating the center of mass for a given configuration of objects
#			WIP: Inputs can be provided continuously until an entire object is build
#
# Python Version:	TODO -- determine py version
#

# WIP
# Started Nov 1, 2017

class calculate_COM:
	"""Calculate Center of Mass Object"""

	def __init__(self):
		self.objects = []

	def get_objects(self):
		"""Return list of objects"""
		return self.objects

	def add_object(self, distance, mass):
		"""Add an object by distance and mass to object list
		arg1: distance (in meters)
		arg2: mass     (in kilograms)
		"""
		self.objects.append([distance, mass])

# TODO -- most things ;)
