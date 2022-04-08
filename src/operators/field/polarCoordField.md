A field that produces various types of polar coordinates.

## Parameters

* `Format`
  * `polar`: Produces a vector with X: distance, Y: angle, Z: position along center axis.
  * `spherical`: Produces a vector with X: distance, Y: angle 1, Z: angle 2.
  * `planedist`: Produces a single float value with distance along a plane (ignoring one axis).
  * `dist`: Produces a single float value with distance from the center point.
* `Angleunit`
  * `ratio`
  * `degrees`
  * `radians`
* `Axis`
  * `x`
  * `y`
  * `z`
* `Center`: The center point of the polar coordinates.
* `Coordtype`
  * `auto`
  * `float`
  * `vec2`
  * `vec3`
* `Contexttype`
  * `auto`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`
  * `ParticleContext`