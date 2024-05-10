Repeats space along a line, similar to `modulo1D`.

Similar to `modulo1D`, this operator repeats space in a row of slices. But instead of being on an axis, it uses an arbitrary line defined by two points, with a fixed number of evenly spaced slices between them.

## Parameters

* `Enable`
* `Point1`
* `Point2`
* `Divisions`: Number of slices.
* `Mirrortype`: Whether to flip alternating slices, which can be useful for ensuring that shapes line up with their neighbors if they get cut off.
  * `none`
  * `mirror`

## Inputs

* `definition_in`: 

## Variables

* `cellcoord`: Cell index, 0, 1, 2, etc.
* `normcoord`: Cell index, scaled to a 0..1 range.