Switches between inputs based on the iteration value provided by a downstream operator.

Only connected inputs are considered, and they are renumbered to skip over any missing ones. So if
only 2 and 4 are connected, they are treated as 1 and 2.

Iteration values are rounded to the nearest integer (after the `Extend` mode is applied to handle values
outside the expected range from 0 to the number of connected inputs minus 1.

## Parameters

* `Enable`
* `Iterationpart`: Which component of the iteration vector to use. In most cases this should be X.
  * `x`
  * `y`
  * `z`
  * `w`
* `Extend`: How to handle iteration values outside the 0..(N-1) range. 
  * `clamp`: Clamp iteration to 0..(N-1) range.
  * `loop`: Loop from 0 to N-1.
  * `zigzag`: Zig-zag back and forth between 0 and N-1.

## Inputs

* `definition_in_1`:
* `definition_in_2`:
* `definition_in_3`: 
* `definition_in_4`: 