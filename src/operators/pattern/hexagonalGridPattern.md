Hexagonal grid pattern.

This operator produces different types of values from the grid depending on the selected Pattern.

## Parameters

* `Pattern`: What type of values to produce from the grid.
  * `hexgrid`: Produces float values, with 1 for the grid cells, and 0 for the edges between cells.
  * `hexdist`: Produces float values with the distance scaled so that edges are 0 and cell centers are 1.
  * `hex3`: Produces float values which mark each cell with either 0, 0.5, or 1, such that no two adjacent cells are the same.
  * `hex3color`: Produces vectors with colors where 3 chosen colors are applied to cells, such that no two adjacent cells are the same.
* `Translate`: Moves the entire pattern.
* `Size`: Scales the pattern.
* `Thickness`: Thickness of the edges between the cells.
* `Blending`: Amount of blending between cells and edges.
* `Polycolor1`: Color 1 to use for cells (when applicable).
* `Polycolor2`: Color 2 to use for cells (when applicable).
* `Polycolor3`: Color 3 to use for cells (when applicable).

## Inputs

* `coordField`: Field that produces vectors that the pattern uses as coordinates instead of regular spatial position. Only the X and Y parts are used.
* `thicknessField`: Field that controls the thickness of the edges between cells.
* `blendingField`: Field that controls the amount of blending between cells and edges.
* `polyColor1Field`: Field to provide cell color 1.
* `polyColor2Field`: Field to provide cell color 2.
* `polyColor3Field`: Field to provide cell color 3.