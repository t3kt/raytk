Use an SDF to limit the area where a field produces values.

Within the specified bounds, the value from the first input field is used.

Outside the bounds, if there's a second input field, that is used instead. Otherwise the `Outside Value` parameter is used for those areas.

## Parameters

* `Enable`
* `Offset`: Offsets the edge of the bound area, expanding/collapsing it. This is equivalent to inserting a `round` operator.
* `Blending`: Range over which to fade from the main field to the outside field/param.
* `Outsidevalue`: Value to use outside the bounds, if there is no second field input.

## Inputs

* `inside`: 
* `outside`: 
* `boundVolume`: 