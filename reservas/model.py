from database.database import db
from datetime import datetime
from service import reservasService

class ModelReservas:
    def get_reservas(self) -> list:
        return db["reservas"]

    def criar_reserva(self, reserva: dict) -> dict:
        db["reservas"].append(reserva)
        return reserva
    
    def validar_entidades(self, turma_id: int, professor_id: int) -> dict:

        response = reservasService().validar_entidades(turma_id, professor_id)

        if response["valida_turma_status_code"] != 200:
            return {"error": "Turma não existe"}
        
        if response["valida_professor_status_code"] != 200:
            return {"error": "Professor não existe"}
        
        return {}


"""from database.database import DatabaseManager

class ModelReservas:
    def __init__(self) -> None:
        ...

    def get_reservas(self):
        return DatabaseManager().select_all("SELECT * FROM reservas")"""
