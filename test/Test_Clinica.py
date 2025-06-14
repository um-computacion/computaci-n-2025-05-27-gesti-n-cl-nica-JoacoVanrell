import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime, timedelta
from src.Clinica import (
    Clinica, Paciente, Medico,
    PacienteNoEncontradoException, MedicoNoDisponibleException,
    TurnoOcupadoException, RecetaInvalidaException
)
from src.Especialidad import Especialidad


class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("1111", "Test", "01/01/1990")
        self.medico = Medico("M-1", "Doc")
        especialidad = Especialidad("Cardiología", ["lunes"])
        self.medico.agregar_especialidad(especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

        hoy = datetime.now()
        dias_hasta_lunes = (0 - hoy.weekday() + 7) % 7 or 7
        self.fecha_lunes = (hoy + timedelta(days=dias_hasta_lunes)).replace(hour=10, minute=0, second=0, microsecond=0)

    def test_agregar_paciente_funciona(self):
        nuevo = Paciente("2222", "Otro", "02/02/1990")
        self.clinica.agregar_paciente(nuevo)
        self.assertIn("2222", [p.obtener_dni() for p in self.clinica.obtener_pacientes()])

    def test_agregar_medico_funciona(self):
        otro = Medico("M-2", "Dr. Otro")
        self.clinica.agregar_medico(otro)
        self.assertIn("M-2", [m.obtener_matricula() for m in self.clinica.obtener_medicos()])

    def test_agregar_medico_duplicado_falla(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_exitoso(self):
        self.clinica.agendar_turno("1111", "M-1", self.fecha_lunes, "Cardiología")
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)
        historia = self.clinica.obtener_historia_clinica_por_dni("1111")
        self.assertEqual(len(historia.obtener_turnos()), 1)

    def test_agendar_turno_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("9999", "M-1", self.fecha_lunes, "Cardiología")

    def test_agendar_turno_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("1111", "M-999", self.fecha_lunes, "Cardiología")

    def test_agendar_turno_duplicado(self):
        self.clinica.agendar_turno("1111", "M-1", self.fecha_lunes, "Cardiología")
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("1111", "M-1", self.fecha_lunes, "Cardiología")

    def test_agendar_turno_especialidad_no_disponible(self):
        martes = self.fecha_lunes + timedelta(days=1)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("1111", "M-1", martes, "Cardiología")

    def test_emitir_receta_exitosamente(self):
        self.clinica.emitir_receta("1111", "M-1", ["Aspirina"])
        historia = self.clinica.obtener_historia_clinica_por_dni("1111")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_sin_medicamentos_falla(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("1111", "M-1", [])


if __name__ == "__main__":
    unittest.main()

