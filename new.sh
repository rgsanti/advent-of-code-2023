#!/bin/bash

echo "Generating folders and files for Day $1..."
mkdir $1 && cd $1
mkdir 1 && mkdir 2
cd 1 && touch input.txt && touch solution.py
cd ../2 && touch input.txt && touch solution.py
exit 0