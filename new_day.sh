#!/bin/bash

# langs=["python"]

# for lang in "${langs[@]}"
do
    # if [[ $lang == $1 ]]
    # then
        echo "Generating folders and files for Day $1 for $2..."
        mkdir $1 && cd $1
        mkdir 1 && mkdir 2
        cd 1 && touch input.txt
        case $2 in
        "python")
            touch solution.py
            ;;
        esac
        cd ../2 && touch input.txt
        case $2 in
        "python")
            touch solution.py
            ;;
        esac
        exit 0
    else
        echo "Specified language not found!"
        exit 1
    fi
done