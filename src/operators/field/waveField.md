A field that uses a periodic wave.

If there is an input, that rop is used to get the coordinate that is fed into the wave function.
Without an input, the Axis is used to run the wave function on the position along the selected axis.

## Parameters

* `Enable`
* `Function`: The type of wave.
  * `sin`
  * `cos`
  * `tri`
  * `ramp`
  * `square`
* `Axis`: If there is no input, the coordinate along this axis is used for the wave function phase.
  * `x`
  * `y`
  * `z`
* `Coordtype`
  * `float`
  * `vec2`
  * `vec3`
* `Contexttype`
  * `useinput`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Period`: The length of a single cycle of the wave.
* `Phase`: Offset of the wave along the axis / coordinates.
* `Amplitude`: The height of the wave, which scales the range of output values. If this is set to 3 (and `Offset` is 0), a ramp wave will produce values from 0 to 3.
* `Offset`: Adds to the values produced by the wave. If this is set to 0.5 (and `Amplitude` is set to 1), a ramp wave will produce values from 0.5 to 1.5.
* `Inspect`

## Inputs

* `definition_in` *Wave Coordinate Source*: If attached, the wave will use this to determine the numbers that it passes to the wave function (instead of using the position along the chosen `Axis`).