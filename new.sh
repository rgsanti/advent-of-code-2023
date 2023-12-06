#!/bin/bash

echo "Generating directory and files for Day $1..."
mkdir $1 && cd $1
touch input.txt && touch test.txt && touch solution.py
exit 0