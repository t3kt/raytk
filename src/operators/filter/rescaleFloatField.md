Simplified version of `rescaleField` that only has single settings vs vectors for each.

This can be applied to either float or vector fields. In the case of vector fields, the same settings are used for all parts of the incoming vectors.

## Parameters

* `Enable`
* `Inputrange`: The low/high ends of the expected input values.
* `Outputrange`: The low/high ends of the rescaled values.
* `Multiply`: Multiplier applied to values after range scaling.
* `Postadd`: Amount added to values after the other steps.

## Inputs

* `definition_in`: 