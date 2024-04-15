# Calculate solar irradiance
The jupyter notebook provides skripts to calculate solar irradiance averaged over a year. 
It uses the Brunger Hooper algorithm, defined in [[1]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=93f59805f64fd372d7ce5e18addbeadcc846de6b). 
The generated json consists of a 2D nested array, returning the irradiance for (phi, theta) pairs, where phi and theta are spherical coordinates.
