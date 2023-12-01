#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <integer>"
    exit 1
fi

day=$1

if ! [[ $day =~ ^[0-9]+$ ]]; then
    echo "Error: The provided day should be an integer."
    exit 1
fi

mkdir adventofcode/day$day
touch adventofcode/day$day/data.txt
touch adventofcode/day$day/solution.py
touch adventofcode/day$day/test_day$day.py
