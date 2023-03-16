from shapely.geometry import shape, Point
import json


# Find country that contains the point
def find_country(lat, long, map = None):

    # Load GeoJSON file containing sectors
    if map:
        gjs = map
    else:
        with open('geojson/world-administrative-boundaries.geojson') as f:
            gjs = json.load(f)

    # Construct point based on lon/lat returned by geocoder
    point = Point(long, lat)
    
    # Check each polygon (country) to see if it contains the point
    for feature in gjs['features']:
        polygon = shape(feature['geometry'])
        
        # If country contains the point, return the country name
        if polygon.contains(point):
            return feature['properties']['name']
        
    return None

def main():
    with open('world-administrative-boundaries.geojson') as f:
        gjs = json.load(f)
    # Tests for find_country
    print("Test 1: Washington, DC (USA)")
    lat = 38.8977
    long = -77.0365
    print(find_country(lat, long, gjs))
    
    print("Test 2: London (UK)")
    lat = 51.5074
    long = 0.1278
    print(find_country(lat, long))
    
    print("Test 3: Sydney (Australia)")
    lat = -33.8688
    long = 151.2093
    print(find_country(lat, long))

if __name__ == '__main__':
    main()
    