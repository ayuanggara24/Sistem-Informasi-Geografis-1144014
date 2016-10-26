#!bin/python

import shapefile
sf = shapefile.Reader ("E:\land\land.shp")
print sf
shapes = sf.shapes()
print len (shapes)

# for name in dir(shapes(3)):
#		if not name.startswitch('__'):
#			print name