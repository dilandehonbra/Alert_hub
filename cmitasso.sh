#!/usr/bin/env bash
files=$(ls $PWD)

desc=$1

for i in $(echo "$files") ; do git add $PWD/$i ; done

git commit -m "${desc}" && git push
