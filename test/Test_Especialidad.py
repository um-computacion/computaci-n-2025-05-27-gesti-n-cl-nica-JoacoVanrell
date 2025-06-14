import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.Especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida(self):
        e = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.assertEqual(e.obtener_especialidad(), "Pediatría")

    def test_no_se_puede_crear_sin_dias(self):
        with self.assertRaises(ValueError):
            Especialidad("X", [])

    def test_dias_guardados_en_minusculas(self):
        e = Especialidad("X", ["Lunes", "Martes"])
        self.assertTrue(e.verificar_dia("lunes"))
        self.assertTrue(e.verificar_dia("MARTES"))
        self.assertFalse(e.verificar_dia("miércoles"))

    def test_verificacion_no_sensible_a_mayusculas(self):
        e = Especialidad("X", ["martes"])
        self.assertTrue(e.verificar_dia("MARTES"))
        self.assertTrue(e.verificar_dia("MarTes"))

    def test_verificacion_dia_que_no_atiende(self):
        e = Especialidad("X", ["lunes"])
        self.assertFalse(e.verificar_dia("martes"))

    def test_str_incluye_todo_correctamente(self):
        e = Especialidad("Cardiología", ["Lunes", "Viernes"])
        texto = str(e)
        self.assertIn("Cardiología", texto)
        self.assertIn("lunes", texto)
        self.assertIn("viernes", texto)

    def test_espacios_en_dias_son_eliminados(self):
        e = Especialidad("X", [" Lunes ", " Martes"])
        self.assertTrue(e.verificar_dia("lunes"))
        self.assertTrue(e.verificar_dia("martes"))

    def test_verifica_varios_dias(self):
        dias = ["lunes", "miércoles", "viernes"]
        e = Especialidad("Y", dias)
        for dia in dias:
            self.assertTrue(e.verificar_dia(dia))

    def test_obtener_nombre_especialidad(self):
        e = Especialidad("Test", ["lunes"])
        self.assertEqual(e.obtener_especialidad(), "Test")

    def test_str_muestra_todos_los_dias(self):
        dias = ["lunes", "martes"]
        e = Especialidad("E", dias)
        texto = str(e)
        for dia in dias:
            self.assertIn(dia, texto)


if __name__ == "__main__":
    unittest.main()

