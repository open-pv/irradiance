# Calculate solar irradiance
The jupyter notebook provides skripts to calculate solar irradiance averaged over a year. 
It uses the Brunger Hooper algorithm, defined in [[1]](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=93f59805f64fd372d7ce5e18addbeadcc846de6b). 
The generated json consists of a 2D nested array, returning the irradiance for (phi, theta) pairs, where phi and theta are spherical coordinates.

<figure>
    <img src="https://github.com/open-pv/irradiance/assets/74312290/ec18260e-9d6e-4a35-9627-a383f8a07a0e"
         alt="Irradiance Plot in spherical coordiantes, for theta in [0,2*PI] and phi in [0, PI/2]. The color indicates the irradiance.">
    <br/>
    <figcaption>Irradiance as calculated with the jupyter notebook. The color indicates the irradiance coming from the given sky segment, legend is in arbitrary units.</figcaption>
</figure>



