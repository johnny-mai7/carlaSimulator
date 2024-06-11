import pyproj

try:
    pyproj.Proj(init='epsg:4326')
    print("Proj is working correctly.")
except pyproj.exceptions.CRSError as e:
    print(f"Proj error: {e}")

