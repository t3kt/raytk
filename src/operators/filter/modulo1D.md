Repeats space along one axis.

This has the effect of making infinite copies of (slices of) the input, but without the cost
of having to separately calculate each copy.

## Parameters

* `Enable`
* `Axis`: The axis to repeat space along.
  * `x`
  * `y`
  * `z`
* `Size`: The spacing of the repetition. This sets the with of the slice taken from the input.
* `Offset`: Shifts where the input slice is taken from without moving the position of the repetitions.
* `Shift`: Shifts the whole repeated space.
* `Mirrortype`: How to the slices are varied.
  * `none`: No mirroring.
  * `mirror`: Flip every other slice.
* `Uselimit`: Whether to have a limited number of slices instead of an infinite series.
* `Limitstart`: The index of the first slice to show. This can also be a fractional value to cut off part of the first slice (though this can cause rendering issues).
* `Limitstop`: THe index of the last slice to show. This can also be a fractional value to cut off part of the last slice (though this can cause rendering issues).
* `Limitoffset`: Offsets the `Limitstart` and `Limitstop` indices.
* `Iterationtype`: Whether and how to expose iteration values to upstream operators.
  * `none`: Pass along whatever is provided by the next op after this one.
  * `cellcoord`: Use the slice index as the x component of the iteration, with yzw set to 0.
  * `alternatingcoord`: Alternates back and forth between 0 and 1 in the x component, with yzw set to 0.

## Inputs

* `definition_in`: 