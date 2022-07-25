#!/usr/bin/env python
# coding: utf-8

# # Week 4: HTTP requests and spatial data
# The **objective** of this lecture is to learn more about data acquisition and access via web service APIs, and even a brief exploration of the developer console.  We will find and access _spatial_ data and begin to work with the `geopandas` project.

# In[1]:


import requests
import pandas


# ## One of the most useful free APIs
# 
# I use this often. OpenStreetMap (OSM) is a crowd-sourced map of the world. Nominatum is a web service that allows users to interact with OSM data. The input for the Nominatum geocoder is an address or a place name; the output is a latitude and longitude (and other OSM metadata). The reverse geocoder accepts a latitude and longitude, and returns the place name and address - and sometimes even the boundary of the facility, if requested.

# In[2]:


url = "https://nominatim.openstreetmap.org/reverse"
payload = {
    "format": "json",
    "lat": 37.8692322,
    "lon": -122.25755
}
r = requests.get(url, params=payload)
response = r.json()


# In[3]:


print(response.keys())

print(response["display_name"])


# In[4]:


url = "https://nominatim.openstreetmap.org/reverse"
payload = {
    "format": "json",
    "lat": 37.87, # round to 2 significant digits
    "lon": -122.26 # rount to 2 significant digits
}
r = requests.get(url, params=payload)
response = r.json()
print(response["display_name"])


# ## Creating a function
# 
# The only thing we did was change the values of certain variables.  For this, instead of copying code, we can create a template instead.

# In[5]:


def get_name(lat, lon):
    """
    Accepts a latitude and longitude.
    Returns the OSM place name.
    """
    url = "https://nominatim.openstreetmap.org/reverse"
    payload = {
        "format": "json",
        "lat": lat,
        "lon": lon
    }

    r = requests.get(url, params=payload)
    response = r.json()
    return response["display_name"]

get_name(37.87, -122.26)


# ## Finding (spatial) data
# The requests package allows access to data. How do we find the data we want to access. Often, websites will rely on data. Let's try to find data by looking inside the developer console. [This was a helpful article](https://support.monday.com/hc/en-us/articles/360002197259-How-to-Open-the-Developer-Console) on how to open the developer console in different browsers.

# In[6]:


url = "https://global-coal-map-2020.s3.eu-west-2.amazonaws.com/data/coal2020.geojson"
r = requests.get(url)
response = r.json()
features = response["features"]


# In[7]:


len(features)


# In[8]:


features[0]


# In[9]:


rows = [f["properties"] for f in features]
df = pandas.DataFrame(rows)
df.head()


# In[10]:


operating = df[df.status == "Operating"]
operating.groupby("coalType")["annualCarbon"].sum()
hist_data = operating.groupby("regionLabel")["annualCarbon"].sum()
hist_data = hist_data.reset_index().sort_values("annualCarbon")
plt.barh(hist_data.regionLabel, hist_data.annualCarbon)


# ## Plotting spatial data 
# While we had access to the geographic coordinates, we didn't really use them.  With `geopandas` it is pretty quick to start to create a map.

# In[20]:


# !pip install geopandas
import geopandas


# In[29]:


# automatically added a geometry field
power_plants = geopandas.read_file("https://global-coal-map-2020.s3.eu-west-2.amazonaws.com/data/coal2020.geojson")


# In[34]:


print(geopandas.datasets.get_path('naturalearth_lowres'))
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
base = world.plot(color='white', edgecolor='black')
power_plants.plot(ax=base, color='red', markersize=1)


# In[42]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(15,10))

world.plot(
    ax=ax,
    color="black",
    edgecolor="white"
)

power_plants.plot(
    ax=ax, 
    color='red', 
    markersize=1
)

