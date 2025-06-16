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
        self.__pacientes: dict[str, Paciente] = {}
        self.__medicos: dict[str, Medico] = {}
        self.__turnos: List[Turno] = []
        self.__historias: dict[str, HistoriaClinica] = {}


    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"Paciente {dni} no registrado.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException(f"Médico {matricula} no registrado.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(f"Turno ocupado: {matricula} → {fecha_hora}")

    @staticmethod
    def obtener_dia_semana_en_espanol(fecha_hora: datetime) -> str:
        dias = {
            "Monday": "lunes", "Tuesday": "martes", "Wednesday": "miércoles",
            "Thursday": "jueves", "Friday": "viernes",
            "Saturday": "sábado", "Sunday": "domingo"
        }
        return dias[fecha_hora.strftime("%A")]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> Optional[str]:
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad: str, dia_semana: str):
        disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if disponible is None or disponible.lower() != especialidad.lower():
            raise MedicoNoDisponibleException(
                f"{medico.obtener_matricula()} no atiende {especialidad} los {dia_semana}"
            )

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias[dni]


    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"Ya existe paciente {dni}.")
        self.__pacientes[dni] = paciente
        self.__historias[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Ya existe médico {matricula}.")
        self.__medicos[matricula] = medico

    def agendar_turno(self, dni: str, matricula: str, fecha_hora: datetime, especialidad: str):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        medico = self.__medicos[matricula]
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        paciente = self.__pacientes[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias[dni].agregar_turno(turno)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: List[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        if not medicamentos:
            raise RecetaInvalidaException("Debe indicar al menos un medicamento.")

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias[dni].agregar_receta(receta)

    def obtener_pacientes(self) -> List[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> List[Medico]:
        return list(self.__medicos.values())

    def obtener_turnos(self) -> List[Turno]:
        return list(self.__turnos)