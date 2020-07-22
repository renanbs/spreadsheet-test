from functools import wraps
from http import HTTPStatus

import jwt
from flask import request, jsonify, current_app


def decode_token(auth_token, secret_key):
    payload = jwt.decode(auth_token, secret_key)
    return payload['email']


def build_message(status, msg):
    message = {'error': str(msg)}
    resp = jsonify(message)
    resp.status_code = status
    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            auth = request.headers.get('authorization')[7:]
            email = decode_token(auth, current_app.config.get('SECRET_KEY'))
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, TypeError) as e:
            return build_message(HTTPStatus.UNAUTHORIZED, e)

        # the list of emails above should be in a database
        if email not in ['lucas@sheetgo.com', 'mauricio@sheetgo.com', 'rafael@sheetgo.com']:
            return build_message(HTTPStatus.FORBIDDEN, 'Forbidden')

        return f(*args, **kwargs)
    return decorated
