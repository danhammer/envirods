#!/usr/bin/env python
# coding: utf-8

# ### Lab 3: Linear regression
# 
# 1. Generate a dataset that represents a sample of 10,000 cars.  Assume you have collected information on the price of the car, the mileage, and the age of the car.  Think about how the variables may be correlated with each other when you create the dataset (e.g., mileage and age are probably positively related).  Describe the variables with `describe()` and talk about the choices you made to generate a dataset that looks roughly realistic.  (This requires some thought.)
#    
#    - The data generating process should look like $price_i = b + m_1 \cdot mileage_i + m_2 \cdot age_i + \omega_i$ and $mileage_i = m_3 \cdot age_i + \epsilon_i$ for each car $i$ that ranges from 0 to 9,999.  There are two random error terms, $\omega_i$ and $\epsilon_i$.  Generate $\omega$ to be distributed `numpy.random.normal(0, 1000, 10000)` and $\epsilon$ to be distributed `numpy.random.normal(0, 5000, 10000)`.
#    - Describe why you chose values $m_1$, $m_2$, $m_3$, and $b$.
#    
# 
# 2. Plot the distributions of the age, mileage, and price of the car.  Include a vertical line at the mean of each distribution.
# 
# 3. Estimate a linear regression with price as the dependent (`y`) variable and mileage as the independent (`x`) variable.  Are the numbers what you'd expect?  Why or why not?
# 
# 4. Use the `EJSCREEN_demo3.csv` data to describe the correlation between `OZONE` and `PM25`. 
# 
# 5. Consider this URL and explore the parameters and response data:
# 
#     `https://api.e7e.dev/news/retrieve?themes=wildlands&limit=2000&daysback=365`
# 
#     This API returns geolocated stories for display at [news.earthrise.media](https://news.earthrise.media/).  By  adjusting the URL and using the `requests` library, how many stories were tagged with `pollution` in the last 30 days? Print the titles of the stories.  (Hint: There is a default number for the `limit` parameter.)
