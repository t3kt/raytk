Material that uses phong shading.

## Parameters

* `Enable`
* `Ambientcolor`: Base color applied to the surface regardless of lights.
* `Diffusecolor`: Color reflected by matte surfaces.
* `Specularcolor`: Color reflected by glossy surfaces.
* `Shine`: Specular exponent, which adjusts the light curve of specular highlights.
* `Enableshadow`: Whether to use shadows. When enabled, if the *Shadow Definition* input is provided, that will be used. Otherwise a default shadow function will be used.
* `Inspect`
* `Help`

## Inputs

* `definition_in`
* `shadow_definition_in` *Shadow Definition*: Used to customize the behavior of shadows for the material. Only used if `Enableshadow` is on.