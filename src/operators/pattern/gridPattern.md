Rectangular grid pattern.

This operator produces different types of values from the grid depending on the selected Format.

## Parameters

* `Format`: What type of values to produce from the pattern.
  * `edge`: Produces float values, with 0 for the grid cells and 1 for the edges between cells.
  * `dist`: Produces float values with the raw distance from the edge, like an SDF.
  * `normdist`: Produces float values with the distance scaled so that edges are 0 and cell centers are 1.
  * `color`: Produces vectors with the chosen color for the cells and the edges.
* `Translate`: Moves the entire pattern.
* `Size`: Scales the pattern.
* `Thickness`: Thickness of the edges between the cells.
* `Blending`: Amount of blending between cells and edges.
* `Fillcolor`: Color to use for the cells (when applicable).
* `Edgecolor`: Color to use for the edges (when applicable).

## Inputs

* `coordField`: Field that produces vectors that the pattern uses as coordinates instead of regular spatial position. Only the X and Y parts are used.
* `spacingField`: Field that controls the sizing of the grid cells.
* `thicknessField`: Field that controls the thickness of the edges between cells.
* `blendingField`: Field that controls the amount of blending between cells and edges.
* `fillColorField`: Field that provides colors for the cells.
* `edgeColorField`: Field that provides colors for the edges.