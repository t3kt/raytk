Cone-shaped spotlight.

This is similar to the Light COMP in spotlight mode.

## Parameters

* `Intensity`: Brightness that is applied to the `Color`.
* `Color`: Color of the light.
* `Position`: The position of the tip of the light cone.
* `Direction`: The direction which the cone faces, as a vector.
* `Coneangle`: The width of the cone.
* `Conedelta`: The amount of blending between the inside and the outside of the cone.
* `Enableattenuation`: Whether to limit the light range.
* `Attenuationstart`: The distance at which the light starts to dim.
* `Attenuationend`: The distance at which the light is fully dimmed.
* `Rotate`: Rotation for the direction that the light faces.
* `Enablelookat`: Whether the light should face a specific position.
* `Lookatpos`: Coordinates that the light should face.
* `Upvec`: Up vector used to orient the light.
* `Enableshadow`: Whether the light should produce shadows.

## Inputs

* `colorField`:  Optional field that controls the color of the light.
* `colorField`: Field controls the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.
* `attenuationField`: Field/function that controls the slope and coloration of the attenuation rolloff is shaped. It can be used to make the light shift from one color to another, or to control the sharpness of the rolloff.
