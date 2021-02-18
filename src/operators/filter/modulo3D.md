Repeats space along all 3 axes.

This has the effect of making an infinite 3D grid of copies of (slices/cells of) the input, but without the cost of having
to separately calculate each one.

## Parameters

* `Enable`
* `Size`: The spacing of the grid along each axis, which is also the size of the cell that is taken from the input.
* `Offset`: Shifts where the input cell is taken from without moving the position of the grid.
* `Shift`: Shifts the whole grid (and its contents).

## Inputs

* `definition_in`: 