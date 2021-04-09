A pyramid with four sides.

## Parameters

* `Translate`: Moves the center of the base of the pyramid.
* `Height`: The height of the pyramid.
* `Width`: The width of the base of the pyramid. Note that widths smaller than 0.5 will produce rendering errors.
* `Axis`
  * `x`
  * `y`
  * `z`

## Inputs

* `height_field_definition_in`: Optional field used to determine the height. When connected, the `Height` is multiplied by the value produced by the field.
* `width_field_definition_in`: Optional field used to determine the width. When connected, the `Width` is multiplied by the value produced by the field.