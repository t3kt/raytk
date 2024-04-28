Repeats an SDF along a line, combining the results.

Note that this multiplies the work of the input for each clone, meaning that 4 clones means 4x the work of whatever is connected to the input.

The `modulo1D` can be a cheaper alternative to `linearClone` though it comes with limitations.

## Parameters

* `Enable`
* `Count`: The number of copies. The performance cost of the input is multiplied by this number.
* `Translate1`: Position of the start of the line of clones.
* `Translate2`: Position of the end of the line of clones.
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
* `Iterationtype`: Whether and how to expose iteration values to upstream operators.
  * `none`
  * `index`

## Inputs

* `definition_in`: 
* `blendRadiusField`: 

## Variables

* `index`: 
* `normindex`: 