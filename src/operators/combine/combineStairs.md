Stair SDF combine, producing steps along the blend region.

## Parameters

* `Enable`
* `Operation`: The type of combine operation.
  * `union`: Produces the combined area of both inputs.
  * `intersect`: Produces the area where both inputs overlap.
  * `diff`: Subtracts the second input from the first.
* `Swapinputs`: Swaps the order of the inputs. This is only used for the `diff` mode.
* `Number`: The number of steps in the blending region.
* `Radius`: The size of the blending region.
* `Offset`: Shifts the steps along the blend region, with 0 being no shift, and 1 being a full shift of the total number of steps.

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `radius_definition_in`:  Value field that can be used to vary the radius of the blend region at different points in space, by *multiplying* the value of the `Radius` parameter.
* `offset_definition_in`:  Value field that can be used to vary the offset of the stairs at different points in space, by *adding* to the value of the `Offset` parameter.