Flips the input across an axis, either on its own or merged with the original.

## Parameters

* `Enable`
* `Axis`
  * `x`
  * `y`
  * `z`
* `Offset`: Moves the reflection plane along the axis.
* `Shift`: Moves the input towards / away from the reflection plane.
* `Mergetype`: Whether to just flip the input or flip it and merge that with the original.
  * `none`
  * `union`
  * `smoothUnion`
* `Mergeradius`
* `Iterationtype`: What kind of iteration values should be provided for upstream ops.
  * `none`
  * `index`: The original is assigned 0, flipped 1.
  * `sign`: Original is assigned 1, flipped -1.

## Inputs

* `definition_in`: 