import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.Receta import Receta, RecetaInvalidaException
from src.Paciente import Paciente
from src.Medico import Medico
from src.Especialidad import Especialidad
from datetime import datetime

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("1111", "Test", "01/01/1990")
        esp = Especialidad("X", ["lunes"])
        self.medico = Medico("M-1", "Doc", [esp])

    def test_creacion_correcta(self):
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.assertIn("Ibuprofeno", str(receta))

    def test_error_si_no_hay_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [])

    def test_str_contiene_todos_los_datos(self):
        receta = Receta(self.paciente, self.medico, ["A", "B"])
        texto = str(receta)
        self.assertIn(self.paciente.obtener_dni(), texto)
        self.assertIn(self.medico.obtener_matricula(), texto)
        self.assertIn("A, B", texto)
        self.assertRegex(texto, r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}")

    def test_medicamentos_se_mantienen_en_orden(self):
        meds = ["Med1", "Med2", "Med3"]
        receta = Receta(self.paciente, self.medico, meds)
        for i, nombre in enumerate(meds):
            self.assertIn(nombre, str(receta).split(": ")[1].split(", ")[i])

    def test_fecha_generada_es_valida(self):
        receta = Receta(self.paciente, self.medico, ["X"])
        fecha = receta.obtener_fecha()
        self.assertIsInstance(fecha, datetime)

    def test_formato_str_especifico(self):
        receta = Receta(self.paciente, self.medico, ["X", "Y"])
        texto = str(receta)
        self.assertRegex(texto, rf"Receta - {self.paciente.obtener_dni()} por {self.medico.obtener_matricula()} el \d{{2}}/\d{{2}}/\d{{4}} \d{{2}}:\d{{2}}: X, Y")

    def test_lista_de_medicamentos_puede_ser_generica(self):
        meds = [1, 2, 3] 
        receta = Receta(self.paciente, self.medico, meds)
        self.assertEqual(receta.obtener_medicamentos(), meds)


if __name__ == "__main__":
    unittest.main()

