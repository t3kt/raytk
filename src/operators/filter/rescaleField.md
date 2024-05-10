Rescales the values produced by a field.

This is equivalent to the "Range" parameters in a Math CHOP.

It works for either float value fields or vector fields. When using a float value field, only the first part of each of the range parameters is used.

## Parameters

* `Enable`
* `Inputlow`: The low end of the expected input values.
* `Inputhigh`: The high end of the expected input values.
* `Outputlow`: The low end of the rescaled value range.
* `Outputhigh`: The high end of the rescaled value range.
* `Returntype`
  * `auto`
  * `float`
  * `vec4`
* `Multiply`: Multiplier value applied to all parts of the values after range scaling.
* `Mult`: Multiplier values applied to each part of the values after range scaling.
* `Postadd`: Amounts added to the rescaled values after all other steps.

## Inputs

* `definition_in`: 