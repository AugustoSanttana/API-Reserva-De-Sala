from database.database import db
from datetime import datetime

class ModelReservas:
    def get_reservas(self):
        return db["reservas"]

    def criar_reserva(self, reserva):
        db["reservas"].append(reserva)
        return reserva









"""from database.database import DatabaseManager

class ModelReservas:
    def __init__(self) -> None:
        ...

    def get_reservas(self):
        return DatabaseManager().select_all("SELECT * FROM reservas")"""
