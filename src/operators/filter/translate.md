Translates coordinates of the input ROP.

Translate can be used in 2D or 3D.
It can optionally use a vector field to apply variable amounts of translation based on coordinates.
If a field is used, the field values are added to the Translate XYZ parameter.

## Parameters

* `Enable`
* `Translate`: Amount of translation along each axis. For 2D, only X and Y are used.
* `Inspect`
* `Help`

## Inputs

* `definition_in`
* `translate_field_definition_in` *Translate Field*: If provided, this field is used to control the amount of translation at each point in space. If the field returns a float (or SDF), the `Translate` parameter is *multiplied* by that value. If it returns a vec4, the parts are *added* to the `Translate` parameter parts.