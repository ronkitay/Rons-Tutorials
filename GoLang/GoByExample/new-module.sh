#!/bin/sh

if [ $# -ne 2 ]; then
  echo "Expecting exactly one argument"
  exit 1
fi

let next=$(fd -t d  | sort -n | tail -n 1 | cut -d '.' -f1)+1;

mkdir "${next}.$1"

cd "${next}.$1"

REPO_ROOT=$(git rev-parse --show-toplevel)

sed -i .bak "$ s|)|	./GoLang/GoByExample/${next}.$1|" ${REPO_ROOT}/go.work

printf "\n)" >> ${REPO_ROOT}/go.work

rm ${REPO_ROOT}/go.work.bak

echo "module ronkitay.com/GoByExample/${1}.v0" > go.mod; 
echo "" >> go.mod; 
printf "go 1.21.1" >> go.mod

echo "package main" > ${2}.go
echo "" >> ${2}.go
echo "func main() {" >> ${2}.go
echo "" >> ${2}.go
echo "}" >> ${2}.go