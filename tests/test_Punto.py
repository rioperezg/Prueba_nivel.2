import unittest
import Punto
class TestDatabase(unittest.TestCase):
      def test_Punto__str__(self):
            P = Punto(2, 3)
            PuntoA_creado = P.__init__()
            self.assertEqual(PuntoA_creado, "Punto:(2,3)")