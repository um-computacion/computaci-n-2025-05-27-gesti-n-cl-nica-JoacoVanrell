from datetime import datetime
from src.Paciente import Paciente
from src.Medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__paciente__: Paciente = paciente
        self.__medico__: Medico = medico
        self.__fecha_hora__: datetime = fecha_hora
        self.__especialidad__: str = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico__

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora__

    def __str__(self) -> str:
        f = self.__fecha_hora__.strftime("%d/%m/%Y %H:%M")
        return (f"Turno - {self.__paciente__.obtener_dni()} con "
                f"{self.__medico__.obtener_matricula()} el {f} "
                f"({self.__especialidad__})")
