#!/bin/bash

# Check if an argument is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi

year=$1
day=$2

if ! [[ $day =~ ^[0-9]+$ ]]; then
    echo "Error: The provided day should be an integer."
    exit 1
fi

mkdir adventofcode/year$year/day$day
mkdir adventofcode/year$year/day$day/input
touch adventofcode/year$year/day$day/__init__.py
touch adventofcode/year$year/day$day/input/real_data.txt
touch adventofcode/year$year/day$day/input/test_data_part1.txt
touch adventofcode/year$year/day$day/input/test_data_part2.txt
touch adventofcode/year$year/day$day/solution.py
touch adventofcode/year$year/day$day/test_day$day.py
