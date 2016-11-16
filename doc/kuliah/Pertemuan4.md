## MEET 4


.shp Is one form of a file that resides in the shapefile that stores the data of geometry. In shp file contained some data such as:
Bbox a boundary box are the coordinates of 4 points or coordinates of the boundary on the map that berbetuk view rectangle in the map.
Shape Type there are several types, such as:
Point: 1 standard bernomorkan point coordinates from ESRI.
Polyline: coordinates of the points that make up the line but does not establish a standard bernomorkan area 3 of ESRI.
Polygon: coordinate establish standard bernomorkan area 5 of ESRI.
Reads the number of the geometry data in python:
shapefile import
sf = shapefile.Reader ( "negara.shp")
shapes
x = sf.shapes ()
print len ​​(x)

.dbf format

.dbf Format is a file format that can store files tabular and store data attributes.

Reads the number of the geometry data in python:

shapefile import
records ()
records (n)
