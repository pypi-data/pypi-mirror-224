from PIL import Image
import pandas as pd
Image.MAX_IMAGE_PIXELS = None

def lookupCZ(lat,lon):

    # Load the image file
    img = Image.open('./data/Beck_KG_V1_present_0p0083.tif')
    img_rgb = img.convert('RGB')

    # Get the RGB values of the pixel at position (x, y)
    x = round((lon+180)*(img.size[0])/360 - 0.5)
    y = round(-(lat-90)*(img.size[1])/180 - 0.5)
    r, g, b = img_rgb.getpixel((x, y))
    
    df = pd.read_csv('./data/kg_colors.csv')
    rgb_values = {'R': r, 'G': g, 'B': b}

    # Use the loc method to find the index of the row that matches the input values
    res = df['kg_zone'].loc[(df['R'] == rgb_values['R']) & 
                (df['G'] == rgb_values['G']) & 
                (df['B'] == rgb_values['B'])]

    return res.values[0]


def tranlateZipCode(zipcode):

    zipcode = str(zipcode)
    df = pd.read_csv('./data/zipcodes.csv', index_col=0, dtype={'zip':'string'})
        
    try:
        rows = df.loc[df['zip'] == zipcode]
        if len(rows) == 0:
            return f"No matching rows found for zipcode {zipcode}"
        else:
            return rows
    except Exception as e:
        return f"Search failed: {e}"

