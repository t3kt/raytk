Limits the values produced by a float or vector field.

This is similar to the Limit CHOP.

## Parameters

* `Enable`
* `Limittype`
  * `off`: Don't apply any limiting.
  * `clamp`: Clamp the values to the range.
  * `loop`: Wrap values around the range.
  * `zigzag`: Similar to "loop" but zigzags back and forth across the range.
* `Low`
* `High`

## Inputs

* `definition_in`: 