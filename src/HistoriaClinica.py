from datetime import datetime
from typing import List
from src.Paciente import Paciente
from src.Turno import Turno
from src.Receta import Receta


class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente__: Paciente = paciente
        self.__turnos__: List[Turno] = []
        self.__recetas__: List[Receta] = []

    def agregar_turno(self, turno: Turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta: Receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self) -> List[Turno]:
        return list(self.__turnos__)

    def obtener_recetas(self) -> List[Receta]:
        return list(self.__recetas__)

    def __str__(self) -> str:
        t = "\n".join(str(x) for x in self.__turnos__) or "—"
        r = "\n".join(str(x) for x in self.__recetas__) or "—"
        return (f"Historia de {self.__paciente__.obtener_dni()}:\n"
                f"TURNOS:\n{t}\nRECETAS:\n{r}")
