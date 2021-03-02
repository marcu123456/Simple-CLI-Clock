#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
    mv cli-clock.py ~/.cli-clock.py
    sudo chmod +x cli-clock
    sudo mv cli-clock /usr/local/bin
