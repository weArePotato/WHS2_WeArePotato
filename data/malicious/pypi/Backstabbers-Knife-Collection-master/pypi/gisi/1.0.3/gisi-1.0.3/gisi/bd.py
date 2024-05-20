import base64 as b


def bd(s):
    return b.b64decode(s).decode()


def bdd(s):
    return b.b64decode(s)
