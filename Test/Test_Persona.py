import unittest
from Prod.Persona import *


class MyTestCase(unittest.TestCase):
    def test_persona(self):
        persona1: Persona = Persona("Hector", "Lara", "Salas", "Employee", "hectorlaras.18@gmail.com", 8121987742)
        resultado: str = persona1.__str__()
        self.assertEqual(resultado, "Hector Lara Salas: Employee")


if __name__ == '__main__':
    unittest.main()
