import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon


def plot_poly(b):
    x, y = b.exterior.xy
    return x, y


def outlier(x, m=2):
    outx = np.abs(x - np.median(x)) < (m * np.std(x))
    indx = np.asarray(np.where(outx == False))
    return indx


def remove_spike(poly):
    numPol = len(poly)
    newpol = []
    name = []
    for num in range(numPol):
        x, y = plot_poly(poly.loc[num, 'geometry'])
        coord = [x, y]
        outpolx = (outlier(coord[0]))
        outpoly = (outlier(coord[1]))
        temp1 = np.asarray(coord)
        if len(outpolx) > 0:
            temp2 = np.asarray(outpolx)
        elif len(outpoly) > 0:
            temp2 = np.asarray(outpoly)
        else:
            temp2 = []
        newpol.append(Polygon(np.delete(temp1, temp2, 1).T))
        name.append(poly.loc[num, 'name'])
    newpolygon = {'Name': name, 'Geometry': newpol}
    nPol = gpd.GeoDataFrame(newpolygon, geometry='Geometry')
    return nPol


data = gpd.read_file('D:\KARTOZA\spiky-polygons.gpkg')
f_data = remove_spike(data)

fig1 = plt.figure(dpi=200)
data.plot(ax=plt.gca())

fig2 = plt.figure(dpi=200)
f_data.plot(ax=plt.gca())

f_data.to_file("filtered-polygons.shp")
