#!/usr/bin/env python
# coding: utf-8

# # Lab 2: Plotting distributions
# 
# This is not going to be easy, especially for students with no experience in Python.  But that's what Thursdays are for! As a reminder, the labs are graded along the following four dimensions:
# 
# 1. **Execution**. There are no errors in executing the Notebook cells.
# 2. **Narrative**. Jupyter Notebooks are half code and half narrative prose. The integrated code should just be an illustration of the text.  Explain what you're doing!
# 3. **Creativity**. You are able to find interesting patterns in the data.
# 4. **Presentation**. Where there are maps and graphs, they are presented nicely.
# 
# Even though the code will speak for itself for these questions, explain what you're doing in the **Text** cells.
# 
# 1. Using the dataset from Week 2 `EJSCREEN_demo2.csv`, create a table with the number of missing values for every environmental justice score in the dataset (e.g., `P_RESP_D2`).  Comment on why some of the variables may have more missing values than others. 
# 
# 2. What is the average population represented by a Census Block Group.  Plot a histogram for all Census Block Groups with populations less than 10,000.  
# 
# 3. How many Census Block Groups are there in California (referring to this particular dataset)?  How does the average score of "Respiratory Hazard" in California Block Groups compare to the rest of the country? Does this make sense to you?
# 
# 4. Create single plot with **two** overlaid histograms. Plot the *density* of block groups at different respiratory hazard scores (0-100) for California and for the rest of the United States. (Hint: a parameter `density=True` should be set). The  One for California respiratory hazard.  Make this look nice by adding a legend and making sure that the histograms are not totally opaque. (Hint: set the parameter `alpha` to be less than 1.)  Comment on the skewness of the distributions.
