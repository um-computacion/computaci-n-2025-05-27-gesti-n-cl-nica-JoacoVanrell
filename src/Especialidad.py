from typing import List

class Especialidad:
    def __init__(self, tipo: str, dias: List[str]):
        if not dias:
            raise ValueError("Una especialidad debe tener al menos un día disponible.")
        if not tipo.strip():
            raise ValueError("El tipo de especialidad no puede estar vacío.")
        if not dias or any(not d.strip() for d in dias):
            raise ValueError("Cada día debe ser una cadena válida no vacía.")
        
        self.__tipo: str = tipo
        self.__dias: List[str] = [d.strip().lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.strip().lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
