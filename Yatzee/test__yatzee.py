import unittest

from die import Die

class DieTestCase(unittest.TestCase):

    def test_die_face_value(self):
        die = Die(6, 6)
        self.assertEqual(die.getFace(), 6)

    def test_die_face_out_of_bounds(self):
        with self.assertRaises(IndexError):
            die = Die(6, 8)

if __name__ == '__main__':
    unittest.main()