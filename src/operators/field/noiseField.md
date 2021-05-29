A float or vector field that uses one of several noise functions.

Some of these may be costly to compute, so pay attention to frame rate when using them.

The different types of noise use different types of coordinates. If the type of coordinate used
by `Noisetype` doesn't match the `Coordtype`, any missing parts will be replaced with zeros.
When the `Coordtype` is 3D but the `Noisetype` only uses 2D, the `Axis` parameter determines
which parts of the coordinates are used.

For types that use 4D coordinates, the `Translate` and `Scale` parameters can still be used to control the 4th coordinate.

## Parameters

* `Noisetype`: The type of noise function.
  * `TDSimplexNoise2d`
  * `TDSimplexNoise3d`
  * `TDSimplexNoise4d`
  * `TDPerlinNoise2d`
  * `TDPerlinNoise3d`
  * `TDPerlinNoise4d`
  * `classicperlin2d`
  * `classicperlin3d`
  * `classicperlin4d`
  * `simplex2d`
  * `simplex3d`
  * `simplex4d`
* `Coordtype`: The type of coordinates that the op supports.
  * `vec2`
  * `vec3`
* `Contexttype`
* `Axis`: When the `Noisetype` uses 2D coordinates but `Coordtype` is 3D, this is used to choose which plane of the coordinates are used.
  * `x`: Use Y and Z.
  * `y`: Use Z and X.
  * `z`: Use X and Y.
* `Translate`: Offsets the coordinates used to calculate noise.
* `Scale`: Scales the coordinates used to calculate noise.
* `Amplitude`: Multiplies the amount produced by the noise.
* `Offset`: Offsets (adds to) the amount produced by the noise.