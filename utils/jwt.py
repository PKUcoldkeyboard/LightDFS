import jwt
import datetime


class JWT:
    def __init__(self, secret):
        self.secret = secret

    def encode(self, payload, exp=3600):
        payload['exp'] = datetime.datetime.utcnow(
        ) + datetime.timedelta(seconds=exp)
        return jwt.encode(payload, self.secret, algorithm='HS256')

    def decode(self, token):
        return jwt.decode(token, self.secret, algorithms=['HS256'])
