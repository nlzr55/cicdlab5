import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_zero_side(self):
        self.assertEqual(area(10, 0), 0.0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100.0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4), 10.0, places=7)

    def test_area_raises_on_negative(self):
        with self.assertRaises(ValueError):
            area(-1, 5)

    def test_perimeter_basic(self):
        self.assertEqual(perimeter(5, 10), 30.0)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 7), 14.0)

    def test_perimeter_raises_on_negative(self):
        with self.assertRaises(ValueError):
            perimeter(3, -2)


if __name__ == '__main__':
    unittest.main()  
