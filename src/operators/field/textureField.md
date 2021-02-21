A float or vector field that looks up values from a texture.

## Parameters

* `Enable`
* `Coordtype`: The type of coordinates used for UV mapping.
  * `float`: Uses the 1D coordinate as U and 0 for V.
  * `vec2`: Uses the provided 2D coordinates.
  * `vec3`: Uses the specified `Axis` to choose which axes to use for U and V.
* `Returntype`
  * `float`
  * `vec4`
* `Contexttype`: When used for materials, set to `MaterialContext`, otherwise use `Context`.
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Axis`: When using 3D coordinates, the axis that faces the plane used for UV. This is not used when a UV field input is attached.
  * `x`: U=Y, V=Z
  * `y`: U=Z, V=X
  * `z`: U=X, V=Y
* `Translate`: Offsets the UV coordinates.
* `Scale`: Scales the UV coordinates.
* `Texture`: TOP used for the texture.
* `Extendmode`: How to handle UV coordinates outside the 0..1 range.
  * `hold`
  * `zero`
  * `repeat`
  * `mirror`

## Inputs

* `uv_field_definition_in` *UV Map Field*: When provided, this field is used to calculate the UV coordinates (in the x and y parts of the vec4).