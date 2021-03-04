Combines SDFs in various ways.

Depending on which `Combine` option is selected, different parameters will be enabled.
This operator only supports two input SDFs (along with a value field to control blending).
To combine more than two SDFs, use one of the specialized operators like [`simpleUnion`](/raytk/reference/operators/combine/).

## Parameters

* `Enable`
* `Combine`: The type of combination operation to perform.
  * `simpleUnion`: The combined areas of each of the inputs.
  * `simpleIntersect`: The overlapping areas of each of the inputs.
  * `simpleDiff`: The first input with the second input removed from it.
  * `smoothUnion`: Like `simpleUnion` but with the intersecting edges rounded out.
  * `smoothIntersect`: Like `simpleIntersect` but with the intersecting edges rounded out.
  * `smoothDiff`: Like `simpleDiff` but with the intersecting edges rounded out.
  * `roundUnion`: Uses a quarter circle blending area along the edges.
  * `roundIntersect`
  * `roundDiff`
  * `chamferUnion`: Uses a 45 degree flat slope to blend along the edges.
  * `chamferIntersect`
  * `chamferDiff`
  * `stairUnion`: Uses vertical and horizontal stairs to blend along the edges.
  * `stairIntersect`
  * `stairDiff`
  * `columnUnion`: Uses multiple circular tubes to blend along the edges.
  * `columnIntersect`
  * `columnDiff`
* `Swapinputs`: Swaps the order of the inputs. This is only relevant for "diff" modes.
* `Radius`: The size of the blending region.
* `Number`: For stair and column modes, this controls how many steps are used in the blending regions.

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `radius_field_definition_in`: 