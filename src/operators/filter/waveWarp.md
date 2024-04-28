Uses repeating waves to offset space.

The `Axis` parameter determines which axis is used to produce the waves.

A separate wave is used for offsetting for each axis.

The `Period` and `Phase` parameters control the spacing and position of the waves.

The `Amplitude` and `Offset` parameters control how much each axis's wave shifts coordinates on that axis.

## Parameters

* `Enable`
* `Function`: Type of wave used to offset space.
  * `sin`
  * `cos`
  * `tri`
  * `ramp`
  * `rramp`
  * `square`
  * `addsquare2`
  * `addsquare4`
  * `addsquare8`
* `Axis`: The axis along which the waves are produced.
  * `x`
  * `y`
  * `z`
  * `dist`
* `Period`: The width of the waves for each axis.
* `Phase`: The phase of the waves for each axis.
* `Amplitude`: The scale of the movement for each axis.
* `Offset`: Offsets the movement for each axis.
* `Phaseoffset`: Offset applied to the wave phase separately for each axis.
* `Amplitudemult`: Multiplier applied to the wave amplitude separately for each axis.

## Inputs

* `definition_in`: 