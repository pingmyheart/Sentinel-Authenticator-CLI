import logging

from flasgger import swag_from
from flask import Blueprint, jsonify

from executor.totp import generate_executor_impl

log = logging.getLogger(__name__)

totp_bp = Blueprint('totp', __name__, url_prefix='/totp')


@totp_bp.route('/generate', methods=['GET'])
@swag_from('totp_generate.yaml')
def generate():
    service_response = generate_executor_impl.execute()
    return jsonify(service_response.model_dump()), 200
