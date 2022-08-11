#!/usr/bin/env python
# coding: utf-8

# # Week 6: Merging and comparing geospatial data
# The **objective** of this lecture is to continue to put in the reptitions of downloading, visualizing, and analyzing geospatial data.  We are working with _two_ different datasets on asset-level emissions.  This lecture is purely the notes, meant exclusively for copy and paste in class, as needed.

# In[1]:


import geopandas
import pandas
import warnings
warnings.filterwarnings("ignore")


# In[2]:


url = "https://raw.githubusercontent.com/danhammer/envirods/main/data/steel.geojson"
steel_gdf = geopandas.read_file(url)


# In[3]:


steel_gdf.sort_values("CO2_emissions", ascending=False)


# In[4]:


import matplotlib.pyplot as plt
from datetime import datetime

plant = steel_gdf[steel_gdf["asset_name"] == "Jiangsu Shagang Group Co., Ltd."]
plt.plot(
    plant["end_date"], 
    plant["CO2_emissions"],
)


# In[5]:


from dateutil.parser import parse
from datetime import datetime

plant['date'] = pandas.to_datetime(plant['end_date'])

plt.plot(
    plant["date"], 
    plant["CO2_emissions"],
)

plt.box(on=None)


# In[6]:


plant["year"] = plant["date"].dt.year
print(plant["date"].dt)


# In[7]:


steel_gdf["date"] = pandas.to_datetime(steel_gdf['end_date'])
steel_gdf["year"] = steel_gdf["date"].dt.year
steel_gdf


# In[8]:


steel_collapsed = steel_gdf.groupby(["asset_name"])["CO2_emissions"].sum().reset_index()


# In[9]:


locations = steel_gdf[["asset_name", "geometry"]].drop_duplicates(ignore_index=True)


# In[10]:


df = steel_collapsed.merge(locations, on="asset_name")
gdf = geopandas.GeoDataFrame(df, geometry="geometry")

import matplotlib.pyplot as plt

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[world["continent"] != "Antarctica"]

fig, ax = plt.subplots(figsize=(20, 10))

world.plot(
    ax=ax,
    edgecolor="grey",
    color="lightgrey"
)

gdf.plot(
    ax=ax,
    markersize=3,
    column="CO2_emissions",
    cmap="magma"
)

plt.box(on=None)
plt.axis('off')


# In[11]:


import numpy

gdf["log_CO2_emissions"] = numpy.log(gdf["CO2_emissions"])
gdf.sort_values("CO2_emissions")

print(gdf[["asset_name", "CO2_emissions"]].sort_values("CO2_emissions").head())


# In[12]:


gdf = gdf[gdf["CO2_emissions"] > 0]
gdf["log_CO2_emissions"] = numpy.log(gdf["CO2_emissions"])

fig, ax = plt.subplots(figsize=(20, 10))

world.plot(
    ax=ax,
    edgecolor="grey",
    color="lightgrey"
)

gdf.plot(
    ax=ax,
    markersize=3,
    column="log_CO2_emissions",
    cmap="magma",
    legend=True
)

plt.box(on=None)
plt.axis('off')


# In[13]:


aviation = pandas.read_csv("https://raw.githubusercontent.com/danhammer/envirods/main/data/aviation.csv")
aviation['geometry'] = geopandas.GeoSeries.from_wkt(aviation['geometry'])

aviation_gdf = geopandas.GeoDataFrame(
    aviation,
    geometry="geometry"
)


# In[14]:


x = aviation_gdf.groupby(["iso3_country"]).sum()["CO2_emissions_tonnes"].reset_index()
x.columns = ["iso", "aviation_emissions"]

y = steel_gdf.groupby(["iso3_country"]).sum()["CO2_emissions"].reset_index()
y.columns = ["iso", "steel_emissions"]


# In[15]:


df = x.merge(y, how="inner", on="iso")
df["total"] =  df["aviation_emissions"] + df["steel_emissions"]

graphing_df = df.sort_values("total", ascending=False)[0:10]

plt.barh(
    graphing_df["iso"],
    graphing_df["total"]
)


# In[16]:


plt.barh(graphing_df["iso"], graphing_df["aviation_emissions"])


# In[17]:


plt.barh(graphing_df["iso"], graphing_df["aviation_emissions"])
plt.barh(graphing_df["iso"], graphing_df["steel_emissions"], left=graphing_df["aviation_emissions"])
plt.box(on=None)
plt.savefig("/Users/danhammer/Desktop/steel.png", transparent=True)


# In[18]:


plt.barh(graphing_df["iso"], graphing_df["steel_emissions"])
plt.barh(graphing_df["iso"], graphing_df["aviation_emissions"], left=graphing_df["steel_emissions"])


# In[19]:


aviation_gdf["date"] = pandas.to_datetime(aviation_gdf['end_date'])
aviation_gdf["year"] = aviation_gdf["date"].dt.year


# In[20]:


x = aviation_gdf.groupby(["year"]).sum()["CO2_emissions_tonnes"].reset_index()
x.columns = ["year", "aviation_emissions"]

y = steel_gdf.groupby(["year"]).sum()["CO2_emissions"].reset_index()
y.columns = ["year", "steel_emissions"]


# In[21]:


df = x.merge(y, how="inner", on="year")
df["total"] =  df["aviation_emissions"] + df["steel_emissions"]

df = df[df.year < 2022] # different months

# plot bars
plt.bar(df["year"] - 0.1, df['aviation_emissions'], width = 0.2)
plt.bar(df["year"] + 0.1, df['steel_emissions'], width = 0.2)

plt.box(on=None)
plt.savefig("/Users/danhammer/Desktop/annual.png", transparent=True)


# In[22]:


df = steel_collapsed.merge(locations, on="asset_name")
gdf = geopandas.GeoDataFrame(df, geometry="geometry")


gdf = gdf[gdf["CO2_emissions"] > 0]
gdf["log_CO2_emissions"] = numpy.log(gdf["CO2_emissions"])

fig, ax = plt.subplots(figsize=(20, 10), frameon=False)

world.plot(
    ax=ax,
    edgecolor="white",
    color="lightgrey"
)

gdf.plot(
    ax=ax,
    markersize=3,
    column="log_CO2_emissions",
    cmap="OrRd"
)

plt.tight_layout()
plt.box(on=None)
plt.axis('off')
plt.savefig("/Users/danhammer/Desktop/steel.png", transparent=True)


# In[23]:


x = aviation_gdf.groupby("asset_name").sum()["CO2_emissions_tonnes"].reset_index()

x = x.sort_values("CO2_emissions_tonnes", ascending=False)

fig, ax = plt.subplots(figsize=(15, 5), frameon=False)

plt.barh(
    x["asset_name"],
    x["CO2_emissions_tonnes"]
)

plt.box(on=None)
plt.savefig("/Users/danhammer/Desktop/airports.png", transparent=True)


# In[114]:


x = steel_gdf.groupby("asset_name").sum()["CO2_emissions"].reset_index()

x = x.sort_values("CO2_emissions", ascending=False)[0:15]

fig, ax = plt.subplots(figsize=(15, 5), frameon=False)

plt.barh(
    x["asset_name"],
    x["CO2_emissions"]
)

plt.box(on=None)
plt.savefig("/Users/danhammer/Desktop/steel_rank.png", transparent=True)


# ## Comparisons

# In[ ]:


url = "https://raw.githubusercontent.com/danhammer/envirods/main/data/steel.geojson"
steel_gdf = geopandas.read_file(url)

