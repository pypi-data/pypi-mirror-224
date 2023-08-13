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