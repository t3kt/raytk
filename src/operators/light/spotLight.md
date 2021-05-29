Cone-shaped spotlight.

This is similar to the Light COMP in spotlight mode.

## Parameters

* `Intensity`
* `Color`
* `Position`: The position of the tip of the light cone.
* `Direction`: The direction which the cone faces, as a vector.
* `Coneangle`: The width of the cone.
* `Conedelta`: The amount of blending between the inside and outside of the cone.
* `Enableattenuation`: Whether to adjust the amount of light depending on distance.
* `Attenuationstart`: The start of the blending range, inside which the light will be at full intensity.
* `Attenuationend`: The end of the blending range, outside which the light will be at zero intensity.

## Inputs

* `color_field_definition_in`: Optional field that controls the color of the light.
* `attenutation_field_definition_in`: Optional function that controls the color/intensity of the light based on the attenuation distance.