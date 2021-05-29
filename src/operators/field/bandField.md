Field that applies values based on a band/slice of an axis.

For example, this can be used to have one color within Z = 0.3 to 0.5, and another color for all other coordinates.

See also the `slice` operator, which behaves similarly for SDF results.

## Parameters

* `Coordtype`
  * `float`
  * `vec2`
  * `vec3`
* `Axis`
  * `x`
  * `y`
  * `z`
  * `dist`
* `Center`: The center position along the axis of the "inside" part of the band.
* `Width`: The width of the "inside" part of the band, along the axis.
* `Enableblending`: Whether to smooth the transition between "inside" and "outside" vs a hard cutoff.
* `Blending`: The blending distance between "inside" and "outside". This applies to both borders of the "inside" area. 
* `Returntype`: Whether to produce a single float value or a vector with 4 parts.
  * `float`
  * `vec4`
* `Insidevalue`: The value used for the "inside" part. If `Return Type` is `Float`, only the first parameter will be used.
* `Outsidevalue`: The value used for the "outside" part. If `Return Type` is `Float`, only the first parameter will be used.
* `Contexttype`
  * `auto`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`

## Inputs

* `coord_field_definition_in`: Optional float field that can be used as an alternative coordinate source (instead of using the `Axis` parameter).
* `inside_value_definition_in`: Optional field that is used to produce the values for the "inside" part. If used, the `Inside Value` parameter will be ignored.
* `outside_value_definition_in`:  Optional field that is used to produce the values for the "outside" part. If used, the `Outside Value` parameter will be ignored.
* `blend_function_definition_in`: Optional function used to control how `Blending` is applied.