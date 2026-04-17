import logging

from flask import Blueprint, jsonify

from executor.totp import generate_executor_impl

log = logging.getLogger(__name__)

totp_bp = Blueprint('totp', __name__, url_prefix='/totp')


@totp_bp.route('/generate', methods=['GET'])
def health():
    service_response = generate_executor_impl.execute()
    return jsonify(service_response.model_dump()), 200
