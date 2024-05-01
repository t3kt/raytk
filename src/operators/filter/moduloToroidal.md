Repeats space as rows and columns of a torus-shaped grid.

## Parameters

* `Enable`
* `Axis`: Axis that the torus is around.
  * `x`
  * `y`
  * `z`
* `Radius`: Primary radius of the torus around the main axis.
* `Thickness`: Thickness of the torus.
* `Repetitions`: Number of rows and columns across the torus.
* `Shift`: Shifts the repetitions across the rows and columns of the torus.
* `Mirrortype`: Flips alternating repetitions so they mirror each other.
  * `none`
  * `rows`
  * `cols`
  * `grid`

## Inputs

* `definition_in`: 
* `repetitionsField`: 
* `radiusField`: 
* `thicknessField`: 
* `shiftField`: 

## Variables

* `cell`: Index of the row and column as integers (0..N).
* `normcell`: Index of the row and column scaled to a 0..1 range based on the number of Repetitions.
* `angle`: Angle around the main axis as degrees (0..360).
* `normangle`: Angle around the main axis, scaled to a 0..1 range.
* `innerangle`: Angle around the inner body of the torus as degrees (0..360).
* `norminnerangle`: Angle around the inner body of the torus, scaled to a 0..1 range.