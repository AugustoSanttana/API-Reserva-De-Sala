from flask import Blueprint, request, jsonify
from reservas.model import ModelReservas 
import requests
from database.database import db
from datetime import datetime

reservas_blueprint = Blueprint("reserva", __name__)

def validar_entidades(turma_id, professor_id):
    resp = requests.get(f"http://localhost:8000/turmas/{turma_id}")
    resp2 = requests.get(f"http://localhost:8000/professores/{professor_id}")
    return resp.status_code and resp2.status_code == 200
    

@reservas_blueprint.route("/reservas", methods=["GET"])
def get_reservas():
    response = ModelReservas().get_reservas()
    if not response:
        return jsonify(msg="nenhuma reserva registrada"), 200
    return jsonify(reservas=response)

@reservas_blueprint.route("/reservar-sala", methods=["POST"])
def criar_reserva():
    dados = request.get_json()
    turma_id = dados.get("turma_id")
    professor_id = dados.get("professor_id")
    sala = dados.get("sala")
    data = dados.get("data")
    hora_inicio = dados.get("hora_inicio")
    hora_fim = dados.get("hora_fim")

    
    if not validar_entidades(turma_id):
        return jsonify({"erro":"turma ou professor não foram encontrados"}), 400
    
    nova_reserva = {
        "turma_id": turma_id,
        "professor_id": professor_id,
        "sala": sala,
        "data": datetime.strptime(data, "%Y-%m-%d").date(),
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim
    }
    
    ModelReservas().criar_reserva(nova_reserva)
    
    return jsonify({"msg": "Reserva criada com sucesso!", "reserva": nova_reserva}), 201

    

    
    


