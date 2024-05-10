Light that emits from a torus or ring shape.

## Parameters

* `Intensity`: Brightness that is applied to the `Color`.
* `Color`: Color of the light.
* `Axis`: The axis which the ring faces.
  * `x`
  * `y`
  * `z`
* `Position`: Center position of the ring.
* `Radius`: Radius of the ring.
* `Enableattenuation`: Whether to limit the light range.
* `Attenuationstart`: The distance at which the light starts to dim.
* `Attenuationend`: The distance at which the light is fully dimmed.
* `Enableshadow`: Whether the light should produce shadows.

## Inputs

* `colorField`: Field controls the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.
