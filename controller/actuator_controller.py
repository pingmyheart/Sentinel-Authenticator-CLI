import logging

from flasgger import swag_from
from flask import Blueprint, jsonify

log = logging.getLogger(__name__)

actuator_bp = Blueprint('actuator', __name__, url_prefix='/actuator')


@actuator_bp.route('/health', methods=['GET'])
@swag_from('actuator_health.yaml')
def health():
    log.debug("[INCOMING REQUEST] - Health actuator")
    return jsonify(status="healthy"), 200


@actuator_bp.route('/readiness', methods=['GET'])
@swag_from('actuator_readiness.yaml')
def readiness():
    log.debug("[INCOMING REQUEST] - Ready actuator")
    return jsonify(status="ready"), 200
