A field that uses HSV-based parameters to produce colors.

By default, the X axis is used for the hue.

## Parameters

* `Hueoffset`
* `Saturation`
* `Value`
* `Coordtype`
  * `useinput`
  * `float`
  * `vec2`
  * `vec3`
* `Contexttype`
  * `useinput`
  * `auto`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`

## Inputs

* `hue_field_definition_in`: Optional field that can calculate the hue setting based on position or other attributes.
* `saturation_field_definition_in`: Optional field that can calculate the saturation setting based on position or other attributes.
* `value_field_definition_in`: Optional field that can calculate the value setting based on position or other attributes.