from flask import Blueprint

from controllers.UserController import index, store, show, update, delete, logout

notice_bp = Blueprint('notice_bp', __name__)
notice_bp.route('/create', methods=['POST'])(store)
notice_bp.route('/<int:notice_id>', methods=['GET'])(show)
