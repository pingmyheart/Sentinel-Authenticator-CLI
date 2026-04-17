import logging

from flask import Blueprint, jsonify

log = logging.getLogger(__name__)

actuator_bp = Blueprint('actuator', __name__, url_prefix='/actuator')


@actuator_bp.route('/health', methods=['GET'])
def health():
    log.debug("[INCOMING REQUEST] - Health actuator")
    return jsonify(status="healthy"), 200


@actuator_bp.route('/readiness', methods=['GET'])
def readiness():
    log.debug("[INCOMING REQUEST] - Ready actuator")
    return jsonify(status="ready"), 200
