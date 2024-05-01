Repeats space in a spherical mesh layout with rows and columns.

## Parameters

* `Enable`
* `Repetitions`: How many rows and columns to have.
* `Shift`: Shifts the repetitions across the rows and columns.
* `Offset`: Shifts the contents of each repetition, away from the sphere center or side to side along the columns.
* `Pivot`: Center point of the sphere
* `Mirrortype`: Flips alternating repetitions so they mirror each other.
  * `none`
  * `rows`
  * `cols`
  * `grid`

## Inputs

* `definition_in`: 
* `repetitionsField`: 
* `offsetField`: 
* `shiftField`: 

## Variables

* `cell`: Index of the row and column as integers (0..N).
* `normcell`: Index of the row and column scaled to a 0..1 range based on the number of Repetitions.