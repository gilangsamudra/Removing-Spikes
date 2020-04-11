# Removing Spikes
This code uses the following python libraries:
1. Geopandas
2. Numpy
3. Matplotlib
4. Shapely

The objectives of the program is to remove all detected spikes from polygons data.
There are 4 conditions of a polygon, the figure below shows the example of polygon conditions.

![Polygon Types](https://user-images.githubusercontent.com/44993635/79042791-e02e0280-7c24-11ea-9776-b5f6bc057e05.png)

As we can see, the polygon number 1 is polygon without spike and the others are polygon with a spike but have different orientation. Orientation of a polygon plays an important role in this program. It determines the sensitivity of detecting spikes in the polygon data in x and/or y direction on Cartesian plane.

Basically, a polygon is formed with number of straight lines, and those lines are formed by number of points.
I use this basic definition of polygon to develop a program that can detect spikes of any polygon.

The first step is to extract the polygon data to get the coordinates of all points that form a polygon.
The next step is to treat the spike point as an outlier of our data set (data points). I use a simple method to filter out an outlier in a data set.
![outlier](https://user-images.githubusercontent.com/44993635/79043194-f12c4300-7c27-11ea-8793-18623cce7fed.png)

where std(x) is deviation standard of vector x and m is a constant we specify to determine the thresshold of the filter. 

The key idea is if we are able to detect the outlier then we can filter it out from our data set. It means removing the spike-point that distorts our polygon. The final step is to reconstruct the polygon with the new data set (the filtered data).

Below is the result of the spike-filtering program that I develop:
### Raw Data
![spiky polygon](https://user-images.githubusercontent.com/44993635/79043537-ebcff800-7c29-11ea-9364-fef1a8a68460.png)

### Filtered Data
![Filtered Polygon](https://user-images.githubusercontent.com/44993635/79043769-909f0500-7c2b-11ea-8986-746d79967624.png)
