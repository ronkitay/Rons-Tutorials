#!/bin/sh

HELM_UNITTEST_VERSION="3.7.1-0.2.8"

# function setup() {
#     echo "Downloading dependencies"
#     helm dep update chart/tests/chart-integration-test
# }

function runTests() {
    echo "Running chart integration test"
    docker run --rm -v $(pwd):/apps quintush/helm-unittest:$HELM_UNITTEST_VERSION chart/tests/chart-integration-test --debug --color
}

# setup

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