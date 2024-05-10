Cylinder, either solid or a hollow tube.

## Parameters

* `Translate`: Shifts the center of the cylinder.
* `Radius`: The radius of the cylinder.
* `Height`: The height of the cylinder, along the selected axis.
* `Axis`
  * `x`
  * `y`
  * `z`
* `Infiniteheight`: Whether to extend infinitely along the chosen axis or have a limited height.
* `Hollow`: Whether to make the cylinder a hollow tube instead of a solid cylinder.
* `Thickness`: Thickness of the walls of the tube when using hollow mode.

## Inputs

* `heightField`:  Optional field used to control the radius of the cylinder. If it uses 1D coordinates, it is given the position along the axis. For 3D coordinates, it is given the raw position.
* `radiusField`: 
* `thicknessField`: 

## Variables

* `axispos`: 
* `normoffset`: 
* `normangle`: 