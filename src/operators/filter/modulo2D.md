Repeats space along 2 axes.

This has the effect of making an infinite grid of copies of (slices/cells of) the input, but without the cost of having
to separately calculate each copy.

## Parameters

* `Enable`
* `Axis`: The axis facing the plane along which space is repeated.
  * `x`: Repeat space on the Y and Z axes.
  * `y`: Repeat space on the X and Z axes.
  * `z`: Repeat space on the X and Y axes.
* `Size`: The spacing of the grid along the two axes. This sets the size of the cell taken from the input.
* `Offset`: Shifts where the input cell is taken from without moving the position of the grid.
* `Shift`: Shifts the whole grid (and its contents).
* `Mirrortype`: How the cells are varied.
  * `none`: All cells are treated the same.
  * `mirror`: Every other cell is flipped.
  * `grid`: Flip every other cell along the diagonal axis as well. This means that for an input with something in one corner, there will be groups of 4 cells with all those corners facing each other.
* `Iterationtype`: Whether and how to expose iteration values to upstream operators.
  * `none`: Pass along whatever is provided by the next op after this one.
  * `tiledquadrant`: For each cluster of 4 cells, output 0 for the top left, 1 for top right, 2 for bottom left,  and 3 for bottom right, and put that value in the x component, and set yzw to 0.
  * `cellcoord`: Use the cell coordinates as the x and y components of the iteration, with zw set to 0. Note that it always uses xy, even if the grid is along another plane.
  * `alternatingcoord`: Cell coordinates that alternate between 0 and 1 along both axes in xy, with zw set to 0.

## Inputs

* `definition_in`: 