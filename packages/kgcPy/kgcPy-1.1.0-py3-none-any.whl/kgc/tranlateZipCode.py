import pandas as pd
from importlib import resources
import io

def tranlateZipCode(zipcode):

    zipcode = str(zipcode)

    with resources.open_binary('kgc', 'zipcodes.csv') as fp:
        zipcodes_csv = fp.read()
    df = pd.read_csv(io.BytesIO(zipcodes_csv), index_col=0, dtype={'zip':'string'})
        
    try:
        rows = df.loc[df['zip'] == zipcode]
        if len(rows) == 0:
            return f"No matching rows found for zipcode {zipcode}"
        else:
            return rows
    except Exception as e:
        return f"Search failed: {e}"

