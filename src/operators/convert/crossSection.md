Takes a 3D (or 2D) operator and take a cross section of it across a plane or a single axis.

## Parameters

* `Enable`
* `Axes`
  * `x`: Produces a 1D result that samples along the X axis.
  * `y`: Produces a 1D result that samples along the Y axis.
  * `z`: Produces a 1D result that samples along the Z axis.
  * `xy`: Produces a 2D result that samples on the XY plane.
  * `yx`: Produces a 2D result that samples on the YX plane.
  * `yz`: Produces a 2D result that samples on the YZ plane.
  * `zy`: Produces a 2D result that samples on the ZY plane.
  * `xz`: Produces a 2D result that samples on the XZ plane.
  * `zx`: Produces a 2D result that samples on the ZX plane.
* `Offset`: Offsets the plane or axis where the input is sampled.

## Inputs

* `definition_in`: 