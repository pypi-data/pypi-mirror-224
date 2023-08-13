# kgc
Aids in identifying the Koeppen-Geiger (KG) climatic zone for
a given lat and lon of any location. The resolution of KG map is at 0.0083 degree or approximately 1 km at the equator, reported by Beck et al. [2018]. 

Beck, H.E., N.E. Zimmermann, T.R. McVicar, N. Vergopolan, A. Berg, E.F. Wood: Present and future Köppen-Geiger climate classification maps at 1-km resolution, Nature Scientific Data, 2018.


# Features
 - lookupCZ(lat, lon): identify the Koeppen-Geiger (KG) climatic zone for a given lat and lon
 - tranlateZipCode('zipcode'): find the lat and lon for a given 'zipcode'
 - nearbyCZ(lat,lon,size=1): get possible climate zones from nearby 8 pixels, and compare to the center pixel
 
#  Setup
1. Install it at bash
```bash
$ pip install kgcPy
```
2.	Import it in python
```python
from kgcPy import *
``` 
#  A quick example
***Find KG zone for a given zipcode***
```python
zipcode = translateZipCode('02134')
lat = zipcode['lat'].iloc[0]
lon = zipcode['lon'].iloc[0]
res = lookupCZ(lat, lon)
res
``` 
***Output will be KG zone***

#  Versions
All notable changes to this project will be documented in this file.
## [1.1.0] - 2023-05-18

## Funding Acknowledgements:
