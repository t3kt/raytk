Combines SDFs using a smooth union operator.

Produces the combined areas of the input shapes, blended to smooth out the intersections.

## Parameters

* `Enable`
* `Amount`: Size of the blending region.
* `Inspect`

## Inputs

* `definition_in_1`: The first SDF to combine.
* `definition_in_2`: The second SDF to combine.
* `definition_in_3` *Radius Field*: Float value field that can vary the amount of blending at different points in space.