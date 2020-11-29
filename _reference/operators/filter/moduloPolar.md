---
layout: page
title: moduloPolar
parent: Filter Operators
grand_parent: Operator Categories
---

Repeats space radially, like a kaleidoscope.

* `Axis` - The axis around which space is sliced.
* `Repetitions` - The number of angle repetitions. For example, a value of 6 would mean 6 slices of space, each with a 60 degree width.
* `Round To Integer` - Whether to round the `Repetitions` (and `Limit Low` and `Limit High`) to whole integers.
* `Pre Rotate` - Rotation applied before slicing.
* `Rotate` - Rotation applied after slicing.
* `Mirror Type` - Whether to flip every other slice. This is useful to avoid hard breaks at edges. It will result in the appearance of half as many slices, since half of them will be flipped.
* `Offset` - Distance to shift the shape before slicing it.
* `Use Limit` - Whether to limit the range of repetitions. Space outside that range will be left as it is.
* `Limit Low` - Start or the repetition range, in terms of the number of repetitions.
* `Limit High` - End or the repetition range, in terms of the number of repetitions.
* `Iterate On Cells` - Whether to expose the slice number as an "iteration" value for upstream ops.
