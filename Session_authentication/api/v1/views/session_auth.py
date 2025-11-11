#!/usr/bin/env python3
""" Session authentication module """

from api.v1.views import app_views
import os
from flask import jsonify, request, abort


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    JSON body:
      - email: string
      - password: string
    Return:
      - User object JSON represented
      - 400 if email is missing
      - 400 if password is missing
      - 401 if no User found or if password is wrong
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({ "error": "email missing" }), 400
    if password is None:
        return jsonify({ "error": "password missing" }), 400
    from models.user import User

    users = User.search({'email': email})
    if not users:
        return jsonify({ "error": "no user found for this email" }), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return response


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False
)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - Empty JSON object
      - 404 if no session found
    """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        return abort(404)
    return jsonify({}), 200
