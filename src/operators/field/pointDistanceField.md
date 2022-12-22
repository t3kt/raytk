A float field that provides the distance from a specific point in space from either the current position or from another point.

## Parameters

* `Center`: The point from which distance is measured.
* `Coordtype`: The type of coordinates to use.
  * `float`
  * `vec2`
  * `vec3`
* `Axes`: Which axes to use when calculating distances.
  * `xyz`
  * `xy`
  * `yz`
  * `xz`
  * `x`
  * `y`
  * `z`

## Inputs

* `coordField`: If provided, this is used to produce positions instead of the actual coordinates.
* `centerField`: If provided, this is used to produce the center position instead of the Center parameter.