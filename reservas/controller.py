from flask import Blueprint, request, jsonify
from reservas.model import ModelReservas 
from datetime import datetime

reservas_blueprint = Blueprint("reserva", __name__)

@reservas_blueprint.route("/turmas_disponiveis", methods=["GET"])
def get_turmas():

    response = ModelReservas().get_turmas_disponiveis()

    if not response:
        return jsonify(msg="nenhuma turma encontrada"), 200

    return jsonify(response), 200


@reservas_blueprint.route("/reservas", methods=["GET"])
def get_reservas():
    response = ModelReservas().get_reservas()

    if not response:
        return jsonify(msg="Nenhuma reserva registrada"), 200

    reservas = []
    for r in response:
        reserva_dict = dict(r._mapping)
        reserva_dict["data"] = reserva_dict["data"].strftime("%Y-%m-%d")
        reserva_dict["hora_inicio"] = reserva_dict["hora_inicio"].strftime("%H:%M")
        reserva_dict["hora_fim"] = reserva_dict["hora_fim"].strftime("%H:%M")
        reservas.append(reserva_dict)

    return jsonify(reservas=reservas), 200

@reservas_blueprint.route("/reservar_sala", methods=["POST"])
def criar_reserva():
    dados = request.get_json()

    turma_id = dados.get("turma_id", "")
    professor_id = dados.get("professor_id", "")
    sala = dados.get("sala", "")
    data_str = dados.get("data", "")
    hora_inicio_str = dados.get("hora_inicio", "")
    hora_fim_str = dados.get("hora_fim", "")

    # Validação de existência de turma e professor
    valida_entidades = ModelReservas().validar_entidades(turma_id, professor_id)

    if valida_entidades.get("error"):
        return jsonify(error=valida_entidades["error"]), 400

    # Converte strings para date e time
    try:
        data = datetime.strptime(data_str, "%Y-%m-%d").date()
        hora_inicio = datetime.strptime(hora_inicio_str, "%H:%M").time()
        hora_fim = datetime.strptime(hora_fim_str, "%H:%M").time()
    except ValueError:
        return jsonify(error="Formato de data ou hora inválido"), 400

    nova_reserva = {
        "turma_id": turma_id,
        "professor_id": professor_id,
        "sala": sala,
        "data": data,
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim
    }

    reserva_criada = ModelReservas().criar_reserva(nova_reserva)

    # Serializa date/time
    reserva_criada["data"] = reserva_criada["data"].strftime("%Y-%m-%d")
    reserva_criada["hora_inicio"] = reserva_criada["hora_inicio"].strftime("%H:%M")
    reserva_criada["hora_fim"] = reserva_criada["hora_fim"].strftime("%H:%M")

    return jsonify({"msg": "Reserva criada com sucesso!", "reserva": reserva_criada}), 201


    

    
    


