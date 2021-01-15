Mirror coordinates across two axes and the diagonals.

## Parameters

* `Enable`
* `Axis`: Axis that faces the plane where coordinates are mirrored.
  * `x`
  * `y`
  * `z`
* `Size`: Spacing of the reflection planes.
* `Offset`: Shifts the input before applying reflection.
* `Rotateaxis`: Rotates the input before applying reflection.
* `Iterateoncells`: Enables upstream operators to check which cell in the reflection grid a point is in.

## Inputs

* `definition_in`: 
* `rotate_axis_field_definition_in` *Rotate Axis Field*: Value field used to vary the `Rotateaxis`. If the field is a 1D field, it is given the distance from the center. If it is a 2D field, it is given the position along the mirror axes. If it is a 3D field, it is given the raw position. The value is converted to radians and *added* to the `Rotateaxis` parameter.