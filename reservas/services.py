import requests

class RequestError(Exception):
    ...

class reservasService:

    def __init__(self):
        ...

        
    def validar_entidades(self, turma_id: int, professor_id: int) -> dict:

        valida_turma = requests.get(f"http://localhost:8000/turmas/{turma_id}")
        valida_professor = requests.get(f"http://localhost:8000/professores/{professor_id}")

        return {"valida_turma_status_code": valida_turma.status_code,
                "valida_professor_status_code": valida_professor.status_code}
    
    def get_turmas_disponiveis(self):
        
        response_turmas = requests.get("http://127.0.0.1:8000/turmas")

        if response_turmas.status_code != 200:
            raise RecursionError("não foi possivel buscar turmas")

        return response_turmas.json()
    
