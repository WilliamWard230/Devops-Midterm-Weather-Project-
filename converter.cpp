// William Ward
// MidTerm Project
// This program reads in the file created by the concatenation script, creates a csv file, and outputs the desired
// values to the csv file. The program hard codes the column headers and outputs them to the csv file. Then each line
// of the input txt is read and a substring containing the desired value is created and output to the csv file.

#include <iostream>
#include <fstream>
#include <map>

// an enumeration of the columns that will be found in the created csv file
enum Columns
{
    Date,
    Condition,
    High_Temperature,
    Low_Temperature,
    Average_Temperature,
    Precipitation,
    Wind_Speed,
    Dew_Point
};

// mapping each coloumn with a corresponding string
std::map<Columns, std::string> columnMap = {
    {Date, "Date"},
    {Condition, "Condition"},
    {High_Temperature, "High Temperature"},
    {Low_Temperature, "Low Temperature"},
    {Average_Temperature, "Average Temperature"},
    {Precipitation, "Precipitation"},
    {Wind_Speed, "Wind Speed"},
    {Dew_Point, "Dew Point"}};

// declaring the findColon function written at the bottom of the page
std::string findColon(std::string);

// forecasts.txt is to be passed in as argv
int main(int argc, char *argv[])
{
    // declaring varibles for the lines of forecast.txt, a counter for columns, and a counter for each csv column
    std::string line;
    int columnCount = 1;
    int csvCount = 1;

    // creating an output csv file
    std::string fileName = "weather_data.csv";
    std::ofstream outputFile(fileName);

    // printing each column from the columns map and adding a ',' after every output apart from the last one
    for (auto &column : columnMap)
    {
        outputFile << column.second;
        if (columnCount < 8)
        {
            outputFile << ",";
        }
        columnCount++;
    }
    outputFile << std::endl;

    std::ifstream file(argv[1]);

    // reading in forecasts.txt line by line
    while (std::getline(file, line))
    {
        // finds the value after the colon and outputs the value to the csv file. Adds a ',' after every value except the last one
        if (csvCount < 8)
        {
            outputFile << findColon(line) << ",";
            csvCount++;
        }
        else
        {
            outputFile << findColon(line) << std::endl;
            csvCount = 1;
        }
    }

    return 0;
}

// function for creating a substring of each line that cuts off everything upto and including the colon, leaving only the desired value
std::string findColon(std::string line)
{
    int pos;

    pos = line.find(':');
    std::string csvValue = line.substr(pos + 1);

    return csvValue;
}