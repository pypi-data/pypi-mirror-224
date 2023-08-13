from PIL import Image
import pandas as pd
from importlib import resources
import io
Image.MAX_IMAGE_PIXELS = None

def lookupCZ(lat,lon):

    # Load the image file
    with resources.open_binary('kgc', 'Beck_KG_V1_present_0p0083.tif') as fp:
        img = fp.read()
    img = Image.open(io.BytesIO(img))
    img_rgb = img.convert('RGB')

    # Get the RGB values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)
    r, g, b = img_rgb.getpixel((x, y))
    
    with resources.open_binary('kgc', 'kg_colors.csv') as fp:
        kg_colors = fp.read()
    df = pd.read_csv(io.BytesIO(kg_colors))
    rgb_values = {'R': r, 'G': g, 'B': b}

    # Use the loc method to find the index of the row that matches the input values
    res = df['kg_zone'].loc[(df['R'] == rgb_values['R']) & 
                (df['G'] == rgb_values['G']) & 
                (df['B'] == rgb_values['B'])]

    return res.values[0]

def translateZipCode(zipcode):

    zipcode = str(zipcode)

    with resources.open_binary('kgc', 'zipcodes.csv') as fp:
        zipcodes_csv = fp.read()
    df = pd.read_csv(io.BytesIO(zipcodes_csv), index_col=0, dtype={'zip':'string'})
        
    try:
        rows = df.loc[df['zip'] == zipcode]
        if len(rows) == 0:
            return f"No matching rows found for zipcode {zipcode}"
        else:
            return rows['lat'].iloc[0], rows['lon'].iloc[0]
    except Exception as e:
        return f"Search failed: {e}"

def irradianceQuantile(kg_zone):

    # kg_zone = str(kg_zone)

    with resources.open_binary('kgc', 'df_quantile.csv') as fp:
        irradianceQuantile_csv = fp.read()
    df = pd.read_csv(io.BytesIO(irradianceQuantile_csv), index_col=0, dtype={'kg_zone':'string'})
        
    try:
        rows = df.loc[df['kg_zone'] == kg_zone]
        if len(rows) == 0:
            return f"Climate zone {kg_zone} doesn't exist"
        else:
            return rows['quantilep98'].iloc[0], rows['quantilep80'].iloc[0], rows['quantilep50'].iloc[0], rows['quantilep30'].iloc[0]
    except Exception as e:
        return f"Search failed: {e}"

# The inputed number to nearest ’fine’ (100s) resolution grid point.
def roundCoordinates(lat,lon):

    # Load the image file
    with resources.open_binary('kgc', 'Beck_KG_V1_present_0p0083.tif') as fp:
        img = fp.read()
    img = Image.open(io.BytesIO(img))

    # Get the RGB values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)

    lonRound = (x + 0.5) * 360 / img.size[0] - 180
    latRound = - (y + 0.5) * 180 / img.size[1] + 90

    return latRound, lonRound

#get possible climate zones from nearby 8 pixels, and compare to the center pixel 
def nearbyCZ(lat,lon,size=1):

    # Load the image file
    # Test
    # img = Image.open('Beck_KG_V1_present_0p0083.tif')
    with resources.open_binary('kgc', 'Beck_KG_V1_present_0p0083.tif') as fp:
        img = fp.read()
    img = Image.open(io.BytesIO(img))
    img_rgb = img.convert('RGB')

    # Get the RGB values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)
 
    # Test
    # df = pd.read_csv('kg_colors.csv')
    with resources.open_binary('kgc', 'kg_colors.csv') as fp:
        kg_colors = fp.read()
    df = pd.read_csv(io.BytesIO(kg_colors))

    climateZones = []
    climateZone = ''

    for i in range(x-size, x+size+1):
        for j in range(y-size, y+size+1):
            try:
                r, g, b = img_rgb.getpixel((i, j))
                rgb_values = {'R': r, 'G': g, 'B': b}
                # Use the loc method to find the index of the row that matches the input values
                cz = df['kg_zone'].loc[(df['R'] == rgb_values['R']) & 
                        (df['G'] == rgb_values['G']) & 
                        (df['B'] == rgb_values['B'])]
                climateZones.append(cz.values[0])
                if i == x and j == y:
                    climateZone = cz.values[0]
            except IndexError:
                pass
    
    climateZones_series = pd.Series(climateZones)
    climateZones_counts = climateZones_series.value_counts()
    climateZones_percentage = climateZones_counts / climateZones_counts.sum()
    uncertaintyNearbyCZ = climateZones_percentage[climateZone]

    nearbyCZ = climateZones_series.unique().tolist()
    nearbyCZ.remove(climateZone)

    return climateZone, uncertaintyNearbyCZ, nearbyCZ

# # %%
# # Test
# from PIL import Image
# import pandas as pd
# Image.MAX_IMAGE_PIXELS = None
# # %%
# res = nearbyCZ(13,120)
# res
# # %%
# img = Image.open('Beck_KG_V1_present_0p0083.tif')

# # %%
# import os
# print(os.getcwd())
# # %%

# lat = 30
# lon = 120
# size = 1

# # %%
# img = Image.open('Beck_KG_V1_present_0p0083.tif')
# # with resources.open_binary('kgc', 'Beck_KG_V1_present_0p0083.tif') as fp:
# #     img = fp.read()
# # img = Image.open(io.BytesIO(img))
# img_rgb = img.convert('RGB')

# # Get the RGB values of the pixel at position (x, y)
# x = round((lon+180)*(img.size[0])/360 - 0.5)
# y = round(-(lat-90)*(img.size[1])/180 - 0.5)

# # Get the pixels within the surrounding area
# # left = x - size
# # upper = y - size
# # right = x + size
# # lower = y + size
# # pixels = img.crop((left, upper, right, lower))
# # img_rgb = pixels.convert('RGB')

# # %%
# # Test
# df = pd.read_csv('kg_colors.csv')
# # with resources.open_binary('kgc', 'kg_colors.csv') as fp:
# #     kg_colors = fp.read()
# # df = pd.read_csv(io.BytesIO(kg_colors))

# climateZones = []

# for i in range(x-1, x+2):
#     for j in range(y-1, y+2):
#         try:
#             r, g, b = img_rgb.getpixel((i, j))
#             rgb_values = {'R': r, 'G': g, 'B': b}
#             # Use the loc method to find the index of the row that matches the input values
#             cz = df['kg_zone'].loc[(df['R'] == rgb_values['R']) & 
#                     (df['G'] == rgb_values['G']) & 
#                     (df['B'] == rgb_values['B'])]
#             climateZones.append(cz.values[0])
#             if i == x and j == y:
#                 climateZone = cz.values[0]
#         except IndexError:
#             pass
                

# climateZones

# # %%
# len(climateZones)
# # %%
# climateZone
# # %%
# climateZones_series = pd.Series(climateZones)
# # climateZones_series = climateZones
# #%%
# climateZones_series
# #%%
# climateZones_percentage = climateZones_series.value_counts() / climateZones_series.value_counts().sum()
# # %%
# climateZones_percentage
# #%%
# climateZones_percentage['Cfa']
# #%%
# climateZones_percentage[climateZone]
# #%%
# print()
# #%%
# # Create a DataFrame from the counts
# climateZones_df = pd.DataFrame({'nearbyCZ': climateZones_percentage.index, 'percentageCZ': climateZones_percentage})
# climateZones_df
# # r, g, b = img_rgb.getpixel((x, y))

# # possibleCZ = climateZones_series
# # CZuncertainty = climateZones_counts

# # return climateZones_df
# # %%
# img_rgb.size
# # %%


# # %%
# climateZones_df
# # %%
# climateZones_percentage
# # %%
