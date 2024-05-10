Light that emits from along an axis, similar to an infinitely long tube light.

## Parameters

* `Axis`: Axis that the limit emits from.
  * `x`
  * `y`
  * `z`
* `Position`: Position of the light. One axis of this won't be used since the light is infinite along one axis.
* `Rotate`: Rotates the light source.
* `Intensity`: Brightness that is applied to the `Color`.
* `Color`: Color of the light.
* `Enableattenuation`: Whether to limit the light range.
* `Attenuationstart`: The distance at which the light starts to dim.
* `Attenuationend`: The distance at which the light is fully dimmed.
* `Enableshadow`: Whether the light should produce shadows.

## Inputs

* `positionField`: Field offsets the position of the light. The coordinates that this field gets are the spot on the surface that the light is being calculated for.
* `colorField`: Field controls the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.
* `attenuationField`: Field/function that controls the slope and coloration of the attenuation rolloff is shaped. It can be used to make the light shift from one color to another, or to control the sharpness of the rolloff.

## Variables

* `lightdir`: Direction that the light is from the current position on a surface that's being shaded. This will be the closet point along the chosen axis.