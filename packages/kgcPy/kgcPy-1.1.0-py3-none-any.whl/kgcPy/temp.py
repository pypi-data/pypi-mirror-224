#%%
from PIL import Image
import pandas as pd
import webcolors

# %%
img = Image.open('kmz_int_reshape.png')

# %%
img.getpixel((100,200))
# %%
import numpy as np
np.amin(img)

# %%
lat = 27.82	
lon = -15.42

img = Image.open('KG_1986-2010.png')
img_rgb = img.convert('RGB')

# Get the RGB values of the pixel at position (x, y)
x = round((lon+180)*(img.size[0])/360 - 0.5)
y = round(-(lat-90)*(img.size[1])/180 - 0.5)
r, g, b = img_rgb.getpixel((x, y))
# %%
r
# %%
g
# %%
b
# %%
rgb = img_rgb.getpixel((x, y))
hex_code = webcolors.rgb_to_hex(rgb)
# %%
hex_code