#!/usr/bin/env bash
files=$(ls $PWD)

desc=$1
cmdlineOptions=$2
for i in $(echo "$files") ; do git add $PWD/$i ; done

git commit -m "${desc}" ${cmdLineOptions} && git push origin main
