from datetime import datetime

class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: str):
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Fecha inválida: {fecha_nacimiento}. Use dd/mm/aaaa.")
        self.__dni: str = dni
        self.__nombre: str = nombre
        self.__fecha_nacimiento: str = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre} ({self.__dni}) - Nac: {self.__fecha_nacimiento}"
