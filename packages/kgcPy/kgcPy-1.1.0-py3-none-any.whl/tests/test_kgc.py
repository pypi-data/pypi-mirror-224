#%%
from kgcPy import *

#%%
zipcode = '02134'
lat,lon = translateZipCode(zipcode)
kg_zone = lookupCZ(lat, lon)
print('Koppen geiger zone is '+kg_zone)
res_irrQuan = irradianceQuantile(kg_zone)
res_irrQuan[0]
#%%
print('The 98%, 80%, 50%, and 30% irradiance quantile of '+ kg_zone +' respectively is ' + res_irrQuan[0] + res_irrQuan[1] + res_irrQuan[2])
#%%
res_nearbyCZ = nearbyCZ(lat,lon,size=10)
print('Possible nearby kg zones are ' + str(res_nearbyCZ[2]))
res_nearbyCZ
# %%
## lookupCZ data frame demo
# create a data frame
data = pd.DataFrame({'Site': ['GC', 'UFS', 'NEG'], 
                     'Longitude': [-15.42, 10.98, 34.78],
                     'Latitude': [27.82, 47.42, 30.86]})
data['CZ'] = data.apply(lambda rows: lookupCZ(rows['Latitude'], rows['Longitude']), axis=1)
data
# %%
## translateZipCode data frame demo
# create a data frame
data = pd.DataFrame({'zip': [44106, '00638', '01106']})
data[['lat','lon']] = data.apply(lambda rows: translateZipCode(rows['zip']), axis=1).apply(pd.Series)
data

# %%
zipcode = '44106'
lat, lon = translateZipCode(zipcode)
res = nearbyCZ(lat,lon)
res
# %%
a, b = res
# %%
a
# %%
data = pd.DataFrame({'Site': ['GC', 'UFS', 'NEG'], 
                     'Longitude': [-15.42, 10.98, 34.78],
                     'Latitude': [27.82, 47.42, 30.86]})
data[['CZ', 'uncertaintyNearbyCZ', 'nearbyCZ']] = data.apply(lambda rows: nearbyCZ(rows['Latitude'], rows['Longitude']), axis=1).apply(pd.Series)
data

# %%
lat = 27.82	
lon = -15.42
res = nearbyCZ(lat,lon)
res
# %%
data = pd.DataFrame({'Site': ['GC', 'UFS', 'NEG'], 
                     'Longitude': [-15.42, 10.98, 34.78],
                     'Latitude': [27.82, 47.42, 30.86]})
data[['CZ', 'uncertaintyNearbyCZ', 'nearbyCZ']] = data.apply(lambda rows: nearbyCZ(rows['Latitude'], rows['Longitude'], size=8), axis=1).apply(pd.Series)
data
# %%
zipcode = '44106'
lat, lon = translateZipCode(zipcode)
res = nearbyCZ(lat,lon,size=3)
res
# %%
zipcode = '44106'
lat, lon = translateZipCode(zipcode)
res = nearbyCZ(lat,lon,size=10)
res
# %%
zipcode = '44106'
lat, lon = translateZipCode(zipcode)
res = nearbyCZ(lat,lon,size=50)
res
# %%
zipcode = '44106'
lat, lon = translateZipCode(zipcode)
res = nearbyCZ(lat,lon,size=100)
res
# %%
kg_zone = 'BWh'
res = irradianceQuantile(kg_zone)
res
# %%
kg_zone = 'ET'
res = irradianceQuantile(kg_zone)
res
# %%
data = pd.DataFrame({'Site': ['GC', 'UFS', 'NEG'], 
                     'Longitude': [-15.42, 10.98, 34.78],
                     'Latitude': [27.82, 47.42, 30.86]})
data['CZ'] = data.apply(lambda rows: lookupCZ(rows['Latitude'], rows['Longitude']), axis=1)
data


# %%
data
# %%

climate_colors = ["#960000", "#FF0000", "#FF6E6E", "#FFCCCC", "#CC8D14", "#CCAA54", "#FFCC00", "#FFFF64",
                  "#007800", "#005000", "#003200", "#96FF00", "#00D700", "#00AA00", "#BEBE00", "#8C8C00",
                  "#5A5A00", "#550055", "#820082", "#C800C8", "#FF6EFF", "#646464", "#8C8C8C", "#BEBEBE",
                  "#E6E6E6", "#6E28B4", "#B464FA", "#C89BFA", "#C8C8FF", "#6496FF", "#64FFFF", "#F5FFFF"]

# %%
import matplotlib.colors as mcolors
import pandas as pd

# Define the R color list
climate_colors = ["#960000", "#FF0000", "#FF6E6E", "#FFCCCC", "#CC8D14", "#CCAA54", "#FFCC00", "#FFFF64",
                  "#007800", "#005000", "#003200", "#96FF00", "#00D700", "#00AA00", "#BEBE00", "#8C8C00",
                  "#5A5A00", "#550055", "#820082", "#C800C8", "#FF6EFF", "#646464", "#8C8C8C", "#BEBEBE",
                  "#E6E6E6", "#6E28B4", "#B464FA", "#C89BFA", "#C8C8FF", "#6496FF", "#64FFFF", "#F5FFFF"]

# Initialize lists to store RGB values
red = []
green = []
blue = []

# Convert colors to 255 RGB values
for color in climate_colors:
    rgb = mcolors.hex2color(color)
    red.append(int(rgb[0] * 255))
    green.append(int(rgb[1] * 255))
    blue.append(int(rgb[2] * 255))

charvec = ['Af', 'Am', 'As', 'Aw',
               'BSh', 'BSk', 'BWh', 'BWk',
               'Cfa', 'Cfb', 'Cfc',
               'Csa', 'Csb', 'Csc',
               'Cwa', 'Cwb', 'Cwc',
               'Dfa', 'Dfb', 'Dfc', 'Dfd',
               'Dsa', 'Dsb', 'Dsc', 'Dsd',
               'Dwa', 'Dwb', 'Dwc', 'Dwd',
               'EF', 'ET', 'Ocean']

# Create a dataframe with 255 RGB values
df_colors = pd.DataFrame({"kg_zone": charvec, "R": red, "G": green, "B": blue})

# Print the 255 RGB dataframe
print(df_colors)

# %%
df_colors.to_csv('kg_colors.csv')
# %%
charvec = ['Af', 'Am', 'As', 'Aw',
               'BSh', 'BSk', 'BWh', 'BWk',
               'Cfa', 'Cfb', 'Cfc',
               'Csa', 'Csb', 'Csc',
               'Cwa', 'Cwb', 'Cwc',
               'Dfa', 'Dfb', 'Dfc', 'Dfd',
               'Dsa', 'Dsb', 'Dsc', 'Dsd',
               'Dwa', 'Dwb', 'Dwc', 'Dwd',
               'EF', 'ET', 'Ocean']
len(charvec)
# %%
