import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.HistoriaClinica import HistoriaClinica
from src.Paciente import Paciente
from src.Turno import Turno
from src.Receta import Receta
from src.Medico import Medico
from src.Especialidad import Especialidad
from datetime import datetime

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("1111", "Test", "01/01/1990")
        self.historia = HistoriaClinica(self.paciente)
        especialidad = Especialidad("X", ["lunes"])
        self.medico = Medico("M-1", "Doc", [especialidad])
        self.fecha_hora = datetime(2025, 6, 1, 8, 0)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, "X")
        self.receta = Receta(self.paciente, self.medico, ["A"])

    def test_lista_turnos_empieza_vacia(self):
        self.assertEqual(self.historia.obtener_turnos(), [])

    def test_lista_recetas_empieza_vacia(self):
        self.assertEqual(self.historia.obtener_recetas(), [])

    def test_agregar_turno_funciona(self):
        self.historia.agregar_turno(self.turno)
        self.assertEqual(self.historia.obtener_turnos(), [self.turno])

    def test_agregar_receta_funciona(self):
        self.historia.agregar_receta(self.receta)
        self.assertEqual(self.historia.obtener_recetas(), [self.receta])

    def test_lista_turnos_no_puede_modificarse_por_fuera(self):
        copia = self.historia.obtener_turnos()
        copia.append("falso")
        self.assertNotIn("falso", self.historia.obtener_turnos())

    def test_lista_recetas_no_puede_modificarse_por_fuera(self):
        copia = self.historia.obtener_recetas()
        copia.append("falso")
        self.assertNotIn("falso", self.historia.obtener_recetas())

    def test_str_con_historia_vacia(self):
        texto = str(self.historia)
        self.assertIn("TURNOS", texto)
        self.assertIn("RECETAS", texto)

    def test_str_con_datos_muestra_todo(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        texto = str(self.historia)
        self.assertIn(str(self.turno), texto)
        self.assertIn(str(self.receta), texto)

    def test_str_sin_turnos_muestra_guion(self):
        self.historia.agregar_receta(self.receta)
        texto = str(self.historia).split("RECETAS:")[0]
        self.assertIn("—", texto)

    def test_str_sin_recetas_muestra_guion(self):
        self.historia.agregar_turno(self.turno)
        texto = str(self.historia).split("TURNOS:")[1]
        self.assertIn("—", texto)


if __name__ == "__main__":
    unittest.main()
