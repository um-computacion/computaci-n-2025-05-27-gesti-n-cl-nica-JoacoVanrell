from datetime import datetime
from src.Paciente import Paciente
from src.Medico import Medico

class RecetaInvalidaException(Exception):
    """Se lanza cuando se intenta emitir una receta sin medicamentos."""
    pass

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not medicamentos:
            raise RecetaInvalidaException("Debe indicar al menos un medicamento.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        f_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        meds = ", ".join(self.__medicamentos)
        return (
            f"Receta - {self.__paciente.obtener_dni()} por "
            f"{self.__medico.obtener_matricula()} el {f_str}: {meds}"
        )

    def obtener_paciente(self) -> Paciente:
        return self.__paciente

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_medicamentos(self) -> list[str]:
        return self.__medicamentos

    def obtener_fecha(self) -> datetime:
        return self.__fecha
