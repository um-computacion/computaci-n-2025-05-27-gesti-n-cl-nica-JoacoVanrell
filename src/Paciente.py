from datetime import datetime

class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: str):
        # fecha_nacimiento en formato "dd/mm/aaaa"
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Fecha inválida: {fecha_nacimiento}. Use dd/mm/aaaa.")
        self.__dni__: str = dni
        self.__nombre__: str = nombre
        self.__fecha_nacimiento__: str = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni__

    def __str__(self) -> str:
        return f"{self.__nombre__} ({self.__dni__}) - Nac: {self.__fecha_nacimiento__}"
