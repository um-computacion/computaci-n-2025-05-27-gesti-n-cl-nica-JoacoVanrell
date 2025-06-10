from datetime import datetime
from typing import List, Optional
from src.Paciente import Paciente
from src.Medico import Medico
from src.Turno import Turno
from src.Receta import Receta
from src.HistoriaClinica import HistoriaClinica


class PacienteNoEncontradoException(Exception):
    """Se lanza cuando un paciente no está registrado."""
    pass

class MedicoNoDisponibleException(Exception):
    """Se lanza cuando un médico no está registrado o no disponible."""
    pass

class TurnoOcupadoException(Exception):
    """Se lanza cuando ya existe un turno para ese médico en la misma fecha y hora."""
    pass

class RecetaInvalidaException(Exception):
    """Se lanza cuando se intenta emitir una receta sin medicamentos."""
    pass

class Clinica:
    def __init__(self):
        self.__pacientes__: dict[str, Paciente] = {}
        self.__medicos__:   dict[str, Medico]   = {}
        self.__turnos__:    List[Turno]         = []
        self.__historias__: dict[str, HistoriaClinica] = {}

    # — Validaciones auxiliares —
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException(f"Paciente {dni} no registrado.")

    def validar_existencia_medico(self, mat: str):
        if mat not in self.__medicos__:
            raise MedicoNoDisponibleException(f"Médico {mat} no registrado.")

    def validar_turno_no_duplicado(self, mat: str, fecha_hora: datetime):
        for t in self.__turnos__:
            if (t.obtener_medico().obtener_matricula() == mat and 
                t.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(f"Turno ocupado: {mat} → {fecha_hora}")

    @staticmethod
    def obtener_dia_semana_en_espanol(fecha_hora: datetime) -> str:
        dias = {
            "Monday":"lunes","Tuesday":"martes","Wednesday":"miércoles",
            "Thursday":"jueves","Friday":"viernes","Saturday":"sábado",
            "Sunday":"domingo"
        }
        return dias[fecha_hora.strftime("%A")]

    def obtener_especialidad_disponible(self, medico: Medico, dia_sem: str) -> Optional[str]:
        return medico.obtener_especialidad_para_dia(dia_sem)
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
            """Devuelve el Medico si existe, o lanza MedicoNoDisponibleException."""
            self.validar_existencia_medico(matricula)
            return self.__medicos__[matricula]

    def validar_especialidad_en_dia(self, medico: Medico, esp: str, dia_sem: str):
        disp = self.obtener_especialidad_disponible(medico, dia_sem)
        if disp is None or disp.lower() != esp.lower():
            raise MedicoNoDisponibleException(
                f"{medico.obtener_matricula()} no atiende {esp} los {dia_sem}"
            )

    # — Operaciones públicas —
    def agregar_paciente(self, paciente: Paciente):
        if paciente.obtener_dni() in self.__pacientes__:
            raise ValueError(f"Ya existe paciente {paciente.obtener_dni()}.")
        self.__pacientes__[paciente.obtener_dni()] = paciente
        self.__historias__[paciente.obtener_dni()] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        if medico.obtener_matricula() in self.__medicos__:
            raise ValueError(f"Ya existe médico {medico.obtener_matricula()}.")
        self.__medicos__[medico.obtener_matricula()] = medico

    def agendar_turno(self, dni: str, mat: str, fecha_hora: datetime, esp: str):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(mat)
        self.validar_turno_no_duplicado(mat, fecha_hora)

        dia_sem = Clinica.obtener_dia_semana_en_espanol(fecha_hora)
        medico = self.__medicos__[mat]
        self.validar_especialidad_en_dia(medico, esp, dia_sem)

        paciente = self.__pacientes__[dni]
        turno = Turno(paciente, medico, fecha_hora, esp)
        self.__turnos__.append(turno)
        self.__historias__[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, mat: str, medicamentos: List[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(mat)
        if not medicamentos:
            raise RecetaInvalidaException("Debe indicar al menos un medicamento.")
        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[mat]
        now = datetime.now()
        receta = Receta(paciente, medico, now, medicamentos)
        self.__historias__[dni].agregar_receta(receta)

    def obtener_pacientes(self) -> List[Paciente]:
        return list(self.__pacientes__.values())

    def obtener_medicos(self) -> List[Medico]:
        return list(self.__medicos__.values())

    def obtener_turnos(self) -> List[Turno]:
        return list(self.__turnos__)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias__[dni]