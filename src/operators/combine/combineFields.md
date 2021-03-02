Combines float or vector fields using one of several mathematical operations.

## Parameters

* `Enable`
* `Operation`: What operation to use to combine the field values.
  * `off`: Only use the first input (or second depending on `Swaporder`).
  * `add`: Add the fields.
  * `sub`: Subtract the second from the first.
  * `mul`: Multiply the fields.
  * `div`: Divide the first by the second.
  * `avg`: Average the fields.
  * `min`: Use the smaller of the field values.
  * `max`: Use the larger of the field values.
* `Swaporder`: Swaps the two inputs. This is only relevant for some of the `Operation` values.

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 