A field that switches between two values at a threshold point.

This can be used to apply one color to the left of some point and another color on the right side of that point.
It can also smooth out the transition between the two values.

## Parameters

* `Enable`
* `Coordtype`
  * `float`
  * `vec2`
  * `vec3`
* `Axis`
  * `x`
  * `y`
  * `z`
  * `dist`
* `Edge`
* `Reverse`
* `Enableblend`
* `Blend`
* `Returntype`
  * `float`
  * `vec4`
* `Value1`: Value used when below `Edge`
* `Value2`: Value used when above `Edge`
* `Contexttype`
  * `auto`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`

## Inputs

* `definition_in`: Optional field whose value is used instead of coordinates when checking which side of the threshold a point is on.