Applies a transform based on a range of settings, mapped with either the iteration value or a field input.

This operator defines two different sets of transform settings. It then uses some index value to decide
where in that range it will use. A simple use case for this would be iteration with 3 items, where the
first item moves to one position and the last item moves to another position, and the one in the middle
moves to half way between those two.

The index is based either on the first (x) part of the iteration value provided by a downstream op, or
if the second input is connected, that float value field is used to determine the index.
The index is then scaled from the specified range down to 0..1. The `Extend` parameter controls how
values outside that range are handled.


## Parameters

* `Enable`
* `Indexrange`: The range of index values that are expected. The first value will use `Translate1` and the second will use `Translate2`.
* `Extendmode`: How to handle index values outside of `Indexrange`.
  * `linear`: Linearly scale values, which is like making a graph with a line between the two settings, and then just extending that line in the same direction as it goes past 1 (and before 0).
  * `clamp`: Clamp the index values to the range.
  * `loop`: Loop the values over the range.
* `Enabletranslate`: Wheteher to use translation.
* `Translate1`: Translate setting for the beginning of the range.
* `Translate2`: Translate setting for the end of the range.
* `Enablerotate`: Whether to use rotation.
* `Rotate1`: Rotate setting for the beginning of the range.
* `Rotate2`: Rotate setting for the end of the range.

## Inputs

* `definition_in`: 
* `index_field_definition_in` *Index Field*: Optional float value field to use instead of the iteration value. It is passed the current coordinates.