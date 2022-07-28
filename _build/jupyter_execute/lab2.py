#!/usr/bin/env python
# coding: utf-8

# # Lab 2: Plotting distributions
# 
# This is not going to be easy, especially for students with no experience in Python.  But that's what Thursdays are for! A few notes based on the previous Lab submissions.
# 
# 1. Don't leave code snippets commented in the final submission.  It should be a narrative.  You can comment the in-cell documentation; but not the code.
# 2. Ensure that the permissions are set so that "Anyone with the link" can view and comment on your Colab notebook.
# 3. Label your responses with the appropriate question number (e.g., Question 1, Q1, etc.).
# 4. Run each cell in the Colab so that the responses are saved. You can just "Run All" and then save the notebook.
# 5. I put a lot of emphasis on the responses to "comment on ..." or "analyze this ..." Be sure to write a quick sentence or two that is both thoughtful and relevant.
# 6. Multiple ways to answer the same question are given a lot of extra credit.
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
