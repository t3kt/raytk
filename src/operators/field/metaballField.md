Metaball value field.

## Parameters

* `Coordtype`
  * `float`
  * `vec2`
  * `vec3`
* `Center`: Center position of the ball.
* `Radius`: Radius of the ball on each axis. In 2D mode, only x and y are used. In 1D only x is used.
* `Radiusscale`: Scales the radius on all axes.
* `Weight`: The returned values are multiplied by this.
* `Exponent`: Controls the shape of the ball by applying exponential scaling to coordinates.
* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`
* `Inspect`
* `Help`