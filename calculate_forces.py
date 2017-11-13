#
# File: 			calculate_forces.py
# Author:			Sky Hoffert
# Last Modified:	Nov 13, 2017
# Description:		This file creates an object that is capable of calculating the forces for a given configuration of objects
#
# Python Version:	3.7
#

# WIP
# Started Nov 13, 2017

import math

class calculate_forces:
	"""
	Calculate Forces Object
	"""

	def __init__(self):
		self._mass_module = 0
		self._mass_counterweight = 0
		self._radius_module = 0
		self._radius_module_inner = 0
		self._radius_counterweight = 0
		self._force_module = 0
		self._force_counterweight = 0
		self._force_module_top = 0
		self._gravity_scale_factor = 1
		
	# ---------------- mass_module ----------------
	@property
	def mass_module(self):
		return self._mass_module
	
	@mass_module.setter
	def mass_module(self, value):
		self._mass_module = value
		
	# ---------------- mass_counterweight ----------------
	@property
	def mass_counterweight(self):
		return self._mass_counterweight
	
	@mass_counterweight.setter
	def mass_counterweight(self, value):
		self._mass_counterweight = value
		
	# ---------------- radius_module ----------------
	@property
	def radius_module(self):
		return self._radius_module
	
	@radius_module.setter
	def radius_module(self, value):
		self._radius_module = value
		
	# ---------------- radius_module_inner ----------------
	@property
	def radius_module_inner(self):
		return self._radius_module_inner
	
	@radius_module_inner.setter
	def radius_module_inner(self, value):
		self._radius_module_inner = value
		
	# ---------------- radius_counterweight ----------------
	@property
	def radius_counterweight(self):
		return self._radius_counterweight
	
	@radius_counterweight.setter
	def radius_counterweight(self, value):
		self._radius_counterweight = value
		
	# ---------------- force_module ----------------
	@property
	def force_module(self):
		return self._force_module
	
	@force_module.setter
	def force_module(self, value):
		self._force_module = value
		
	# ---------------- force_counterweight ----------------
	@property
	def force_counterweight(self):
		return self._force_counterweight
	
	@force_counterweight.setter
	def force_counterweight(self, value):
		self._force_counterweight = value
		
	# ---------------- force_module_top ----------------
	@property
	def force_module_top(self):
		return self._force_module_top
	
	@force_module_top.setter
	def force_module_top(self, value):
		self._force_module_top = value
		
	# ---------------- gravity_scale_factor ----------------
	@property
	def gravity_scale_factor(self):
		return self._gravity_scale_factor
	
	@gravity_scale_factor.setter
	def gravity_scale_factor(self, value):
		self._gravity_scale_factor = value

	# ---------------- run ----------------
	def run(self):
		omega = math.sqrt(self._gravity_scale_factor * 9.81 / self._radius_module)
		
		self._force_module = math.pow(omega, 2) * self._radius_module * self._mass_module
		
		d_cm = self._radius_module
		m_t  = self._mass_counterweight + self._mass_module
		self._radius_counterweight = (d_cm * m_t / self._mass_counterweight) - self._radius_module
		
		self._force_counterweight = math.pow(omega, 2) * self._radius_counterweight * self._mass_counterweight
		
		self._force_module_top = math.pow(omega, 2) * self._radius_module_inner
		
	def __str__(self):
		val =       'Force on module:         {:.2f} N\n'.format(self.force_module)
		val = val + 'Force on counterweight:  {:.2f} N\n'.format(self.force_counterweight)
		val = val + 'Accel of inner:          {:.2f} m/s^2\n'.format(self.force_module_top)
		val = val + '                       = {:.2f} g\n'.format(self.force_module_top / 9.81)
		val = val + 'Radius of counterweight: {:.2f} m\n'.format(self.radius_counterweight)
		
		return val
		
		
		
		
		
