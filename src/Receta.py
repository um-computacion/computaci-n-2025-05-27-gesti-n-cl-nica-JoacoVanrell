from datetime import datetime
from typing import List
from src.Paciente import Paciente
from src.Medico import Medico
from src.Clinica import RecetaInvalidaException


class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, medicamentos: List[str]):
        if not medicamentos:
            raise RecetaInvalidaException("La lista de medicamentos no puede estar vacía.")
        self.__paciente__: Paciente = paciente
        self.__medico__: Medico = medico
        self.__fecha_hora__: datetime = fecha_hora
        self.__medicamentos__: List[str] = medicamentos

    def __str__(self) -> str:
        f = self.__fecha_hora__.strftime("%d/%m/%Y %H:%M")
        meds = ", ".join(self.__medicamentos__)
        return (f"Receta - {self.__paciente__.obtener_dni()} por "
                f"{self.__medico__.obtener_matricula()} el {f}: {meds}")
