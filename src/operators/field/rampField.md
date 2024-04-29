Field that produces values that fade from one value to another along an axis or line.

## Parameters

* `Enable`
* `Coordmode`: Whether to specify the ends of the ramp using an axis or arbitrary points.
  * `axis`
  * `points`
* `Axis`: Which axis of the position (or coord input) the ramp should use.
  * `x`
  * `y`
  * `z`
  * `dist`
* `Range`: The start and end of the ramp along the chosen axis.
* `Point1`: The start point when using arbitrary points.
* `Point2`: The ened point when using arbitrary points.
* `Extendmode`: How to handle points outside the specified range.
  * `hold`
  * `zero`
  * `repeat`
  * `mirror`
* `Returntype`: What type of values to produce (single number floats or vectors).
  * `float`
  * `vec4`
* `Value1`: The value at the start of the ramp. If in float mode only the first part is used.
* `Value2`: The value at the end of the ramp. If in float mode only the first part is used.
* `Coordtype`
  * `auto`
  * `float`
  * `vec2`
  * `vec3`

## Inputs

* `coordField`: 
* `point1Field`: 
* `point2Field`: 
* `easingFunc`: 