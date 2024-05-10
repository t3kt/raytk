Switches or blends between several inputs, without the need to rebuild the shader, allowing for fast switching.

Note that inputs that are not connected are skipped over when assigning numbers to them, so if inputs 1, 2, and 4 are connected, they will use indices 0, 1, 2.

## Parameters

* `Enable`
* `Source`: When 0, the first source is used, 1 for the second, etc.
* `Blend`: Whether to blend between inputs.
* `Indexfield`: Field that can provide index values instead of using the parameter.
* `Indexmode`: How to map index values to inputs.
  * `zeroindex`: First is 0, second is 1, and so on.
  * `oneindex`: First is 1, second is 2, and so on.
  * `norm`: Scaled to a 0..1 range, so 0 is the first and 1 is the last.
* `Extend`: How to handle indices that are outside the expected range based on the selected Index Mode.
  * `clamp`
  * `loop`
  * `zigzag`

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `definition_in_3`: 
* `definition_in_4`: 
* `definition_in_5`: 
* `definition_in_6`: 
* `definition_in_7`: 
* `definition_in_8`: 
* `indexField`:  Field used to choose the source index