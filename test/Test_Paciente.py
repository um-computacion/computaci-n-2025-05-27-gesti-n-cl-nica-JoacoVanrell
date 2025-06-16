import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.Paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_creacion_valida(self):
        paciente = Paciente("12345678", "Juan", "22/12/2004")
        self.assertEqual(paciente.obtener_dni(), "12345678")

    def test_fecha_formato_invalido_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("12345678", "Juan", "2004-12-22")  

    def test_fecha_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("123", "A", "31/02/2020")  

    def test_fecha_sin_barras_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("123", "A", "22122004")  

    def test_fecha_con_año_corto_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("123", "A", "01/01/99")  

    def test_str_incluye_datos_correctos(self):
        paciente = Paciente("87654321", "Ana", "05/07/1995")
        texto = str(paciente)
        self.assertIn("Ana", texto)
        self.assertIn("87654321", texto)
        self.assertIn("05/07/1995", texto)

    def test_fecha_con_ceros_a_la_izquierda_es_valida(self):
        paciente = Paciente("55555555", "Zero", "05/02/2005")
        self.assertIn("05/02/2005", str(paciente))

    def test_fecha_bisiesto_valida(self):
        paciente = Paciente("66666666", "Edge", "29/02/2020")
        self.assertIn("29/02/2020", str(paciente))

    def test_dni_se_obtiene_correctamente(self):
        paciente = Paciente("44444444", "Test", "12/12/2012")
        self.assertEqual(paciente.obtener_dni(), "44444444")

    def test_fecha_almacenada_se_mantiene(self):
        fecha = "10/10/2010"
        paciente = Paciente("99999999", "Test", fecha)
        self.assertIn(fecha, str(paciente))
    
    def test_dni_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("", "Juan", "10/10/2000")


    def test_dni_con_letras_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("ABC123", "Juan", "10/10/2000")


    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("12345678", "", "10/10/2000")


    def test_mes_fuera_de_rango_lanza_error(self):
        with self.assertRaises(ValueError):
            Paciente("12345678", "Juan", "10/13/2000")  # mes 13 no existe


    def test_str_funciona_con_nombre_largo(self):
        nombre = "María del Pilar González López"
        p = Paciente("34567890", nombre, "15/05/1992")
        self.assertIn(nombre, str(p))


if __name__ == "__main__":
    unittest.main()

