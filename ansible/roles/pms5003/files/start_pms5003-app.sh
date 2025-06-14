#!/bin/bash

cd /opt/projects/pms5003-app

activate() {
   . ~/.virtualenvs/pimoroni/bin/activate
}

activate

python main.py