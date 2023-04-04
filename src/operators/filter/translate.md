Translates coordinates of the input ROP.

Translate can be used in 2D or 3D.

It can either specify an offset for each axis, or a direction and a distance.

When specifying an offset for each axis, it can optionally use a vector field to apply variable amounts of translation based on coordinates.
If a field is used, the field values are added to the Translate XYZ parameter.

When specifying a direction and distance, it can optionally use a field to add to the distance specified in the Distance parameter.

## Parameters

* `Enable`
* `Translatemode`: How to specify the amount of translation.
  * `axes`
  * `dir`
* `Translate`: Amount of translation along each axis. For 2D, only X and Y are used.
* `Direction`: Vector indicating which direction to move towards. A value of 1,0,0 would move to the right on the X axis, and 0,-1,0 would move down on the Y axis.
* `Distance`: How far to move in the specified direction.
* `Coordtype`
  * `auto`
  * `vec2`
  * `vec3`
* `Target`
  * `coords`
  * `sdfuv`
  * `sdfuv2`
  * `matuv`
  * `value`

## Inputs

* `definition_in`: 
* `translateField`:  If provided, this field is used to control the amount of translation at each point in space. If the field returns a float (or SDF), the `Translate` parameter is *multiplied* by that value. If it returns a vec4, the parts are *added* to the `Translate` parameter parts.
* `distanceField`: If provided, this field is used to add to the distance that space is moved.
* `directionField`: 