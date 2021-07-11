Mirror coordinates across two axes.

This is similar to `mirrorOctant` but without mirroring on the diagonals.

## Parameters

* `Enable`
* `Axis`: Axis that faces the plane where coordinates are mirrored.
  * `x`
  * `y`
  * `z`
* `Size`: Spacing of the reflection planes.
* `Offset`: Shifts the input before applying reflection.
* `Rotateaxis`: Rotates the input before applying reflection.
* `Iterationtype`: Exposes information to upstream operators about which quadrant a point is in.
  * `none`
  * `index`: Numbers the quadrants from 0 to 3.
  * `sign`: Populates the x and y parts of the iteration value with 1 or -1 for different sides of the dividing planes.

## Inputs

* `definition_in`: 
* `rotate_axis_field_definition_in` *Rotate Axis Field*: Value field used to vary the `Rotateaxis`. If the field is a 1D field, it is given the distance from the center. If it is a 2D field, it is given the position along the mirror axes. If it is a 3D field, it is given the raw position. The value is converted to radians and *added* to the `Rotateaxis` parameter.* `offset_field_definition_in`: 
