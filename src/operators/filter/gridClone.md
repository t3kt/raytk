Repeats an SDF in a grid arrangement, combining the results.

It's important to remember that this operator performs the work of its input once *for each clone*. That means that a 3x3 grid does 27 times the work of the input.

The `modulo3D` (or `modulo1D`/`modulo2D`) can be a cheaper alternative to `gridClone` with some limitations.

## Parameters

* `Enable`
* `Count`: The number of copies. The performance cost of the input is multiplied by this number.
* `Center`: Center position of the grid.
* `Size`: Size of the grid on each axis.
* `Mergetype`: How to merge the copies.
  * `simpleUnion`
  * `simpleIntersect`
  * `simpleDiff`
  * `smoothUnion`
  * `smoothIntersect`
  * `smoothDiff`
  * `roundUnion`
  * `roundIntersect`
  * `roundDiff`
  * `chamferUnion`
  * `chamferIntersect`
  * `chamferDiff`
  * `stairUnion`
  * `stairIntersect`
  * `stairDiff`
  * `columnUnion`
  * `columnIntersect`
  * `columnDiff`
  * `simpleXOR`
* `Mergeradius`: The amount of smoothing to apply when merging copies.
* `Mergenumber`
* `Mergeoffset`

## Inputs

* `definition_in`: 
* `blendRadiusField`: 

## Variables

* `coord`: grid cell coordinates for each axis, going from 0..N.
* `normcoord`: grid cell coordinates scaled to 0..1 range.