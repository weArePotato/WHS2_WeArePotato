# geoheat
Javascript: In-memory geohash heatmap. Does not visualize, but constructs an in-memory index of geohashes that you can query to determine density of areas.

# Install

```
npm install --save geoheat
```

# Usage
## Create a heatmap
```
var GeohashHeatmap = require('geoheat');
var myMap = new GeohashHeatmap();
```

## Add some points to your map
```
myMap.addLatLong(37.3939829, -122.0802028); // mountain view
myMap.addLatLong(37.758683, -122.457678); // san francisco - sutro open space preserve
myMap.addLatLong(37.768187, -122.504643); // san francisco - golden gate park
myMap.addLatLong(41.849295, -87.610306); // chicago
```

## Query regions to see heat
```
myMap.getLatLongHeat(lat, lng, precision) === { weight, last }
myMap.getLatLongHeat(37.3939829, -122.0802028, 12) === { weight: 1, last: ${time} }
```

Will return a record to you indicating the relative weight of the location at the given precision,
and the last time that a record was added for that location.

The "precision" field corresponds to the precision (length) as described on
[movable-type's geohash page](http://www.movable-type.co.uk/scripts/geohash.html) by Chris Veness,
roughly copied here:

```
1       ≤ 5,000km      ×      5,000km ~= 25000k km^2  (continents)
2       ≤ 1,250km      ×      625km   ~= 781k   km^2
3       ≤ 156km        ×      156km   ~= 24k    km^2
4       ≤ 39.1km       ×      19.5km  ~= 764    km^2  (states or small countries)
5       ≤ 4.89km       ×      4.89km  ~= 23.9   km^2  (large neighboring cities)
6       ≤ 1.22km       ×      0.61km  ~= 0.74   km^2  (neighborhoods)
7       ≤ 153m         ×      153m    ~= 0.02   km^2
8       ≤ 38.2m        ×      19.1m   ~= 748.72 m^2   (large fields/buildings)
9       ≤ 4.77m        ×      4.77m   ~= 22.75  m^2   (parcel of land)
10      ≤ 1.19m        ×      0.596m  ~= 0.7    m^2   (distinguish trees)
11      ≤ 149mm        ×      149mm   ~= 0.0221 m^2   (surveying)
12      ≤ 37.2mm       ×      18.6mm  ~= 0.0007 m^2   (movement of tectonic plates)
```

# License

MIT license. See `LICENSE` file.
