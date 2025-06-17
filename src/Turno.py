from datetime import datetime
from src.Paciente import Paciente
from src.Medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if paciente is None:
            raise ValueError("El paciente no puede ser None.")
        if medico is None:
            raise ValueError("El médico no puede ser None.")
        if fecha_hora is None:
            raise ValueError("La fecha y hora del turno no pueden ser None.")
        if not especialidad.strip():
            raise ValueError("La especialidad del turno no puede estar vacía.")
        
        self.__paciente: Paciente = paciente
        self.__medico: Medico = medico
        self.__fecha_hora: datetime = fecha_hora
        self.__especialidad: str = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        f = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        return (f"Turno - {self.__paciente.obtener_dni()} con "
                f"{self.__medico.obtener_matricula()} el {f} "
                f"({self.__especialidad})")
