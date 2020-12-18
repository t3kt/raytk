Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.

## Parameters

* `Enable`
* `Operation`: The type of combine operation.
  * `union`: Produces the combined area of both inputs.
  * `intersect`: Produces the area where both inputs overlap.
  * `diff`: Subtracts the second input from the first.
* `Swapinputs`: Swaps the order of the inputs. This is only used for the `diff` mode.
* `Radius`: The size of the blending region.
* `Useradiusfield`
* `Inspect`

## Inputs

* `definition_in_1`
* `definition_in_2`
* `radius_definition_in` *Radius Field*: Value field that can be used to vary the radius of the blend region at different points in space.