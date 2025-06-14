from datetime import datetime
from src.Paciente import Paciente
from src.Medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
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
