Pattern of stacked rectangular bricks.

This pattern produces just float values not colors. To apply color to it, pass it into a `colorRampField`.

The bricks themselves produce values of 0 (or black) and the spaces between them produce values of 1 (or white).

## Parameters

* `Shift`: Offsets every other row of bricks. A value of 0 means a regular grid, and 0.5 is a standard staggered brick layout.
* `Translate`: Moves the entire pattern.
* `Size`: Scales the pattern.
* `Thickness`: Thickness of the spacing between the bricks.
* `Blending`: Amount of blending between bricks and spacing.

## Inputs

* `coordField`: Field that produces vectors that the pattern uses as coordinates instead of regular spatial position. Only the X and Y parts are used.
* `thicknessField`: Field that controls the thickness of the spacing between bricks.
* `blendingField`: Field that controls the amount of blending between bricks and spacing.
* `shiftField`: Field that controls how much alternating rows are shifted.