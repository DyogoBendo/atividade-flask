from flask import Blueprint

from controllers.UserController import store, show, update, delete, logout

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/create', methods=['POST'])(store)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)
user_bp.route('/logout', methods=['GET'])(logout)
