Modifies space using a vector field.

When the shader uses the operator, it will first pass the coordinates to the "Coord Field". It then uses the resulting remapped coordinates when running the first input operator.

## Parameters

* `Enable`
* `Remapmode`: How the remapped coordinates are applied to the original coordinates.
  * `replace`: Totally replace the original coordinates with the new ones that came from the "Coord Field".
  * `add`: Add the new coordinates to the original ones.
  * `multiply`: Multiply the new coordinates with the original ones.
* `Mix`: Cross-fades between the original coordinates and the remapped ones.

## Inputs

* `definition_in`: 
* `coord_field_definition_in`: 