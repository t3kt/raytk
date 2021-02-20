A prism shape, like a cylinder but with flat sides, along the z axis.

## Parameters

* `Prismtype`: The number of sides of the prism.
  * `tri`
  * `square`
  * `hex`
  * `octogon`
* `Translate`: Moves the center of the prism.
* `Radius`: The radius of the prism. If the radius field input is connected, this is not used.
* `Height`: The height / length of the prism. If the height field input, this is not used.
* `Axis`
  * `x`
  * `y`
  * `z`

## Inputs

* `height_field_definition_in` *Height field*: Float value field that controls the height of the prism.
* `radius_field_definition_in` *Radius field*: Float value field that controls the radius of the prism. 