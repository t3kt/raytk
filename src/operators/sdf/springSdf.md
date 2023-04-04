A coiled spring shape.

This is similar to `helixSdf`, but with the fixed height rather than infinite.

## Parameters

* `Axis`
  * `x`
  * `y`
  * `z`
* `Reverse`
* `Radius`: The radius of the spring, i.e. the distance of the spring from the center axis.
* `Height`: Height or length of the spring.
* `Coils`: The number of rotations in the spring. Larger values mean a tighter coil.
* `Thickness`: Thickness of the spring, used when no cross-section SDF is attached.

## Inputs

* `heightField`: 
* `radiusField`: 
* `coilsField`: 
* `thicknessField`: 
* `crossSection`: Optional 2D SDF used as the cross-section for the shape.

## Variables

* `axisoffset`: 
* `normoffset`: 
* `angle`: 
* `normangle`: 