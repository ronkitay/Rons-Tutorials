#!/bin/sh

if [ $# -lt 1 ]; then
  echo "Expecting at least one argument"
  exit 1
fi

MODULE_HUMAN_NAME=$(echo $* | tr -d ' ')
MODULE_CODE_NAME=$(echo $* | tr ' ' '-' | tr 'A-Z' 'a-z')

let next=$(fd -t d  | sort -n | tail -n 1 | cut -d '.' -f1)+1;

MODULE_DIR_NAME="${next}.${MODULE_HUMAN_NAME}"

mkdir "${MODULE_DIR_NAME}"

cd "${MODULE_DIR_NAME}"

REPO_ROOT=$(git rev-parse --show-toplevel)

sed -i .bak "$ s|)|	./GoLang/GoByExample/${MODULE_DIR_NAME}|" ${REPO_ROOT}/go.work

printf "\n)" >> ${REPO_ROOT}/go.work

rm ${REPO_ROOT}/go.work.bak

echo "module ronkitay.com/GoByExample/${MODULE_DIR_NAME}.v0" > go.mod; 
echo "" >> go.mod; 
printf "go 1.21.1" >> go.mod

echo "package main" > ${MODULE_CODE_NAME}.go
echo "" >> ${MODULE_CODE_NAME}.go
echo "func main() {" >> ${MODULE_CODE_NAME}.go
echo "" >> ${MODULE_CODE_NAME}.go
echo "}" >> ${MODULE_CODE_NAME}.go