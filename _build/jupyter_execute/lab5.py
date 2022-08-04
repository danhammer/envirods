#!/usr/bin/env python
# coding: utf-8

# ### Lab 5: Putting in the repetitions
# 
# This lab will focus exclusively on carbon emissions from the aviation sector, using the following dataset:
# 
# `https://raw.githubusercontent.com/danhammer/envirods/main/data/aviation.csv`
# 
# 1. Create a map of the 100 airports with the most flights in 2021, where the color or size of the point is determined by the number of flights.
# 
# 2. Create a chloropleth map of the total emissions from the aviation sector by country.  Resecale the emissions so that the colors shows some variation (i.e., use `numpy.log` to rescale).
# 
# 3. Create a line chart that shows the time series of emissions over time for 4 major airports of your choosing.  Create another one with fuel consumption for those airports.  Bonus if you can do this within a function, where a list of four airports is the input.
# 
# 4. For the top 20 airports with the most emissions in 2019, create a table that is sorted by airports with the greatest proportionate decrease in emissions from 2019 to 2020 (i.e., change in emissions over total 2019 emissions).
# 
