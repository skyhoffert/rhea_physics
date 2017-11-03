#
# File: 		test_calculate_COM.py
# Author:		Sky Hoffert
# Last Modified:	Nov 1, 2017
# Description:		This file tests all aspects of the implementation of calculate_COM.py
#			WIP: Defining and running test cases
#
# Python Version:	2.7.13
#

# WIP
# Started Nov 1, 2017

import unittest
import doctest
from calculate_COM import calculate_COM

class Test_Instantiation(unittest.TestCase):

	def test(self):
		com_calc = calculate_COM()
		self.assertEqual(com_calc, not None)

	def test_doc(self):
		doctest.testmod()

# TODO -- more test cases

if __name__ == '__main__':
	unittest.main()
