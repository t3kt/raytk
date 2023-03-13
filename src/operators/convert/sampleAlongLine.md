Samples a 2D/3D input along a single line, producing a 1D function.

It's similar to crossSection but with a single line instead of a 2D plane.

## Parameters

* `Center`: Position in 2D/3D space where the center of the line sits. When a position of 0 is passed to this operator, it will check its input at the Center location.
* `Direction`: Vector indicating which direction the line goes from the center.
* `Rotate`: Rotation for the sampling line.

## Inputs

* `definition_in`: 