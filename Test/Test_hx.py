import unittest
from HXFunctions.HelpFunctions import *

class test_hx(unittest.TestCase):
    def test1(self):
        resultado: str = holamundo()
        self.assertEqual(resultado, "hola")

if __name__ == "__main__":
    unittest.main()