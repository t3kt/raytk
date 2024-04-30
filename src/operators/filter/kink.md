Bends space, similar to the `bend`.

The bending that this operator applies is slightly different than the `bend` operator, and is asymmetrical, causing a tighter bend on one side based on the bend amount and direction.

Based on [Bending an SDF](https://www.shadertoy.com/view/3llfRl) by blackle.

## Parameters

* `Enable`
* `Direction`: Which axis to bend around on which plane.
  * `xy`: Bends along the X axis, in the Y direction
  * `xz`: Bends along the X axis, in the Z direction
  * `yx`: Bends along the Y axis, in the X direction
  * `yz`: Bends along the Y axis, in the Z direction
  * `zx`: Bends along the Z axis, in the X direction
  * `zy`: Bends along the Z axis, in the Y direction
* `Side`: Which side to bend towards.
  * `neg`
  * `pos`
* `Amount`: Amount of bending.
* `Offset`: Position along the 
* `Spread`: Range over which the bending is spread. Higher values mean a more gradual bend.

## Inputs

* `definition_in`: 
* `amountField`: 
* `offsetField`: 
* `spreadField`: 