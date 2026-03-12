#!/bin/bash

# script that reads every file in weather_data/ and prints each line of a file to forecasts.txt

for forecast in weather_data/*
do
    cat "$forecast" >> forecasts.txt
    printf "\n" >> forecasts.txt
    
done