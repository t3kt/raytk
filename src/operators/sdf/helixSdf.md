SDF for a helix (an elongated spiral).

There are two variations of the helix: dual and single.
The dual variation can do two parallel rails, and supports using a 2D cross-section SDF, but no UV coordinates.
The single variation is just one part, and does not support cross-sections, but does have UV coordinates.

The single variation is based on [Helix Distance](https://www.shadertoy.com/view/MstcWs) by tdhooper.

## Parameters

* `Enable`
* `Axis`
  * `x`
  * `y`
  * `z`
* `Translate`
* `Radius`
* `Thickness`
* `Spread`
* `Dualspread`
* `Helixtype`
  * `dual`
  * `single`
* `Reverse`

## Inputs

* `thicknessField`:  Field used to multiply the `Radius` parameter. If it uses 1D coordinates, it is provided the position along the axis. If it uses 3D coordinates, it uses the absolute position.
* `radiusField`:  Field used to multiply the `Thickness` parameter. If it uses 1D coordinates, it is provided the position along the axis. If it uses 3D coordinates, it uses the absolute position.
* `spreadField`: 
* `crossSection`: 

## Variables

* `axisoffset`: 
* `angle`: 
* `normangle`: 