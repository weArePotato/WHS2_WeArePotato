from bs4 import BeautifulSoup
from sys import version
import requests

class FetchConfigError(Exception):
    def __init__(self, text):
        self.txt = text

class RunError(Exception):
    def __init__(self, text):
        self.txt = text

class Struct():
    def __init__(self, version):
        self.version = version

class Compiler():
    def __init__(self, config):
        self.config = config

    def fetchconfig(self, config):
        try:
            if config != "__main__":
                response = requests.get(f"https://bullcode-configs.netlify.app/{config}.html")
                soup = BeautifulSoup(response.text, "lxml")
                get_version = soup.find("h1", class_ = "version").text
                return Struct(version = get_version)
            else:
                return Struct(version = "v1_0_0")
        except Exception:
            raise FetchConfigError("Invalid config... Check internet connection or config-name!")

    def run(self, code):
        self.code = code
        if "Use Engine" in code or 'Use Engine' in code:
            self.Config = self.fetchconfig(self.config)
            self.version = self.Config.version
            self.bullcode = f".versions.{self.version}.bullcode"
            self.result = f"""from {self.bullcode} import * \n \n{self.code}"""
            print(f"Bullcode {self.version}, using Python {version} \n")
            exec(self.result)
        else:
            raise RunError("looks like you forgot the line 'Use Engine' at the beginning.")
