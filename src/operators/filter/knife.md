Cuts off an SDF along a plane.

## Parameters

* `Enable`
* `Side`: Which side of the cut to keep.
  * `above`
  * `below`
* `Offset`: Shifts the cut plane along the axis that it faces.
* `Rotateplane`: Rotate the cut plane in XYZ. When in 2D, only the Z rotation is used.
* `Axis`
  * `x`
  * `y`
  * `z`
* `Enablesmoothing`: Whether to smooth the transition on each side of the slice down to a size of zero.
* `Smoothradius`: The amount of smoothing distance.

## Inputs

* `definition_in`: 
* `offsetField`: 