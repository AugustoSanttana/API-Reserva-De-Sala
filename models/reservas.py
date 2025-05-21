from database.database import DatabaseManager

class ModelReservas:
    def __init__(self) -> None:
        ...

    def get_reservas(self):
        return DatabaseManager().select_all("SELECT * FROM reservas")
    
