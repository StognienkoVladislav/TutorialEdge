
import unittest
from PyUnit import basic

class MyModuleTest(unittest.TestCase):

    def test_calc_x(self):
        assert(basic.calc_x(2) == 4)
        assert(basic.calc_x(2) == 4)
        assert(basic.calc_x(3) == 5)

if __name__ == "__main__":
    unittest.main()