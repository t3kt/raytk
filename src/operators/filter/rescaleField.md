Rescales the values produced by a field.

This is equivalent to the "Range" parameters in a Math CHOP.

It works for either float value fields or vector fields. When using a float value field, only the first part of each of the range parameters is used.

## Parameters

* `Enable`
* `Inputlow`: The low end of the expected input values.
* `Inputhigh`: The high end of the expected input values.
* `Outputlow`: The low end of the rescaled value range.
* `Outputhigh`: The high end of the rescaled value range.

## Inputs

* `definition_in`: 