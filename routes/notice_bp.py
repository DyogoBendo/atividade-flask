from flask import Blueprint

from controllers.NoticeController import store, show, delete

notice_bp = Blueprint('notice_bp', __name__)
notice_bp.route('/create', methods=['POST', 'GET'])(store)
notice_bp.route('/<int:notice_id>', methods=['GET'])(show)
notice_bp.route('/<int:notice_id>', methods=['GET'])(delete)
