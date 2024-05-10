Light that emits from a single point in space.

## Parameters

* `Position`: The point from which the light emits.
* `Intensity`: Brightness that is applied to the `Color`.
* `Color`: Color of the light.
* `Enableattenuation`: Whether to limit the light range.
* `Attenuationstart`: The distance at which the light starts to dim.
* `Attenuationend`: The distance at which the light is fully dimmed.

## Inputs

* `colorField`: Field controls the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.
* `attenuationField`: Field/function that controls the slope and coloration of the attenuation rolloff is shaped. It can be used to make the light shift from one color to another, or to control the sharpness of the rolloff.
