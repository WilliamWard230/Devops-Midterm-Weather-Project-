#!/bin/bash

# exit if any comman fails
set -e

# runs concatenate.sh to create forecasts.txt
./concatenate.sh

# compiles and names an exe file to read forecasts.txt
clang++ -std=c++20 converter.cpp -o converter.exe

# runs the exe file with forecasts.txt
./converter.exe forecasts.txt

# the converter.exe creates a csv that is run with the visualizer. creating a png
python3 weather_visualizations.py weather_data.csv