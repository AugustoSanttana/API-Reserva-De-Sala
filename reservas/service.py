import requests

class reservasService:

    def __init__(self):
        ...

    def get_turmas(self):
        turmas = requests.get("http://localhost:8000/turmas")
        return turmas
        
    def validar_entidades(self, turma_id: int, professor_id: int) -> dict:

        valida_turma = requests.get(f"http://localhost:8000/turmas/{turma_id}")
        valida_professor = requests.get(f"http://localhost:8000/professores/{professor_id}")

        return {"valida_turma_status_code": valida_turma.status_code,
                "valida_professor_status_code": valida_professor.status_code}
    
