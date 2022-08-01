#!/usr/bin/env python
# coding: utf-8

# ### Lab 4: Spatial Data
# 
# 1. Using the farmers' markets dataset from lecture (`farmers-mkts.csv`) find how many markets sell both wine and cheese.  How many sell plants and nuts?  How many sell poultry and eggs?  How many sell honey and flowers?  Create a function that reports the proportion of all farmers markets in the United States that sell these pairs.
# 
# 2. Using the `world` dataset from lecture (located at `geopandas.datasets.get_path('naturalearth_lowres')`), calculate the total population by region in the world.  Create a horizontal bar chart that displays the total population by region.
# 
# 3. Using the `world` dataset from lecture, define a variable for gross domestic product per capita as `world['gdp_per_cap'] = world['gdp_md_est'] / world['pop_est']` and plot a [chloropleth map](https://en.wikipedia.org/wiki/Choropleth_map) that colors each country in the world by its GDP per capita.
# 
# 4. Create a map of coal-fired power plants in India that are currently operating, where each point is colored by its annual carbon emissions.  Create another map that colors the power plants by some measure of efficiency (like capacity over emissions).
# 
# 5. Use the Earthrise news API to plot a map of 1,000 local news stories about wildlands. Use this URL as a reference: `https://api.e7e.dev/news/retrieve?themes=wildlands&limit=2000&daysback=365` but change the parameters.  Where are most of the stories located?  Why are there areas with very few stories?
# 
# 

# In[1]:


import pandas
import geopandas
df = pandas.read_csv("https://raw.githubusercontent.com/danhammer/envirods/main/data/farmers-mkts.csv")
gdf = geopandas.GeoDataFrame(
    df, 
    geometry=geopandas.points_from_xy(df.x, df.y)
)


# In[2]:


x = gdf[["Plants", "Nuts"]].dropna()
results = (x == "Y").sum()
results / len(x)

