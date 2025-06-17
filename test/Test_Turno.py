import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from src.Turno import Turno
from src.Paciente import Paciente
from src.Medico import Medico
from src.Especialidad import Especialidad
from datetime import datetime

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("1234", "Test", "01/01/2000")
        esp = Especialidad("General", ["lunes"])
        self.medico = Medico("M-1", "Doc", [esp])
        self.fecha_hora = datetime(2025, 6, 15, 10, 5)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, "General")

    def test_obtener_medico(self):
        self.assertIs(self.turno.obtener_medico(), self.medico)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_contiene_toda_la_info(self):
        texto = str(self.turno)
        self.assertIn(self.paciente.obtener_dni(), texto)
        self.assertIn(self.medico.obtener_matricula(), texto)
        self.assertIn("15/06/2025 10:05", texto)
        self.assertIn("(General)", texto)

    def test_formato_str_exacto(self):
        esperado = f"Turno - {self.paciente.obtener_dni()} con {self.medico.obtener_matricula()} el {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} (General)"
        self.assertEqual(str(self.turno), esperado)

    def test_formato_con_numeros_de_un_digito(self):
        dt = datetime(2025, 6, 5, 5, 5)
        turno = Turno(self.paciente, self.medico, dt, "General")
        self.assertIn("05/06/2025 05:05", str(turno))

    def test_turnos_en_dias_distintos_tienen_str_diferente(self):
        otro_turno = Turno(self.paciente, self.medico, datetime(2025, 6, 15, 11, 0), "General")
        self.assertNotEqual(str(self.turno), str(otro_turno))

    def test_especialidad_aparece_en_str(self):
        texto = str(self.turno)
        self.assertRegex(texto, r"\(General\)$")

    def test_str_falla_si_fecha_no_es_datetime(self):
        turno_invalido = Turno(self.paciente, self.medico, "no es fecha", "General")
        with self.assertRaises(AttributeError):
            _ = str(turno_invalido)
    
    def test_turno_con_paciente_none_lanza_error(self):
        with self.assertRaises(ValueError):
            Turno(None, self.medico, self.fecha_hora, "General")
    
    def test_turno_con_medico_none_lanza_error(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, self.fecha_hora, "General")
            
    def test_turno_con_fecha_hora_none_lanza_error(self):
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, None, "General")



if __name__ == "__main__":
    unittest.main()
