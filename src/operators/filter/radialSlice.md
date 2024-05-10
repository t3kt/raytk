Takes a pie-shaped slice of an SDF around an axis, either removing it or everything except it.

## Parameters

* `Enable`
* `Axis`: The axis around which to take the slice.
  * `x`
  * `y`
  * `z`
* `Anglemode`: How to specify the angles of the slice.
  * `width`: Choose a center angle and a width.
  * `sides`: Choose the start and end angles.
* `Center`: Center angle of the slice in degrees.
* `Width`: Width of the slice in degrees.
* `Start`: Start angle in degrees.
* `End`: End angle in degrees.
* `Invert`: Whether to remove just the slice, or remove everything except the slice.
* `Enablesmoothing`: Whether to smooth the transition on each side of the slice down to a size of zero.
* `Smoothradius`: The amount of smoothing distance.

## Inputs

* `definition_in`: 
* `centerField`: 
* `widthField`: 
* `startField`: 
* `endField`: 