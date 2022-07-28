#!/usr/bin/env python
# coding: utf-8

# # Week 3: Linear Regression and Environmental Justice
# The **objective** is to measure trends in data.  We're looking for correlations between variables, and the "tighteness" of that correlation.  We can't talk about causality.  That's the domain of econometrics.  But we _can_ use the data to ask the right or _relevant_ questions.

# In[1]:


import pandas
import matplotlib.pyplot as plt
from scipy import stats


# In[2]:


df = pandas.read_csv("https://github.com/danhammer/envirods/blob/main/data/EJSCREEN_demo3.csv?raw=true")
df.describe()


# Suppose we wanted to examine the distribution of population of the 

# In[3]:


# Set figure size
plt.figure(figsize=(16, 8))

# Assign the plot to a variable, just to suppress output in Notebooks
fig = plt.hist(
    df["ACSTOTPOP"], 
    range=[0,10000], 
    bins=1000
)

# Add a vertical line at the mean value, and standard deviations
plt.axvline(
    df.ACSTOTPOP.mean(), 
    linewidth=3, 
    color="orange"
)

plt.axvline(
    df.ACSTOTPOP.mean()-df.ACSTOTPOP.std(), 
    linewidth=1, 
    color="orange",
    linestyle="dashed"
)

plt.axvline(
    df.ACSTOTPOP.mean()+df.ACSTOTPOP.std(), 
    linewidth=1, 
    color="orange",
    linestyle="dashed"
)


# In[4]:


plt.figure(figsize=(16, 8))

# Assign the plot to a variable, just to suppress output in Notebooks
fig = plt.hist(df.PM25, range=[0,16], bins=1000)

# Add a vertical line at the mean value, and standard deviations
plt.axvline(
    df.PM25.mean(), 
    linewidth=3, 
    color="orange"
)

plt.axvline(
    df.PM25.mean()-df.PM25.std(), 
    linewidth=1, 
    color="orange",
    linestyle="dashed"
)

plt.axvline(
    df.PM25.mean()+df.PM25.std(), 
    linewidth=1, 
    color="orange",
    linestyle="dashed"
)


# The objective is to fit a line that is defined by $y=mx+b$ so that the coefficient $m$ and the intercept $b$ are chosen to minimize the errors between the line and the actual observations.  We use ordinary least squares to find the slope and intercept of this line - the linear model.  There may be other types of models that better represent the data than a linear model; but a linear model is a good first start, just to get a sense of the data.
# 
# Once we have found the $m$ and $b$ that minimize the errors, which we call $\hat{m}$ and $\hat{b}$, we get a predicted $y$ value for each $x$.  We denote and calculate this predicted $y$ value as $\hat{y} = \hat{m} x + \hat{b}$. Note that the $x$ value isn't estimated.  It's just the data.  And therefore has no hat on it.
# 
# For a particular record, with index $i$, calculate the predicted $y$ value for that observation as $\hat{y}_i = \hat{m} x_i + \hat{b}$.  Note that the values of $\hat{m}$ and $\hat{b}$ are constant across all observations and, as a result, don't need the $i$ index.
# 
# Finally, we denote $\bar{y}$ as the mean for the $y$ variable, across all observations.

# In[5]:


m, b, _, _, _ = stats.linregress(df.PM25, df.D_PM25_2)
print("slope: " + str(m))
print("slope: %s" % m)
print(f"slope: {m}")
print(f"intercept: {b}")


# In[6]:


plt.figure(figsize=(16, 8))
plt.scatter(
    df.PM25,
    df.D_PM25_2,
    s=0.01
)

plt.plot(df.PM25, m*df.PM25 + b, color="orange")
plt.ylim([-20000, 20000])


# In[7]:


m, b, _, _, _ = stats.linregress(df.demographic_index, df.D_PM25_2)
print(f"slope: {m}")
print(f"intercept: {b}")


# The R-squared, or coefficient of correlation, or coefficient of determination is a measure of how much of the variation can be explained by the linear model.  A higher $R^2$ value indicates that the linear model explains more of the variation - there is less variation relegated to the residuals, relative to the total variation.
# 
# $$ R^2 = 1 - \frac{RSS}{TSS} = 1 - \frac{\sum_{i} (y_i - \hat{y}_{i})^{2}}{\sum_{i} (y_i - \bar{y})^{2}}$$

# In[8]:


m, b, _, _, _ = stats.linregress(df.PM25, df.D_PM25_2)
df["yhat"] = m*df.PM25 + b
rss = sum((df.D_PM25_2 - df.yhat)**2)
tss = sum((df.D_PM25_2 - df.D_PM25_2.mean())**2)

1 - rss/tss


# In[9]:


m, b, r, _, _ = stats.linregress(df.PM25, df.D_PM25_2)

r**2


# In[10]:


m, b, _, _, _ = stats.linregress(df.demographic_index, df.D_PM25_2)
df["yhat"] = m*df.demographic_index + b
rss = sum((df.D_PM25_2 - df.yhat)**2)
tss = sum((df.D_PM25_2 - df.D_PM25_2.mean())**2)

1 - rss/tss


# In[11]:


m, b, r, _, _ = stats.linregress(df.demographic_index, df.D_PM25_2)

r**2

