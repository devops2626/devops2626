#!/bin/sh
set -e
cd ~/Documents/devops2626/docs
sphinx-build -b html source build
cd ~/Documents/devops2626
DATE=$(date +%Y-%m-%d)
lg2 add docs/source/ docs/build/
lg2 commit -m "Docs: $DATE"
lg2 push
