from typing import List, Optional
from src.Especialidad import Especialidad

class Medico:
    def __init__(self, matricula: str, nombre: str, especialidades: Optional[List[Especialidad]] = None):
        if not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía.")
        if not nombre.strip():
            raise ValueError("El nombre del médico no puede estar vacío.")
        
        self.__matricula: str = matricula
        self.__nombre: str = nombre
        self.__especialidades: List[Especialidad] = especialidades or []

    def agregar_especialidad(self, esp: Especialidad):
        if not isinstance(esp, Especialidad):
            raise TypeError("La especialidad debe ser instancia de Especialidad.")
        # evitar duplicados por tipo
        if any(e.obtener_especialidad() == esp.obtener_especialidad() for e in self.__especialidades):
            raise ValueError(f"Ya existe la especialidad {esp.obtener_especialidad()} para este médico.")
        self.__especialidades.append(esp)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        for e in self.__especialidades:
            if e.verificar_dia(dia):
                return e.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = "\n  ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, {self.__matricula}, [\n  {especialidades_str}\n]"

