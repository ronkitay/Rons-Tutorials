#!/bin/sh

HELM_UNITTEST_IMAGE="helmunittest/helm-unittest"
HELM_UNITTEST_VERSION="3.17.2-0.8.1"


function runTests() {
    echo "Running chart integration test"
    docker run --rm -v $(pwd):/apps ${HELM_UNITTEST_IMAGE}:${HELM_UNITTEST_VERSION} chart/ --debug --color
}

if [[ "$1" == "--watch" ]]; 
then
    while true; do
        clear
        runTests
        sleep 5
    done
else
    runTests
fi