Repeats its input some number of times, exposing the index as the iteration x value, and combines the results.

It is important to note that unless something in the input chain is making use of the iteration to change or
move those copies, they will all be in the same position. The `rangeTransform` operator is designed for this
purpose, though there are also other ops that can do so.

Refer to the Iteration guide for details.

It is also important to note that this operator, like `radialClone` evaluates its input separately for each
iteration, which can cause a significant drain on resources if the input network is complex or costly.

## Parameters

* `Enable`
* `Instancecount`: The number of copies to produce and merge.
* `Combine`: How to combine the copies. Only the "simple" options are guaranteed to work properly. The others may produce unexpected and problematic results.
  * `simpleUnion`: Combines the shapes so that all of their volumes are included.
  * `simpleIntersect`: Combines the shapes so that only the places where all overlap are included.
  * `simpleDiff`: Subtracts the second copy from the first, the third from that, and so on.
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
* `Radius`
* `Mergenumber`
* `Mergeoffset`
* `Enabletransform`
* `Transformchop`: A CHOP containing channels `tx ty tz` and/or `rx ry rz` that specifies the translate and/or rotate for each instance.
* `Enabletranslate`
* `Enablerotate`
* `Enableactivechop`
* `Activechop`: A CHOP containing a channel named `active`, which is used to selectively turn instances off. Any instance with an active value of 0 or less will be excluded from the combined result.

## Inputs

* `definition_in`: 
* `radiusField`: 

## Variables

* `index`: 
* `normindex`: 