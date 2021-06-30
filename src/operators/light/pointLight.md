Light eminating from a single point in space, with optional distance attentuation.

## Parameters

* `Position`: The point from which the light eminates.
* `Intensity`: Brightness of the light.
* `Color`: Color of the light.
* `Enableattenuation`: Whether to limit the light range.
* `Attenuationstart`: The distance at which the light starts to dim.
* `Attenuationend`: The distance at which the light is fully dimmed.

## Inputs

* `color_field_definition_in`: Optional field that can control the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.
* `attenutation_field_definition_in`: Optional field/function that controls the slope and coloration of the attentuation rolloff is shaped. It can be used to make the light shift from one color to another, or to control the sharpness of the rolloff.