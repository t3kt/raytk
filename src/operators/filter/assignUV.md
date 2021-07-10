Assigns UV coordinates to an SDF surface.

Coordinates can either be determined using the selected `UV Mode`, or using a vector field input.

## Parameters

* `Enable`
* `Uvmode`
  * `xyz`
  * `xy`
  * `yx`
  * `yz`
  * `zy`
  * `xz`
  * `zx`
  * `cylindricalx`
  * `cylindricaly`
  * `cylindricalz`
  * `spherical`

## Inputs

* `definition_in`: SDF definition to which the UVs are applied.
* `uv_field_in`: Optional field used to calculate the UV coordinates.