#!/usr/bin/env python
# coding: utf-8

# # Lab 1: Basic operations
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
# 1. Create a `DataFrame` of random numbers with 100 rows and 4 columns. Name the columns `a`, `b`, `c`, and `d`.
# 2. Create a scatter plot of column a against b. Set the size of each point on the scatterplot based on a new variable `adev`, which records the number of deviations of `a` from the average value of `a`. (Scale this variable by, say, 100 or more so that you can see the difference in the final plot.)
# 3. Graph and examine the correlations between different variables in the `EJSCREEN_demo` dataset. Comment on the relationship, for example, between education and distance to "treatment storage and disposal facilities" (TSDFs). Is it positive or negative? Are there certain "mass points" or clusters of observations around a certain value (e.g., zero)?
