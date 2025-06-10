from typing import List

class Especialidad:
    def __init__(self, tipo: str, dias: List[str]):
        if not dias:
            raise ValueError("Una especialidad debe tener al menos un día disponible.")
        # guardamos días en minúsculas
        self.__tipo__: str = tipo
        self.__dias__: List[str] = [d.strip().lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo__

    def verificar_dia(self, dia: str) -> bool:
        return dia.strip().lower() in self.__dias__

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"
