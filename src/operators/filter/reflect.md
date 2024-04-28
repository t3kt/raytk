Reflects space across a plane.

## Parameters

* `Enable`
* `Direction`: Axis and direction across which to reflect.
* `Planenormal`: Vector that the cut plane faces. Note that this is only a direction and not a position in space.
* `Offset`: Moves the reflection plane along the normal that it faces.
* `Shift`: Moves the whole resulting shape along the normal.
* `Exposeiteration`: Whether to expose which side of the plane a point is on as an iteration value for upstream ops.
* `Enableblend`: Whether to stretch out the space near the reflection plane to smooth out the border between the sides.
* `Blend`: How much to stretch the space near the reflection plane.
* `Iterationtype`: How to expose information about the current side as iteration values.
  * `none`
  * `index`
  * `sign`

## Inputs

* `definition_in`: 
* `offsetField`: 
* `shiftField`: 

## Variables

* `sign`: +1, -1 indicating the current side of the reflection.
* `index`: 0, 1 indicating the current side of the reflection.