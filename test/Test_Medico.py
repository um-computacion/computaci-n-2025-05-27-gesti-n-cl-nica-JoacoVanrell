import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.Medico import Medico
from src.Especialidad import Especialidad

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.esp1 = Especialidad("Dermatología", ["lunes"])
        self.esp2 = Especialidad("Cardiología", ["martes"])
        self.medico = Medico("M-100", "Dr. Prueba", [self.esp1])

    def test_crear_medico_sin_especialidades(self):
        medico = Medico("M-101", "Dr. SinEsp")
        self.assertEqual(medico.obtener_matricula(), "M-101")
        self.assertIsNone(medico.obtener_especialidad_para_dia("lunes"))

    def test_crear_medico_con_especialidades(self):
        medico = Medico("M-102", "Dr. ConEsp", [self.esp2])
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiología")

    def test_matricula_se_obtiene_correctamente(self):
        self.assertEqual(self.medico.obtener_matricula(), "M-100")

    def test_agregar_especialidad_correctamente(self):
        self.medico.agregar_especialidad(self.esp2)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("martes"), "Cardiología")

    def test_agregar_especialidad_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            self.medico.agregar_especialidad("esto no es una Especialidad")

    def test_agregar_especialidad_duplicada_lanza_error(self):
        with self.assertRaises(ValueError):
            self.medico.agregar_especialidad(self.esp1)

    def test_especialidad_disponible_en_dia(self):
        resultado = self.medico.obtener_especialidad_para_dia("Lunes")  # mayúscula
        self.assertEqual(resultado, "Dermatología")

    def test_especialidad_no_disponible_devuelve_none(self):
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("miércoles"))

    def test_str_incluye_datos_correctos(self):
        medico = Medico("M-200", "Dr. Representación", [self.esp1, self.esp2])
        texto = str(medico)
        self.assertIn("Dr. Representación", texto)
        self.assertIn("M-200", texto)
        self.assertIn("Dermatología", texto)
        self.assertIn("Cardiología", texto)


if __name__ == "__main__":
    unittest.main()
