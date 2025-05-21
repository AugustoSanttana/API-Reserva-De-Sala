from flask import Blueprint, request, jsonify
from models.reservas import ModelReservas

reservas_blueprint = Blueprint("reserva", __name__)

@reservas_blueprint.route("/reservas", methods=["GET"])
def get_reservas():
    response = ModelReservas().get_reservas()
    if not response:
        return jsonify(msg="nenhuma reserva registrada"), 200
    return jsonify(reservas=response)


