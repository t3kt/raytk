Switches between inputs based on the iteration value provided by a downstream operator.

## Parameters

* `Enable`
* `Iterationpart`: Which component of the iteration vector to use. In most cases this should be X.
  * `x`
  * `y`
  * `z`
  * `w`
* `Extend`: How to handle iteration values outside the 0..1 range. 
  * `clamp`: Clamp iteration to 0..1 range.
  * `loop`: Alternate between 0 for even numbers and 1 for odd numbers.

## Inputs

* `definition_in_1`: The input that should be used when the iteration is 0 (or more accurately < 0.5).
* `definition_in_2`: The input that should be used when the iteration is 1 (or more accurately >= 0.5).