import unittest

from data_type import data_type


class DataTypeTestCase(unittest.TestCase):

	def test_none_type(self):
		self.assertEqual('no value', data_type(None))

	def test_boolean_type(self):
		self.assertEqual(True, data_type(True))

	def test_longlist_type(self):
		self.assertEqual(4, data_type([2,3,4]))

	def test_shortlist_type(self):
		self.assertEqual(None, data_type([2,3]))

	def test_string_type(self):
		self.assertEqual(4, data_type("Hapa"))

if __name__ == '__main__':
	unittest.main()