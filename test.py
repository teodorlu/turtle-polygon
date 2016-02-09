import unittest
import turtle_polygon

			

class TestTurtlePolygon(unittest.TestCase):

	def assert_letter_equal(self, l1, l2):
		for (p1, p2) in zip(l1, l2):
			for ((x1, y1), (x2, y2)) in zip(p1, p2):
				self.assertAlmostEqual(x1, x2)
				self.assertAlmostEqual(y1, y2)

	def test_map_letter(self):
		def shift_x_100(tup):
			(x, y) = tup
			return (x+100, y)

		origin = [[(0,0)]]
		expected_shifted_origin = [[(100,0)]]
		shifted_origin = turtle_polygon.map_letter(shift_x_100, origin)
		self.assert_letter_equal(expected_shifted_origin, shifted_origin)

	def test_translator_x(self):
		origin = [[(0,0)]]
		expected_shifted_origin = [[(100,0)]]

		delta = (100, 0)
		shifted_origin = turtle_polygon.translate_letter(origin, delta)
		self.assert_letter_equal(expected_shifted_origin, shifted_origin)

	def test_concat(self):
		xss = [[1,2,3], [4, 5,6]]
		ys = [1, 2, 3, 4, 5, 6]
		for (x, y) in zip(turtle_polygon.concat(xss), ys):
			self.assertEqual(x, y)

if __name__ == '__main__':
	unittest.main()
