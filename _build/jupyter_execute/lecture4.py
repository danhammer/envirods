#!/usr/bin/env python
# coding: utf-8

# # Week 2: Table Manipulations and Environmental Justice
# The **objective** of this lecture is to apply the `groupby()`, `merge()`, and row-filtering from the previous lecture to an application in environmental justice.
# 
# ## Application
# The EJSCREEN indices are used to prioritize federal funding in order to mitigate environmental injustice. Here, we examine the rural and urban representation in the prioritization data. Does this reflect the composition of the United States?  
# 
# First, read in a dataset that associates each U.S. county with a CDC assessment of urban/suburban/rural. The counties are uniquely identified by a Federal Information Processing System (FIPS) Code. 

# In[1]:


import pandas


# In[2]:


# Source: https://www.cdc.gov/nchs/data_access/urban_rural.htm#Data_Files_and_Documentation
nchs = pandas.read_excel("https://github.com/danhammer/envirods/blob/main/data/NCHSURCodes2013.xlsx?raw=true")
nchs = nchs[["FIPS code", "State Abr.", "County name", "2013 code"]]
nchs.columns = ["fips", "state", "county", "classification"]


# In[3]:


# Associate each of the classifications to one of three categories, rather 
# than one of six - just to simplify our quick analysis
remap_dict = {
    1: "urban",
    2: "suburban",
    3: "suburban",
    4: "rural",
    5: "rural",
    6: "rural"
}

# replace the values of the `classification` column based on the key-value 
# pair in `remap_dict`
nchs = nchs.replace({'classification': remap_dict})


# Now, read in the EJ indices and merge the dataset with the urban/suburban/rural dataset, so that each of the Census Blocks in the EJSCREEN data now has the CDC categorization.

# In[4]:


ejdf = pandas.read_csv("https://raw.githubusercontent.com/danhammer/envirods/main/data/EJSCREEN_demo2.csv")
ejdf = ejdf.merge(nchs, how='left', on='fips')


# In[5]:


# A dictionary to translate opaque variable names to somthing that
# is human-readable
ejvars_dict = {
    'P_LDPNT_D2': 'Lead Paint',
    'P_DSLPM_D2': 'Diesel Particulate Matter',
    'P_CANCR_D2': 'Air Toxics Cancer Risk',
    'P_RESP_D2':  'Respiratory Hazard',
    'P_PTRAF_D2': 'Traffic Proximity',
    'P_PWDIS_D2': 'Water Discharge',
    'P_PNPL_D2':  'National Priority List',
    'P_PRMP_D2':  'Risk Management Plan',
    'P_PTSDF_D2': 'Treatment Storage and Disposal',
    'P_OZONE_D2': 'Ozone Proximity',
    'P_PM25_D2':  'PM25'
}


# Each of the variables in the dataset indicates the percentile where that Census Block falls in prioritization. Those census blocks with high percentiles are prioritized for federal funding.  Here, we examine the urban/suburban/rural breakdown of the population living within these high-priority Census Blocks.

# In[6]:


v = 'P_LDPNT_D2'
temp_df = ejdf[ejdf[v] > 90]
temp_df = temp_df.groupby('classification').sum()['ACSTOTPOP']

# add back in the classification variable for future reference
temp_dict = dict(temp_df)
temp_dict['variable'] = v
temp_dict


# In[7]:


# Instead of just displaying the results for one variable, collect 
# the results for all in a list.
res = []

# Note that ejvars_dict.keys() is a list of the EJ variable names
for v in ejvars_dict.keys():
    temp_df = ejdf[ejdf[v] > 90]
    temp_df = temp_df.groupby('classification').sum()['ACSTOTPOP']
    temp_dict = dict(temp_df)
    temp_dict['variable'] = v
    res.append(temp_dict)

# Create a dataframe of the results
graphing_df = pandas.DataFrame(res)
graphing_df


# We now have a dataframe with the total population in rural, suburban, and urban areas that would be prioritized for EJ funding for each of the 11 indicators.  Now, convert this into a percentage, noting that we can't just divide by the total population of the United States across all of these cell values due to missing values - and the fact that those missing values aren't uniformly distributed across the indicators.

# In[10]:


pop_df = graphing_df[["rural", "suburban", "urban"]]

# first sum over the columns, horizontally
total_by_class = pop_df.sum(axis="columns")

# then divide, within columns, vertically
pop_df = pop_df.div(total_by_class, axis="index")

# add back the classification
pop_df["variable"] = graphing_df["variable"]

# name it appropriately
pop_df["indicators"] = pop_df["variable"].replace(ejvars_dict)

pop_df


# In[11]:


# Plot the results. 
pop_df = pop_df.set_index(pop_df["indicators"])

pop_df.plot(
    kind="barh", 
    stacked=True
)


# In[12]:


pop_df.sort_values(by=['rural']).plot(
    kind="barh", 
    stacked=True
)


# Does this plot reflect the composition rest of the country?  **No.**

# In[13]:


ejdf.groupby("classification").sum()["ACSTOTPOP"] / sum(ejdf["ACSTOTPOP"])


# Should it?  I don't know.  But this very apparent mismatch is not being adequately addressed at the highest levels of government, as they discuss how to identify "underserved communities."
