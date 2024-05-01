Repeats space in a 2d grid where some cells are subdivided into smaller cells recursively.

## Parameters

* `Enable`
* `Axis`: Axis that the grid plane faces.
  * `x`
  * `y`
  * `z`
* `Division`: Number of steps of subdividing.
* `Chance1`: Likelyhood of a cell getting one level of subdivision.
* `Chance2`: Likelyhood of a sub-divided cell getting another level of subdivision.
* `Offset`: Moves the contents within each repeated cell.
* `Shift`: Move the entire arrangement of cells.
* `Enablerescale`: Whether to apply uniform scaling within each cell so that the contents fit the size of the cell.
* `Iterationtype`: How to expose the cell information as iteration values for upstream operators to use.
  * `none`
  * `cell`
* `Seed`: Seed number used as the basis of the randomization.

## Inputs

* `definition_in`: Main input which appears within each cell.
* `shiftField`: Field that controls the shifting of the overall grid layout.
* `offsetField`: Field that controls the offsetting of the contents within each cell.

## Variables

* `cell`: Randomization values different for each cell, but without a predictable layout.
* `layer`: Which layer of subdivision the current cell has.