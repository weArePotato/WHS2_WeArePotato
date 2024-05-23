import sys

class System():
    def __init__(self, version):
        self.cash = "Rad6Xsa3ad35FGGfsfas5"
        self.version = version
        self.python_version = sys.version()
    
    def exit(code = 0):
        sys.exit(code)