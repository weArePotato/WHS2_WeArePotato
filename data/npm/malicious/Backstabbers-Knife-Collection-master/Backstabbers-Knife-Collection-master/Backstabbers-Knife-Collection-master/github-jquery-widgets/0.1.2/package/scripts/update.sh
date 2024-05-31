#!/bin/sh

sdir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $sdir
cd ..
git submodule update --remote --force --recursive lib/radicjs
grunt build:dep
