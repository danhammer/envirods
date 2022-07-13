#!/usr/bin/env python
# coding: utf-8

# ## Week 2: Table Manipulations and Environmental Justice
# The **objective** of this lecture is to introduce the manipulation of rectangular data in Pandas. There are many ways to manage data tables in Python, including the table frameworks used in DATA 8.  The concepts are important.  And, in fact, there is some value in not becoming too wedded to a particular library in the beginning.  So we will teach the concepts here, and offer practical examples in multiple frameworks.

# ### Sort, merge, and collapse

# In[1]:


# import the libraries we will use in this lecture
import pandas
import numpy
import matplotlib.pyplot as plt


# First, create a dataframe from a dictionary.  Each row in a rectangular dataframe may have a unique identifier - some variable that uniquely identifies the record.  The unique identifier could be, for example, the name of a person, a time period, or the intersection of the two.  When the unique identifier for a record (a row) represents both an individual unit (e.g., a person or a country) and a time period (e.g., a day or a year) then the dataset is called **panel dataset**.  Generate a panel dataset, which tracks individuals (indexed by `i`) over time (indexed by `t`).

# In[2]:


d = {
    'id': [1, 1, 2, 2], 
    't':  [1, 2, 1, 2], 
    'x':  [5, 3, 6, 2], 
    'y':  [6, 5, 1, 4]
}

df = pandas.DataFrame(data=d)


# Access certain rows or certain columns in the dataframe.

# In[3]:


df["y"]
df[0:2]
df[2:3]


# #### Sort
# Sort data by a certain variable in ascending and descending order

# In[4]:


df.sort_values(by=['y'])
df.sort_values(by=['y'], ascending=False)


# #### Aggregate (group by)
# Collapse, or aggregate, the data by a certain variable. That is, calculate within-group statistics.

# In[5]:


df.groupby("id")[["x", "y"]].sum()
df.groupby("t")[["x", "y"]].mean()


# #### Merge
# Merge will extend the *width* of the dataframe, based on the identifiers in the dataset. For example, create a *new* dataframe which would add a new variable `z` to individuals `1` and `2` for each time period `1` and `2`.  Merge dataframe with the new variable to the old dataframe.

# In[6]:


dfx = pandas.DataFrame({
    'id': [1, 1, 2, 2], 
    't':  [1, 2, 1, 2], 
    'z':  [4, 3, 4, 3]
})

df.merge(dfx, on=['id', 't'], how='left')


# The `how` parameter in `merge()` specifies how the merge would be performed.  This parameter is not useful when every individual and time period is in both the original dataframe (on the left of the `merge` expression) and the new dataframe (on the right of the `merge` expression).  It matters, however, when not all the records are represented in either or both of the dataframes.  For example, redefine the new dataframe with only records for `id==1`:

# In[7]:


dfx = pandas.DataFrame({
    'id': [1, 1], 
    't':  [1, 2], 
    'z':  [4, 3]
})

# The record identifiers for df are kept, even when not represented in dfx
df.merge(dfx, on=['id', 't'], how='left')


# In[8]:


# The record identifiers for dfx are kept, and only those record identifiers, 
# even not represented in df, noting that dfx contains a subset of the record 
# identifiers of df
df.merge(dfx, on=['id', 't'], how='right')


# In[9]:


# The union of record identifiers in df and dfx are kept.  When the record 
# identifiers in the right dataframe are a subset of those in the left 
# dataframe, then `how=left` is equivalent to `how=outer`
df.merge(dfx, on=['id', 't'], how='outer')


# In[10]:


# The intersection of record identifiers in df and dfx are kept.  When the record 
# identifiers in the right dataframe are a subset of those in the left 
# dataframe, then `how=right` is equivalent to `how=inner`
df.merge(dfx, on=['id', 't'], how='inner')


# Suppose, instead, that the record identifiers of the right dataframe are not just a subset of those in the left:

# In[11]:


dfx = pandas.DataFrame({
    'id': [1, 1, 3, 3], 
    't':  [1, 2, 1, 2], 
    'z':  [4, 3, 9, 8]
})

df.merge(dfx, on=['id', 't'], how='left')


# In[12]:


df.merge(dfx, on=['id', 't'], how='inner')


# In[13]:


df.merge(dfx, on=['id', 't'], how='right')


# In[14]:


df.merge(dfx, on=['id', 't'], how='outer')

