from database.database import DatabaseManager
from reservas.services import reservasService
from sqlalchemy import text

class ModelReservas:

    def get_reservas(self):
        sql = "SELECT * FROM reservas ORDER BY data, hora_inicio"
        return DatabaseManager().select_all(sql)

    def criar_reserva(self, reserva: dict) -> dict:
        sql = text("""
            INSERT INTO reservas (turma_id, professor_id, sala, data, hora_inicio, hora_fim)
            VALUES (:turma_id, :professor_id, :sala, :data, :hora_inicio, :hora_fim)
            RETURNING id
        """)

        with DatabaseManager.engine.begin() as conn:
            result = conn.execute(sql, {
                "turma_id": reserva["turma_id"],
                "professor_id": reserva["professor_id"],
                "sala": reserva["sala"],
                "data": reserva["data"],
                "hora_inicio": reserva["hora_inicio"],
                "hora_fim": reserva["hora_fim"]
            })
            reserva_id = result.fetchone()[0]

        reserva["id"] = reserva_id
        return reserva
    
    def validar_entidades(self, turma_id: int, professor_id: int) -> dict:

        response = reservasService().validar_entidades(turma_id, professor_id)

        if response["valida_turma_status_code"] != 200:
            return {"error": "Turma não existe"}
        
        if response["valida_professor_status_code"] != 200:
            return {"error": "Professor não existe"}
        
        return {}
    
    def get_turmas_disponiveis(self) -> list:

        turmas = reservasService().get_turmas_disponiveis()

        if not turmas:
            return []

        return [turma for turma in turmas if turma["ativo"] == True]
