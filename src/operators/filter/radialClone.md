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
  * `union`: Show all the shapes, without any special treatment for overlap between them.
  * `smoothunion`: Smooths overlaps between the copies.
* `Mergeradius`: The amount of smoothing to apply when merging copies.
* `Iterationtype`: Whether and how to expose iteration values to upstream operators.
  * `none`: Pass along whatever is provided by the next op after this one.
  * `index`: Use the copy index (from 0 to `Count`-1) as the x iteration value.

## Inputs

* `definition_in`: 