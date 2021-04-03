Field that provides values from a CHOP.

## Parameters

* `Coordtype`
  * `float`
  * `vec2`
  * `vec3`
* `Returntype`
  * `float`
  * `vec4`
* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Axis`: Which axis to use to determine the position in the CHOP to use.
  * `x`
  * `y`
  * `z`
* `Translate`: Offsets the coordinate value. This is applied before the "Extend Mode".
* `Scale`: Scales the coordinate value. This is applied before the "Extend Mode".
* `Chop`
* `Extendmode`: How to handle coordinates outside the 0..1 range.
  * `hold`: Clamp the coordinates to the 0..1 range.
  * `zero`: Return zero outside of the 0..1 range.
  * `repeat`: Repeat coordinates outside the 0..1 range.
  * `mirror`: Repeat coordinates outside the 0..1 range, mirrored back and forth.

## Inputs

* `coord_field_definition_in`: If connected, this field is used to determine what position in the CHOP to use at each point.