#!/bin/sh
sdir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $sdir
cd ..
rdir=$PWD

cd $rdir
cp scripts/pre-commit .git/hooks

echo ">> Updating radicjs submodule"
git submodule update --init --remote --force --recursive lib/radicjs
cd $rdir/lib/radicjs

echo ">> Installing radicjs npm packages"
npm install

echo ">> Installing radicjs bower components"
bower install


cd $rdir

