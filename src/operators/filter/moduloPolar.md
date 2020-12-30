Repeats space radially, like a kaleidoscope.

## Parameters

* `Axis`: The axis around which space is sliced.
  * `x`
  * `y`
  * `z`
* `Repetitions`: The number of angle repetitions. For example, a value of 6 would mean 6 slices of space, each with a 60 degree width.
* `Roundtointeger`: Whether to round the `Repetitions` (and `Limit Low` and `Limit High`) to whole integers.
* `Prerotate`: Rotation applied before slicing.
* `Rotate`: Rotation applied after slicing.
* `Mirrortype`: Whether to flip every other slice. This is useful to avoid hard breaks at edges. It will result in the appearance of half as many slices, since half of them will be flipped.
  * `none`
  * `mirror`
* `Offset`: Distance to shift the shape before slicing it.
* `Uselimit`: Whether to limit the range of repetitions. Space outside that range will be left as it is.
* `Limitlow`: Start or the repetition range, in terms of the number of repetitions.
* `Limithigh`: End or the repetition range, in terms of the number of repetitions.
* `Iterateoncells`: Whether to expose the slice number as an "iteration" value for upstream ops.
* `Enable`
* `Inspect`
* `Help`

## Inputs

* `definition_in`: 