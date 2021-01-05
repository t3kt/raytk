Reflects space across a plane.

## Parameters

* `Enable`
* `Direction`
  * `custom`: Use a plane defined by a custom normal vector.
  * `xpos`: Reflect the positive X side onto the negative.
  * `xneg`: Reflect the negative X side onto the positive.
  * `ypos`: Reflect the positive Y side onto the negative.
  * `yneg`: Reflect the negative Y side onto the positive.
  * `zpos`: Reflect the positive Z side onto the negative.
  * `zneg`: Reflect the negative Z side onto the positive.
* `Planenormal`: Vector that the cut plane faces. Note that this is only a direction and not a position in space.
* `Offset`: Moves the reflection plane along the normal that it faces.
* `Shift`: Moves the whole resulting shape along the normal.
* `Exposeiteration`: Whether to expose which side of the plane a point is on as an iteration value for upstream ops.

## Inputs

* `definition_in`: 
* `blend_func_definition_in` *Blend Function*: Function used to control blending across the reflection plane.