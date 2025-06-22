#!/usr/bin/env bash

desc=$1

git add -A
git commit -m "${desc}"
git push origin main
