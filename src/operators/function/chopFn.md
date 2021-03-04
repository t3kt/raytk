Function that looks up values in a CHOP.

## Parameters

* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Chop`: The CHOP that values are pulled from.
* `Extendmode`: How to handle coordinates outside the range.
  * `hold`: Extends the first/last value on each end.
  * `zero`: Produces a value of zero outside the range.
  * `repeat`: Repeats the range.
  * `mirror`: Repeats the range but flips every other part.
* `Range`: The range of indices to map to the full range of the CHOP.