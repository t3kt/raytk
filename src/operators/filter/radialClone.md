Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.

## Parameters

* `Enable`
* `Axis`: The axis around which to rotate the copies.
  * `x`
  * `y`
  * `z`
* `Count`: The number of copies. The performance cost of the input is multiplied by this number.
* `Anglerange`: The angle spread around the axis, where the copies are distributed.
* `Angleoffset`: Shifts the angle of the first copy around the axis.
* `Radiusoffset`: Offsets the copies towards/away from the axis. At zero, all copies will be centered on the axis.
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
* `Iterationtype`: Whether and how to expose iteration values to upstream operators.
  * `none`: Pass along whatever is provided by the next op after this one.
  * `index`: Use the copy index (from 0 to `Count`-1) as the x iteration value.
* `Rotatemode`: Whether the copies should be rotated or just positioned in a ring in their original orientation.
  * `both`
  * `pos`
* `Mergenumber`
* `Mergeoffset`

## Inputs

* `definition_in`: 
* `radialOffsetField`: 
* `angleOffsetField`: 
* `blendRadiusField`: 

## Variables

* `index`: Index of the current clone (0..N)
* `normindex`: Index of the current clone, scaled to a 0..1 range.
* `rotaccum`: Amount of rotation applied for the current clone (0..360).
* `normrotaccum`: Amount of rotation applied for the current clone, scaled to 0..1 range.