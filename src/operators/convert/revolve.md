Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.

## Parameters

* `Axis`
  * `x`
  * `y`
  * `z`
* `Radialoffset`: Moves the cross-section shape closer or further from the axis.
* `Axisoffset`: Moves the resulting shape along the axis.

## Inputs

* `cross_section_definition_in`:  The 2D shape that is revolved around the axis.
* `rotate_field_in`: Optional field that controls rotation of the cross-section as it goes around the axis.
* `scale_field_in`: Optional field that controls scale of the cross-section as it goes around the axis.
* `translate_field_in`: Optional field that controls translate of the cross-section as it goes around the axis.