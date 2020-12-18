Slices space into a grid, and places each input in a separate cell.

This is useful to see several different variations of a shape.
The input shapes are shifted to the center of their cell.


## Parameters

* `Enable`
* `Layout`: How to arrange the cells.
  * `row`: Slice space into cells horizontally. The first cell extends off infinitely to the left and the last cell extends infinitely off to the right.
  * `column`: Slice space into cells vertically.
  * `gridrow`: Slice space into 4 cells arranged in a grid.
* `Axis`: The plane along which to arrange the cells.
  * `x`
  * `y`
  * `z`
* `Size`: The size of the cells
* `Prescale`: Scales the inputs within their cells.
* `Inspect`