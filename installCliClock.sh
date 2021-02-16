#!/bin/bash

mv source.txt ~/.cli-clock.py
echo alias cli-clock='python ~/.cli-clock.py' >> .bashrc
if test -f ".zshrc"; then
    echo alias cli-clock='python ~/.cli-clock.py' >> .zshrc