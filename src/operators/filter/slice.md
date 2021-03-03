Removes all of an SDF except for a slice in space.

## Parameters

* `Enable`
* `Axis`: The axis along which to take the slice.
  * `x`
  * `y`
  * `z`
* `Offset`: Shifts the center position of the slice along the axis.
* `Thickness`: Thickness of the slice.
* `Enablesmoothing`: Whether to smooth the transition on each side of the slice down to a size of zero.
* `Smoothradius`: The amount of smoothing distance.
* `Enablemirror`: When enabled, a second slice is added, mirrored across the origin along the axis.

## Inputs

* `definition_in`: 