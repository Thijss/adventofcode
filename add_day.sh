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
mkdir adventofcode/day$day/input
touch adventofcode/day$day/__init__.py
touch adventofcode/day$day/input/real_data.txt
touch adventofcode/day$day/input/test_data_part1.txt
touch adventofcode/day$day/input/test_data_part2.txt
touch adventofcode/day$day/solution.py
touch adventofcode/day$day/test_day$day.py
