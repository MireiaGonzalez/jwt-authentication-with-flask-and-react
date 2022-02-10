"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/user/register', methods=['POST'])
def new_user():
    body = request.get_json()
    new_user = User(email=body['email'], password=body['password'], is_active=True)
    return jsonify(new_user.serialize()), 200