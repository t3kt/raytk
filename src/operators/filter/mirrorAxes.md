Mirror space across one or more axes, similar to `reflect`.

## Parameters

* `Enable`
* `Axes`: Which axes should be reflected.
  * `x`
  * `y`
  * `z`
  * `xy`
  * `yz`
  * `zx`
  * `xyz`
* `Dirx`: Which side of the X axis should be reflected.
  * `pos`
  * `neg`
* `Diry`: Which side of the Y axis should be reflected.
  * `pos`
  * `neg`
* `Dirz`: Which side of the Z axis should be reflected.
  * `pos`
  * `neg`
* `Flipsidex`: Whether to flip one side of the X axis along either the Y or Z axes.
  * `none`
  * `xpos`
  * `xneg`
  * `ypos`
  * `yneg`
  * `zpos`
  * `zneg`
* `Flipsidey`: Whether to flip one side of the Y axis along either the X or Z axes.
  * `none`
  * `xpos`
  * `xneg`
  * `ypos`
  * `yneg`
  * `zpos`
  * `zneg`
* `Flipsidez`: Whether to flip one side of the Z axis along either the X or Y axes.
  * `none`
  * `xpos`
  * `xneg`
  * `ypos`
  * `yneg`
  * `zpos`
  * `zneg`
* `Center`: Center position for the reflection planes.
* `Offset`: Offset applied to each side, pushing them towards / away from the reflection planes.
* `Enableblend`: Whether to stretch out the area near the reflection plane to soften the transition between the sides.
* `Blending`: How much area to stretch out near the reflection planes.
* `Target`: What the reflection should be applied to.
  * `coords`
  * `sdfuv`
  * `sdfuv2`
  * `matuv`
  * `value`

## Inputs

* `definition_in`: 
* `offsetField`: 
* `directionField`: 
* `flipSideField`: 
* `blendingField`: 

## Variables

* `sides`: 