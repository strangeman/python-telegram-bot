#!/bin/bash

virtualenv .

# activate virtualenv
source ./bin/activate

# install requirements
./bin/pip install -r requirements.txt

# create dirs for data and logs
mkdir -p ./data/state
mkdir -p ./data/log