Material with a basic lighting model.

The material combines several elements to determine the color of a given surface point.

First, the base color uses the `Basecolor` parameter and optionally the `Base Color Field` input.
Next, the specular color uses the color and relative position of the light.
Third, the "Sky" color acts as a simple pseudo light, that uses the surface normal but doesn't support shadows.

## Parameters

* `Enable`
* `Basecolor`
* `Skycolor`: Color of the "sky" pseudo-light.
* `Skyamount`: Amount of "sky" light to apply.
* `Skydir`: Vector of the direction where the "sky" light comes from.
* `Specularamount`: Amount of specular light color to apply.
* `Specularexp`: Controls the sharpness of the specular color rolloff.
* `Enableshadow`: Whether to use shadows. If this is enabled, and the `Shadow` input is connected, that type of shadow is used. If it is enabled but that input is not connected, the default shadow is used.
* `Uselocalpos`: Whether to use the "local" position relative to the input shape when looking up colors using the `Base Color Field` input. If enabled, the coordinates used for the color field will be "before" any downstream transformations are applied. When disabled, the final global position where a point ends up in the render is used instead.

## Inputs

* `definition_in`: 
* `baseColor_definition_in`: 