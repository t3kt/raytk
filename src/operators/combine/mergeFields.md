Merges multiple vector fields, using different fields for each vector part.

This is similar to the Reorder TOP. Each of the 4 vector parts (xyzw) has its own source setting specifying which input its value comes from.

Inputs can either be float fields, or vector fields. If they are vector fields, then the corresponding part of that vector is used when creating the output. For example, if input 3 is a vector field, and `Source Z` is set to `Input 3`, the `z` in the result will be `input1.z`.

## Parameters

* `Enable`
* `Sourcex`
  * `zero`
  * `one`
  * `input1`
  * `input2`
  * `input3`
  * `input4`
* `Sourcey`
  * `zero`
  * `one`
  * `input1`
  * `input2`
  * `input3`
  * `input4`
* `Sourcez`
  * `zero`
  * `one`
  * `input1`
  * `input2`
  * `input3`
  * `input4`
* `Sourcew`
  * `zero`
  * `one`
  * `input1`
  * `input2`
  * `input3`
  * `input4`

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `definition_in_3`: 
* `definition_in_4`: 