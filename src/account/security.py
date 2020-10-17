import jwt
import os
import config
import bcrypt
import sqlite3
import datetime
from functools import wraps
from flask import abort, request
from src.schema import User

def encodeToken(payload):
    payload["createdAt"] = datetime.datetime.now().strftime(
        '%Y-%m-%d-%H:%M:%S')
    encodedJWT = jwt.encode(payload, config.SECRET_KEY,
                            algorithm='HS256').decode()
    return encodedJWT


def decodeToken(token):
    decodedJWT = jwt.decode(token, config.SECRET_KEY, algorithm='HS256')
    return decodedJWT


def hashPassword(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()


def checkPassword(password, hashedPassword):
    return bool(bcrypt.checkpw(password.encode(), hashedPassword.encode()))



def authorize(*allowed):
    def dec(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.cookies.get('auth_token', False)
            isauth = False
            permissionName = None
            if token:
                token_body = decodeToken(token)
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute(
                    f"""SELECT token FROM AuthTokens WHERE user=(SELECT id FROM Users WHERE username='{token_body["username"]}')""")
                tokens = [i[0] for i in c.fetchall()]
                if token in tokens and token_body["permission"] in allowed:
                    isauth = True
                    c.execute(
                        f"""SELECT * FROM Users WHERE username='{token_body["username"]}'""")
                    userDATA = c.fetchone()
                    UserData = User(userDATA,convert=['permission'])
            if not isauth:
                abort(401)
            return f(UserData, *args, **kwargs)
        return wrapper
    return dec